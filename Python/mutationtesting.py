import os
import ast
import subprocess
import shutil
import re
import sys
from typing import Optional, Tuple, List, Dict, Set
from pymongo import MongoClient
from config import get_db_client
import Prompts
from collections import defaultdict

# --- Configuration ---
TEST_FILE_NAME = "test_generated_mutation.py"
CONFIG_FILE_NAME = "setup.cfg"
PY_FILES_DIR = "py_files"

# --- Configuration ---
# No minimum mutants required - accept any number generated


def log(message: str, level: str = "INFO"):
    """Enhanced logging with visible output."""
    prefix_map = {
        "INFO": "ℹ",
        "SUCCESS": "✓",
        "WARNING": "⚠",
        "ERROR": "✗",
        "DEBUG": "→"
    }
    prefix = prefix_map.get(level, "·")
    print(f"{prefix} {message}", flush=True)
    sys.stdout.flush()


def validate_python_syntax(code: str, description: str = "code") -> bool:
    """Validates that a string contains valid Python syntax."""
    try:
        ast.parse(code)
        return True
    except SyntaxError as e:
        log(f"Invalid Python syntax in {description}: {e}", "ERROR")
        return False
    except Exception as e:
        log(f"Failed to parse {description}: {e}", "ERROR")
        return False


def analyze_assertion_strength(assert_statement: str) -> Tuple[bool, str]:
    """
    Performs analysis of assertion strength.
    Returns: (is_strong, reason_if_weak)
    """
    normalized = assert_statement.strip()
    if not normalized.startswith(('assert', 'pytest.raises', 'with pytest.raises')):
        normalized = f"assert {normalized}"
    
    # Basic patterns that indicate weak assertions
    weak_patterns = {
        r'assert\s+True\s*($|#)': "Always-true assertion",
        r'assert\s+1\s*($|#)': "Always-true constant",
        r'assert\s+1\s*==\s*1': "Trivial equality (1==1)",
        r'assert\s+True\s*==\s*True': "Trivial boolean (True==True)",
        r'pass\s*($|#)': "No-op pass statement",
        r'assert\s+.*\s+or\s+True': "Always true with 'or True'",
    }
    
    for pattern, reason in weak_patterns.items():
        if re.search(pattern, normalized, re.IGNORECASE):
            return False, reason
    
    # Check for meaningful comparisons
    has_comparison = any(op in normalized for op in ['==', '!=', '<', '>', '<=', '>=', 'in', 'not in'])
    
    if not has_comparison and 'pytest.raises' not in normalized:
        # Check if it's at least calling a function or checking a result
        if not re.search(r'\w+\(.*\)', normalized) and not re.search(r'result|output|ret|answer|value', normalized.lower()):
            return False, "No comparison or meaningful check"
    
    return True, "Valid assertion"


def validate_postcondition_structure(post_condition: dict) -> Tuple[bool, str]:
    """
    Validates postcondition structure.
    Returns: (is_valid, reason_if_invalid)
    """
    if not isinstance(post_condition, dict):
        return False, "Not a dictionary"
    
    assert_statement = post_condition.get("assert_statement", "").strip()
    
    if not assert_statement:
        return False, "Empty assert statement"
    
    normalized = assert_statement.strip()
    if not normalized.startswith(('assert', 'pytest.raises', 'with pytest.raises')):
        normalized = f"assert {normalized}"
    
    test_code = f"def test():\n    {normalized}"
    if not validate_python_syntax(test_code, "postcondition"):
        return False, "Invalid syntax"
    
    is_strong, reason = analyze_assertion_strength(assert_statement)
    if not is_strong:
        return False, f"Weak: {reason}"
    
    return True, "Valid"


def validate_precondition_structure(pre_condition: dict) -> bool:
    """Validates precondition structure."""
    if not isinstance(pre_condition, dict):
        log("Precondition is not a dictionary", "ERROR")
        return False
    
    setup_statement = pre_condition.get("setup_statement", "").strip()
    
    if not setup_statement:
        log("Empty setup statement in precondition", "ERROR")
        return False
    
    test_code = f"def test():\n    {setup_statement}"
    return validate_python_syntax(test_code, "precondition")


def run_initial_test_verification(test_file: str) -> Tuple[bool, str]:
    """Runs the test WITHOUT mutation to ensure it passes."""
    log("Running initial test verification (no mutation)...", "DEBUG")
    
    env = os.environ.copy()
    env['PYTHONPATH'] = '.'
    
    command = ['pytest', '-v', test_file]
    result = subprocess.run(command, capture_output=True, text=True, env=env, timeout=30)
    
    if result.returncode != 0:
        error_msg = f"Initial test FAILED.\nSTDOUT:\n{result.stdout[:300]}\nSTDERR:\n{result.stderr[:300]}"
        log(error_msg, "ERROR")
        return False, error_msg
    
    log("Initial test PASSED ✓", "SUCCESS")
    return True, ""


def analyze_mutation_results(score: float, total: int, killed: int, survived: int) -> Tuple[bool, str]:
    """
    Simplified mutation result analysis - accepts any valid result.
    Returns: (is_valid, reason_if_invalid)
    """
    log(f"Analyzing mutation results: {killed}/{total} killed, {survived} survived", "DEBUG")
    
    if score < 0.0 or score > 1.0:
        return False, f"Invalid score: {score:.2f}"
    
    # Accept any number of mutants - no minimum required
    if total == 0:
        return False, "No mutants generated"
    
    expected_score = killed / total if total > 0 else 0.0
    if abs(score - expected_score) > 0.01:
        return False, f"Score mismatch: {expected_score:.2f} vs {score:.2f}"
    
    # Accept any score - no minimum or maximum restrictions
    return True, f"Valid: {killed}/{total} killed ({score:.2f})"


def get_function_name(code_str: str) -> Optional[str]:
    """Extracts function name from code."""
    try:
        tree = ast.parse(code_str)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except Exception as e:
        log(f"Error parsing function name: {e}", "ERROR")
    return None


def get_prompts_to_test():
    """Fetches prompts with postconditions."""
    log("Fetching prompts from database...", "INFO")
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    prompts_list = list(prompts_collection.find({"Post_Conditions": {"$ne": []}}))
    
    log(f"Found {len(prompts_list)} prompts with postconditions", "SUCCESS")
    client.close()
    return prompts_list


def setup_test_environment(func_name: str, module_path: str, path_to_mutate: str, 
                          pre_conditions: List[dict], post_conditions: List[dict]) -> Tuple[bool, str, int, int]:
    """Sets up test environment with simplified validation.
    
    Returns: (success, message, total_postconditions, valid_postconditions)
    """
    
    log("Validating preconditions...", "DEBUG")
    valid_pre_conditions = []
    for idx, pre_con in enumerate(pre_conditions):
        if validate_precondition_structure(pre_con):
            valid_pre_conditions.append(pre_con)
        else:
            log(f"Skipped precondition #{idx + 1}", "WARNING")
    
    if not valid_pre_conditions:
        return False, "No valid preconditions", 0, 0
    
    log("Validating postconditions...", "DEBUG")
    valid_post_conditions = []
    rejection_reasons = []
    total_postconditions = len(post_conditions)
    
    for idx, post_con in enumerate(post_conditions):
        is_valid, reason = validate_postcondition_structure(post_con)
        if is_valid:
            valid_post_conditions.append(post_con)
            log(f"Postcondition #{idx + 1}: ✓ {reason}", "SUCCESS")
        else:
            rejection_reasons.append(f"PC#{idx+1}: {reason}")
            log(f"Postcondition #{idx + 1}: ✗ {reason}", "ERROR")
    
    # Accept even a single valid postcondition
    if not valid_post_conditions:
        return False, f"No valid postconditions. Reasons: {'; '.join(rejection_reasons)}", total_postconditions, 0
    
    valid_count = len(valid_post_conditions)
    log(f"Validated {len(valid_pre_conditions)} PRE + {valid_count} POST conditions", "SUCCESS")
    
    # Create test file
    content = [
        "import pytest",
        "import sys",
        "import os",
        "import math",
        "sys.path.insert(0, os.path.abspath('.'))",
        f"from {module_path} import {func_name}",
        "",
        "def test_llm_generated_postconditions():"
    ]

    all_setup_lines = []
    for pre_con in valid_pre_conditions:
        setup_statement = pre_con.get("setup_statement")
        if setup_statement:
            indented_setup = "\n".join(["    " + line for line in setup_statement.splitlines()])
            all_setup_lines.append(indented_setup)
    
    content.append("\n".join(all_setup_lines))
    content.append("") 

    all_asserts = []
    for post_con in valid_post_conditions:
        assert_statement = post_con.get("assert_statement").strip()
        
        if not assert_statement.startswith(('assert', 'pytest.raises', 'with pytest.raises')):
            assert_statement = f"assert {assert_statement}"
        
        indented_assert = "\n".join(["    " + line for line in assert_statement.splitlines()])
        all_asserts.append(indented_assert)
    
    content.append("\n\n".join(all_asserts))
    
    try:
        with open(TEST_FILE_NAME, "w", encoding="utf-8") as f:
            f.write("\n".join(content))
        log(f"Created test file: {TEST_FILE_NAME}", "SUCCESS")
    except Exception as e:
        return False, f"Error writing test file: {e}", total_postconditions, valid_count

    config_content = f"""
[mutmut]
runner = pytest -x {TEST_FILE_NAME}
paths_to_mutate = {path_to_mutate}
"""
    try:
        with open(CONFIG_FILE_NAME, "w", encoding="utf-8") as f:
            f.write(config_content)
        log(f"Created config file: {CONFIG_FILE_NAME}", "SUCCESS")
    except Exception as e:
        return False, f"Error writing config: {e}", total_postconditions, valid_count
    
    return True, "Success", total_postconditions, valid_count


def run_and_parse_mutmut() -> Tuple[Optional[float], int, int, int, str]:
    """Runs mutmut and parses results."""
    
    log("Starting mutmut mutation testing...", "INFO")
    
    env = os.environ.copy()
    env['PYTHONPATH'] = '.'
    
    command = ['mutmut', 'run']
    
    try:
        run_result = subprocess.run(command, capture_output=True, text=True, env=env, timeout=300)
    except subprocess.TimeoutExpired:
        log("Mutation testing TIMEOUT", "ERROR")
        return None, 0, 0, 0, "Timeout"
    
    run_stdout = run_result.stdout
    
    if run_stdout:
        log(f"Mutmut output preview: {run_stdout[:200]}...", "DEBUG")
    
    if "No such option" in run_result.stderr:
        log("Mutmut command failed", "ERROR")
        return None, 0, 0, 0, "Command failed"

    report_command = ['mutmut', 'results']
    report_result = subprocess.run(report_command, capture_output=True, text=True, env=env)
    report_stdout = report_result.stdout

    total_mutants = 0
    killed = 0
    survived = 0
    
    try:
        survived_match = re.search(r"Survived:\s*(\d+)", report_stdout)
        if survived_match:
            survived = int(survived_match.group(1))

        total_match = re.search(r"Total mutants:\s*(\d+)", report_stdout)
        killed_match = re.search(r"Killed:\s*(\d+)", report_stdout)
        
        if total_match and killed_match:
            total_mutants = int(total_match.group(1))
            killed = int(killed_match.group(1))
        else:
            emoji_matches = re.findall(r"(\d+)/(\d+)\s+🎉", run_stdout)
            if emoji_matches:
                last_match = emoji_matches[-1]
                killed = int(last_match[0])
                total_mutants = int(last_match[1])
            else:
                log("Could not parse mutmut output", "ERROR")
                return None, 0, 0, 0, "Parse error"
            
        if total_mutants == 0:
            log("Mutmut found 0 mutants", "ERROR")
            return None, 0, 0, 0, "0 mutants"
        
        if survived > 0:
            killed = total_mutants - survived
        
        score = killed / total_mutants
        
        log(f"Raw mutation results: {killed}/{total_mutants} killed = {score:.2f}", "INFO")
        
        is_valid, validation_msg = analyze_mutation_results(score, total_mutants, killed, survived)
        if not is_valid:
            log(f"REJECTED: {validation_msg}", "ERROR")
            return None, total_mutants, killed, survived, validation_msg
        
        log(f"ACCEPTED: {validation_msg}", "SUCCESS")
        return score, total_mutants, killed, survived, validation_msg
        
    except Exception as e:
        log(f"Parsing exception: {e}", "ERROR")
        return None, 0, 0, 0, f"Exception: {e}"


def cleanup():
    """Removes temporary files."""
    files_to_remove = [TEST_FILE_NAME, ".mutmut-cache", "mutmut.log", CONFIG_FILE_NAME]
    for file in files_to_remove:
        if os.path.exists(file):
            try:
                os.remove(file)
            except:
                pass


def process_prompt(prompt_doc, functions_collection, prompts_collection, strategy_stats):
    """Handles the full mutation testing workflow for a single prompt.
    
    Args:
        strategy_stats: Dict to track statistics per strategy
    
    Returns:
        Dict with processing results
    """
    
    prompt_id = prompt_doc["Prompt_ID"]
    function_id = prompt_doc.get("Function_ID")
    strategy = prompt_doc.get("Prompt_Strategy", "Unknown")

    print("\n" + "="*70)
    log(f"Processing Prompt ID: {prompt_id} | Function ID: {function_id} | Strategy: {strategy}", "INFO")
    print("="*70)

    result = {
        "prompt_id": prompt_id,
        "strategy": strategy,
        "success": False,
        "score": 0.0,
        "total_postconditions": 0,
        "valid_postconditions": 0,
        "passed_initial_test": False
    }

    if function_id is None:
        log("No Function ID associated. SKIP", "ERROR")
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result

    function_doc = functions_collection.find_one({"Function_ID": function_id})
    if not function_doc:
        log(f"Function ID {function_id} not found in DB. SKIP", "ERROR")
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result

    db_file_path = function_doc.get("file_path")
    function_code = function_doc.get("Function_Code")
    
    if not db_file_path or not function_code:
        log("Missing file_path or function code. SKIP", "ERROR")
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result

    if not validate_python_syntax(function_code, "function code"):
        log("Function has invalid syntax. SKIP", "ERROR")
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result
    
    log(f"Function code validated successfully", "INFO")

    correct_file_path = os.path.join(PY_FILES_DIR, db_file_path)
    correct_module_path = correct_file_path.replace(os.sep, ".").replace(".py", "")
    
    try:
        with open(correct_file_path, "w", encoding="utf-8") as f:
            f.write(function_code)
        log(f"Wrote function to: {correct_file_path}", "SUCCESS")
    except Exception as e:
        log(f"Could not write file: {e}. SKIP", "ERROR")
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result

    func_name = get_function_name(function_code)
    if not func_name:
        log("Could not parse function name. SKIP", "ERROR")
        os.remove(correct_file_path)
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result
    log(f"Function name: {func_name}()", "INFO")
            
    post_conditions = prompt_doc.get("Post_Conditions", [])
    pre_conditions = prompt_doc.get("Pre_Conditions", [])
    
    result["total_postconditions"] = len(post_conditions)
    
    if not post_conditions or not pre_conditions:
        log("Missing conditions. SKIP", "ERROR")
        os.remove(correct_file_path)
        Prompts.updateMutationScore(prompt_id, 0.0)
        return result
    
    score = 0.0
    try:
        setup_success, setup_reason, total_post, valid_post = setup_test_environment(
            func_name, correct_module_path, correct_file_path, 
            pre_conditions, post_conditions
        )
        
        result["total_postconditions"] = total_post
        result["valid_postconditions"] = valid_post
        
        if not setup_success:
            log(f"Setup failed: {setup_reason}", "ERROR")
            Prompts.updateMutationScore(prompt_id, 0.0)
            return result
        
        test_passed, error_msg = run_initial_test_verification(TEST_FILE_NAME)
        result["passed_initial_test"] = test_passed
        
        if not test_passed:
            log("Initial test FAILED - postconditions are INCORRECT", "ERROR")
            Prompts.updateMutationScore(prompt_id, 0.0)
            return result
        
        result_score, total, killed, survived, details = run_and_parse_mutmut()
        
        if result_score is None:
            log(f"Mutation testing FAILED: {details}", "ERROR")
            score = 0.0
        else:
            score = result_score
            result["success"] = True
            log(f"✓✓✓ Mutation score: {score:.2f} ✓✓✓", "SUCCESS")
                
    except Exception as e:
        log(f"Exception during testing: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        score = 0.0
    finally:
        cleanup()
        if os.path.exists(correct_file_path):
            os.remove(correct_file_path)

    result["score"] = score
    Prompts.updateMutationScore(prompt_id, score)
    log(f"Database updated: Prompt {prompt_id} → Score {score:.2f}", "SUCCESS")
    
    return result


def print_strategy_report(strategy_stats):
    """Prints a detailed report of strategy performance."""
    
    print("\n" + "="*80)
    print("📊 STRATEGY PERFORMANCE REPORT 📊")
    print("="*80)
    
    # Sort strategies by success count
    sorted_strategies = sorted(strategy_stats.items(), 
                              key=lambda x: x[1]['success_count'], 
                              reverse=True)
    
    for strategy, stats in sorted_strategies:
        total = stats['total']
        success = stats['success_count']
        total_post = stats['total_postconditions']
        valid_post = stats['valid_postconditions']
        passed_initial = stats['passed_initial_test']
        avg_score = stats['total_score'] / success if success > 0 else 0.0
        
        success_rate = (success / total * 100) if total > 0 else 0.0
        validation_rate = (valid_post / total_post * 100) if total_post > 0 else 0.0
        initial_pass_rate = (passed_initial / total * 100) if total > 0 else 0.0
        
        print(f"\n{'─'*80}")
        print(f"Strategy: {strategy}")
        print(f"{'─'*80}")
        print(f"  Total Prompts:              {total:>6}")
        print(f"  ✓ Successful (score > 0):   {success:>6}  ({success_rate:>5.1f}%)")
        print(f"  ✗ Failed (score = 0):       {total - success:>6}  ({100-success_rate:>5.1f}%)")
        print(f"")
        print(f"  Postconditions Generated:   {total_post:>6}")
        print(f"  Postconditions Valid:       {valid_post:>6}  ({validation_rate:>5.1f}%)")
        print(f"  Passed Initial Test:        {passed_initial:>6}  ({initial_pass_rate:>5.1f}%)")
        print(f"")
        print(f"  Average Mutation Score:     {avg_score:>6.3f}")
        
        if success > 0:
            efficiency = (avg_score * success_rate) / 100
            print(f"  Overall Efficiency:         {efficiency:>6.3f}  (avg_score × success_rate)")
    
    print("\n" + "="*80)


def main():
    """Main orchestrator for batch mutation testing."""
    
    print("\n" + "="*70)
    print("🔬 ENHANCED MUTATION TESTING WITH STRATEGY TRACKING 🔬")
    print("="*70 + "\n")

    if not os.path.exists(PY_FILES_DIR):
        os.makedirs(PY_FILES_DIR)
        log(f"Created directory: {PY_FILES_DIR}", "SUCCESS")

    init_path = os.path.join(PY_FILES_DIR, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w") as f:
            pass
        log(f"Created __init__.py", "SUCCESS")
            
    prompts_to_test = get_prompts_to_test()
    
    if not prompts_to_test:
        log("No prompts found with postconditions. EXIT", "WARNING")
        return

    client, db = get_db_client()
    functions_collection = db["Functions"]
    prompts_collection = db["FunctionPrompts"]
    
    # Strategy tracking
    strategy_stats = defaultdict(lambda: {
        'total': 0,
        'success_count': 0,
        'total_postconditions': 0,
        'valid_postconditions': 0,
        'passed_initial_test': 0,
        'total_score': 0.0
    })
    
    success_count = 0
    failure_count = 0
    
    for idx, prompt_doc in enumerate(prompts_to_test, 1):
        print(f"\n{'='*70}")
        log(f"BATCH PROGRESS: [{idx}/{len(prompts_to_test)}]", "INFO")
        print('='*70)
        
        try:
            result = process_prompt(prompt_doc, functions_collection, prompts_collection, strategy_stats)
            
            strategy = result["strategy"]
            strategy_stats[strategy]['total'] += 1
            strategy_stats[strategy]['total_postconditions'] += result['total_postconditions']
            strategy_stats[strategy]['valid_postconditions'] += result['valid_postconditions']
            
            if result['passed_initial_test']:
                strategy_stats[strategy]['passed_initial_test'] += 1
            
            if result['success']:
                success_count += 1
                strategy_stats[strategy]['success_count'] += 1
                strategy_stats[strategy]['total_score'] += result['score']
                log(f"RESULT: SUCCESS (score={result['score']:.2f})", "SUCCESS")
            else:
                failure_count += 1
                log(f"RESULT: FAILED (score=0.0)", "ERROR")
                    
        except Exception as e:
            log(f"Fatal error: {e}", "ERROR")
            import traceback
            traceback.print_exc()
            failure_count += 1
            
    client.close()
    
    # Print overall summary
    print("\n" + "="*70)
    print("📊 OVERALL RESULTS 📊")
    print("="*70)
    log(f"✓ Successful (score > 0):      {success_count:>4}", "SUCCESS")
    log(f"✗ Failed (score = 0):          {failure_count:>4}", "ERROR")
    log(f"  Total Processed:             {len(prompts_to_test):>4}", "INFO")
    if len(prompts_to_test) > 0:
        success_rate = (success_count/len(prompts_to_test)*100)
        log(f"  Success Rate:                {success_rate:>3.1f}%", "INFO")
    print("="*70 + "\n")
    
    # Print strategy report
    print_strategy_report(strategy_stats)


if __name__ == "__main__":
    main()