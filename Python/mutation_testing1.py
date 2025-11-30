import json
import ast
import os
import sys
import re
import random
import string
import math
import collections
import cmath
import functools
from typing import Dict, List, Any, Tuple, Union, Optional


# Add current directory to path to ensure config import works
sys.path.append(os.getcwd())

try:
    import json_repair
    print("Success: 'json_repair' module found. Hallucination analysis will be robust.")
except ImportError:
    json_repair = None
    print("Warning: 'json_repair' not installed. Run 'pip install json_repair' for best results.")

try:
    from config import get_db_client
except ImportError:
    print("Error: config.py not found. Please ensure it exists in the same directory.")
    sys.exit(1)

# ==============================================================================
# 1. MOCK FUNCTION LIBRARY (From Framework)
# ==============================================================================
# These functions allow the execution_statement to run successfully.

def similar_elements(t1, t2):
    return tuple(sorted(list(set(t1) & set(t2))))

def is_not_prime(n):
    if not isinstance(n, int): raise TypeError("Input must be integer")
    if n < 2: return True 
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return True
    return False

def heap_queue_largest(nums, n):
    if not isinstance(nums, list) or not isinstance(n, int): raise TypeError("Invalid types")
    if n > len(nums): return sorted(nums, reverse=True)
    return sorted(nums, reverse=True)[:n]

def differ_At_One_Bit_Pos(a, b):
    if not isinstance(a, int) or not isinstance(b, int): raise TypeError("Inputs must be ints")
    return bin(a ^ b).count('1') == 1

def find_char_long(text):
    if not isinstance(text, str): raise AttributeError("Input must be string")
    return [w for w in text.split() if len(w) >= 4]

def square_nums(nums):
    if not isinstance(nums, list): raise TypeError("Input must be list")
    return [x**2 for x in nums]

def find_Rotations(s):
    if not isinstance(s, str): raise TypeError("Input must be string")
    if not s: return 0
    if len(set(s)) == 1: return 1
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0 and s[:i] * (n // i) == s:
            return i
    return n

def remove_Occ(s, ch):
    if not isinstance(s, str) or not isinstance(ch, str): raise TypeError("Inputs must be strings")
    if s.count(ch) < 2: return s.replace(ch, "") 
    first = s.find(ch)
    last = s.rfind(ch)
    if first == last: return s.replace(ch, "")
    s_list = list(s)
    if last != -1: s_list.pop(last)
    if first != -1: s_list.pop(first)
    return "".join(s_list)

def sort_matrix(M):
    if not isinstance(M, list): raise TypeError("Input must be list")
    return sorted(M, key=sum)

def find_Volume(l, b, h):
    if any(x is None for x in [l,b,h]): raise TypeError("None not allowed")
    if any(not isinstance(x, (int, float)) for x in [l,b,h]): raise TypeError("Must be number")
    return (l * b * h) / 2.0

def text_lowercase_underscore(text):
    if not isinstance(text, str): raise AttributeError("Must be string")
    return bool(re.match(r'^[a-z]+_[a-z]+$', text))

def square_perimeter(a):
    if a is None: raise TypeError("None not allowed")
    if not isinstance(a, (int, float)): raise TypeError("Must be number")
    if a < 0: raise ValueError("Negative side")
    return 4 * a

def remove_dirty_chars(s, second_s):
    return "".join([c for c in s if c not in second_s])

def test_duplicate(nums):
    if not isinstance(nums, list): raise TypeError("Must be list")
    return len(nums) != len(set(nums))

def is_woodall(x):
    if not isinstance(x, int): raise TypeError("Must be int")
    return x in [1, 7, 23, 63, 159, 383, 895]

def check(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    s = str(n)
    try:
        rev_n = int(s[::-1])
        return 2 * rev_n == n + 1
    except:
        return False

def find_Max_Num(arr):
    if not isinstance(arr, list): raise TypeError("Must be list")
    if not arr: return 0
    s_arr = list(map(str, arr))
    # Simple concatenation sort for max number approximation
    s_arr.sort(key=lambda x: x*10, reverse=True)
    return int("".join(s_arr)) if s_arr and s_arr[0] != '0' else 0

def opposite_Signs(x, y):
    if not isinstance(x, int) or not isinstance(y, int): raise TypeError("Must be int")
    return (x ^ y) < 0

def is_octagonal(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    return 3 * n * n - 2 * n

def count_Substrings(s):
    if not isinstance(s, str): raise TypeError("Must be str")
    return len(s) # Simplified placeholder

def smallest_num(xs):
    if xs is None: raise TypeError("None not allowed")
    if not isinstance(xs, list): raise TypeError("Must be list")
    if not xs: raise ValueError("Empty list")
    if any(not isinstance(x, (int, float)) for x in xs): raise TypeError("Must be numbers")
    return min(xs)

def max_difference(lst):
    if not isinstance(lst, list): raise TypeError("Must be list")
    if not lst: raise ValueError("Empty list")
    if not all(isinstance(x, tuple) and len(x) >= 2 for x in lst): raise TypeError("Elements must be tuples")
    return max(abs(a-b) for a, b, *rest in lst)

def subject_marks(subjectmarks):
    if not isinstance(subjectmarks, list): raise TypeError("Must be list")
    return sorted(subjectmarks, key=lambda x: x[1])

def recursive_list_sum(data_list):
    if not isinstance(data_list, list): raise TypeError("Must be list")
    total = 0
    for element in data_list:
        if isinstance(element, list):
            total = total + recursive_list_sum(element)
        elif isinstance(element, (int, float)):
            total = total + element
    return total

def pos_count(nums):
    if not isinstance(nums, list): raise TypeError("Must be list")
    return sum(1 for x in nums if isinstance(x, (int, float)) and x >= 0)

def bell_number(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    if n < 0: raise IndexError("Negative n")
    vals = [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213597, 27644423, 190899322]
    if n < len(vals): return vals[n]
    return 0

def is_Monotonic(A):
    if not isinstance(A, list): raise TypeError("Must be list")
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

def is_sublist(l, s):
    if not isinstance(l, list) or not isinstance(s, list): raise TypeError("Must be list")
    if not s: return True
    sub_len = len(s)
    for i in range(len(l) - sub_len + 1):
        if l[i:i+sub_len] == s:
            return True
    return False

def get_equal(l):
    if not isinstance(l, list): raise TypeError("Must be list")
    if not l: return True
    first_len = len(l[0])
    return all(len(x) == first_len for x in l)

def comb_sort(nums):
    if not isinstance(nums, list): raise TypeError("Must be list")
    return sorted(nums, reverse=True)

def dif_Square(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    return n % 4 != 2

def is_samepatterns(colors, patterns):
    if not isinstance(colors, list) or not isinstance(patterns, list): raise TypeError("Must be lists")
    if len(colors) != len(patterns): return False
    if len(set(colors)) != len(set(patterns)): return False
    return True

def find_tuples(test_list, K):
    if not isinstance(test_list, list): raise TypeError("Must be list")
    if K == 0: raise ZeroDivisionError("K cannot be 0")
    return [t for t in test_list if all(isinstance(x, int) and x % K == 0 for x in t)]

def is_Diff(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    return n % 11 == 0

def word_len(s):
    if not isinstance(s, str): raise AttributeError("Must be str")
    return any(len(w) % 2 != 0 for w in s.split())

def tetrahedral_number(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    return int((n * (n + 1) * (n + 2)) / 6)

def volume_sphere(r):
    if r is None: raise TypeError("None")
    if not isinstance(r, (int, float)): raise TypeError("Must be number")
    return (4/3) * math.pi * (r ** 3)

def get_Char(s):
    if not isinstance(s, str): raise TypeError("Must be str")
    if not s: return 'z'
    val = sum(ord(c.lower()) - ord('a') + 1 for c in s if c.isalpha())
    rem = val % 26
    if rem == 0: return 'z'
    return chr(ord('a') + rem - 1)

def sequence(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    if n <= 2: return 1
    if n == 3: return 2
    cache = {1:1, 2:1}
    def _seq(x):
        if x in cache: return cache[x]
        if x <= 2: return 1
        # Simple recursion limit protection
        if x > 100: return 1
        try:
            res = _seq(_seq(x-1)) + _seq(x - _seq(x-1))
            cache[x] = res
            return res
        except: return 1
    return _seq(n)

def surfacearea_sphere(r):
    if r is None: raise TypeError("None")
    if not isinstance(r, (int, float)): raise TypeError("Must be number")
    return 4 * math.pi * (r ** 2)

def centered_hexagonal_number(n):
    if not isinstance(n, int): raise TypeError("Must be int")
    if n < 0: raise ValueError("Negative n")
    if n == 0: return 1
    return 3 * n * (n - 1) + 1

def merge_dictionaries_three(d1, d2, d3):
    if any(not isinstance(d, dict) for d in [d1, d2, d3]): raise TypeError("Must be dict")
    z = d1.copy()
    z.update(d2)
    z.update(d3)
    return z

def freq_count(l):
    if not isinstance(l, list): raise TypeError("Must be list")
    try:
        return dict(collections.Counter(l))
    except TypeError:
        raise TypeError("Unhashable")

def tuple_to_int(t):
    if not isinstance(t, tuple): raise TypeError("Must be tuple")
    if any(not isinstance(x, int) for x in t): raise ValueError("Elements must be ints")
    return int("".join(map(str, t)))

def list_to_float(l):
    if not isinstance(l, list): raise TypeError("Must be list")
    res = []
    for sub in l:
        if not isinstance(sub, (list, tuple)): raise TypeError("Inner must be list/tuple")
        res.append(tuple(float(x) if str(x).replace('.','',1).isdigit() else x for x in sub))
    return res

def string_to_list(s):
    if not isinstance(s, str): raise AttributeError("Must be string")
    return s.split(' ')

def search(arr):
    if not isinstance(arr, list): raise TypeError("Must be list")
    c = collections.Counter(arr)
    for k, v in c.items():
        if v == 1: return k
    return 0

def max_product_tuple(lst):
    if not isinstance(lst, list): raise TypeError("Must be list")
    if not lst: return 0
    return max(abs(x*y) for x,y in lst) 

def amicable_numbers_sum(limit):
    if not isinstance(limit, int): return "Input is not an integer!"
    if limit <= 0: return "Input must be bigger than 0!"
    return 0 # Simplified mock

def angle_complex(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): raise TypeError("Must be numbers")
    return cmath.phase(complex(a, b))

def find_length(s):
    if not isinstance(s, str): raise TypeError("Must be str")
    if '0' not in s and '1' in s: return 0
    if '1' not in s and '0' in s: return len(s)
    return 0

def multiply_int(x, y):
    if not isinstance(x, int) or not isinstance(y, int): raise TypeError("Must be int")
    return x * y

def long_words(n, s):
    if not isinstance(n, int): raise TypeError("n must be int")
    if not isinstance(s, str): raise AttributeError("s must be str")
    return [w for w in s.split() if len(w) > n]

def magic_square_test(m):
    if not isinstance(m, list): raise TypeError("Must be list")
    if not m: return False
    n = len(m)
    if any(len(row) != n for row in m): return False
    return True

def max_occurrences(nums):
    if not isinstance(nums, list): raise TypeError("Must be list")
    if not nums: raise ValueError("Empty")
    return max(set(nums), key=nums.count)

def index_minimum(test_list):
    if not isinstance(test_list, list): raise TypeError("Must be list")
    if not test_list: raise ValueError("Empty list")
    return min(test_list, key=lambda x: x[1])[0]

def Find_Min_Length(lst):
    if not isinstance(lst, list): raise TypeError("Must be list")
    if not lst: return 0
    return min(len(x) for x in lst)


# Collection name in MongoDB
COLLECTION_NAME = "FunctionPrompts"

def clean_json_string(json_str):
    """
    Cleans a string to extract valid JSON. 
    Handles Markdown code blocks (```json ... ```) commonly output by LLMs.
    """
    if not isinstance(json_str, str):
        return json_str
    
    if json_repair:
        try:
            # If successful, json_repair.loads returns a python object (dict/list)
            return json_repair.loads(json_str)
        except Exception:
            pass
        
    markdown_pattern = r"```(?:json)?\s*([\s\S]*?)\s*```"
    match = re.search(markdown_pattern, json_str, re.IGNORECASE)
    cleaned_str = match.group(1).strip() if match else json_str.strip()
    cleaned_str = re.sub(r'\\(?![/u"\\bfnrt])', r'\\\\', cleaned_str)
    try:
        return json.loads(cleaned_str)
    except json.JSONDecodeError:
        return {}

class InputGenerator:
    @staticmethod
    def get_int(constraints):
        min_val = constraints.get('min_val', -100)
        max_val = constraints.get('max_val', 100)
        val = constraints.get('value')
        if val is not None: return val
        if min_val > max_val: min_val, max_val = max_val, min_val
        return random.randint(min_val, max_val)

    @staticmethod
    def get_float(constraints):
        min_val = constraints.get('min_val', -100.0)
        max_val = constraints.get('max_val', 100.0)
        if min_val > max_val: min_val, max_val = max_val, min_val
        return random.uniform(min_val, max_val)

    @staticmethod
    def get_str(constraints):
        val = constraints.get('value')
        if val is not None: return val
        min_len = constraints.get('min_len', 1)
        max_len = constraints.get('max_len', 10)
        pattern = constraints.get('pattern')
        if pattern:
            if '01' in pattern: return "".join(random.choice('01') for _ in range(random.randint(min_len, max_len)))
            if 'a-z' in pattern: return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(min_len, max_len)))
        length = random.randint(min_len, max_len)
        return "".join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def get_list(type_str, constraints):
        min_len = constraints.get('min_len', 1)
        max_len = constraints.get('max_len', 5)
        size = random.randint(min_len, max_len)
        subtype = "int"
        if "str" in type_str: subtype = "str"
        elif "float" in type_str: subtype = "float"
        elif "tuple" in type_str: subtype = "tuple"
        elif "list" in type_str: subtype = "list"
        elif "bool" in type_str: subtype = "bool"
        
        elem_constraints = constraints.get('elements', {})
        if isinstance(elem_constraints, list) and len(elem_constraints) > 0: elem_constraints = elem_constraints[0]
        if not isinstance(elem_constraints, dict): elem_constraints = {}
        
        if 'min_val' in constraints and subtype == 'int': elem_constraints['min_val'] = constraints['min_val']
        if 'max_val' in constraints and subtype == 'int': elem_constraints['max_val'] = constraints['max_val']

        if subtype == "int": return [InputGenerator.get_int(elem_constraints) for _ in range(size)]
        elif subtype == "str": return [InputGenerator.get_str(elem_constraints) for _ in range(size)]
        elif subtype == "float": return [InputGenerator.get_float(elem_constraints) for _ in range(size)]
        elif subtype == "tuple": return [(random.randint(1,10), random.randint(1,10)) for _ in range(size)]
        elif subtype == "list": return [[random.randint(1,10)] for _ in range(size)]
        elif subtype == "bool": return [random.choice([True, False]) for _ in range(size)]
        return []

    @staticmethod
    def generate(type_str, constraints):
        if not constraints: constraints = {}
        if "list" in type_str or "List" in type_str: return InputGenerator.get_list(type_str, constraints)
        elif "tuple" in type_str or "Tuple" in type_str: return tuple(InputGenerator.get_list(type_str, constraints))
        elif "int" in type_str: return InputGenerator.get_int(constraints)
        elif "float" in type_str: return InputGenerator.get_float(constraints)
        elif "str" in type_str: return InputGenerator.get_str(constraints)
        elif "dict" in type_str: return {"a": 1, "b": 2}
        elif "bool" in type_str:
            val = constraints.get('value')
            return val if val is not None else random.choice([True, False])
        elif "None" in type_str: return None
        else: return None

class MutationEngine:
    def __init__(self):
        self.replacements = [
            ('==', '!=', "Equality Negation"), ('!=', '==', "Inequality Negation"),
            ('<=', '>', "Boundary Change"), ('>=', '<', "Boundary Change"),
            ('<', '>=', "Boundary Change"), ('>', '<=', "Boundary Change"),
            (' and ', ' or ', "Logical Operator Change"), (' or ', ' and ', "Logical Operator Change"),
            ('+', '-', "Arithmetic Operator Change"), ('-', '+', "Arithmetic Operator Change"),
            ('*', '/', "Arithmetic Operator Change"), ('/', '*', "Arithmetic Operator Change"),
            ('True', 'False', "Boolean Negation"), ('False', 'True', "Boolean Negation")
        ]

    def generate_mutants(self, assertion_str):
        mutants = []
        for old, new, type_ in self.replacements:
            if old in assertion_str:
                start = 0
                while True:
                    idx = assertion_str.find(old, start)
                    if idx == -1: break
                    mutant_code = assertion_str[:idx] + new + assertion_str[idx+len(old):]
                    mutants.append({'code': mutant_code, 'type': type_})
                    start = idx + 1
        return mutants

# ==============================================================================
# 3. MAIN LOGIC
# ==============================================================================

def calculate_mutation_score(doc: Dict[str, Any]) -> Tuple[float, int]:
    raw_response = doc.get('test_cases')
    if not raw_response and 'Structured_Response' in doc:
         raw_response = doc['Structured_Response']

    if not raw_response: return 0.0, 0
    
    test_cases = []
    if isinstance(raw_response, str):
         parsed = clean_json_string(raw_response)
         if isinstance(parsed, dict) and 'test_cases' in parsed:
             test_cases = parsed['test_cases']
         elif isinstance(parsed, list):
             test_cases = parsed
    elif isinstance(raw_response, list):
        test_cases = raw_response
    elif isinstance(raw_response, dict) and 'test_cases' in raw_response:
        test_cases = raw_response['test_cases']
    
    if not test_cases: return 0.0, 0
    
    engine = MutationEngine()
    context = globals().copy()
    
    test_case_scores = [] # Store individual scores (0.0 to 1.0) per test case
    
    total_mutants_global = 0 # To track if we did any work at all
    
    for tc in test_cases:
        local_vars = context.copy()
        inputs = tc.get('input_types', {})
        constraints = tc.get('input_constraints', {})
        
        try:
            for var_name, var_type in inputs.items():
                var_const = constraints.get(var_name, {})
                generated_val = InputGenerator.generate(var_type, var_const)
                local_vars[var_name] = generated_val
        except Exception:
            continue

        exec_stmt = tc.get('execution_statement')
        try:
            exec(exec_stmt, {}, local_vars)
        except Exception:
            continue
            
        postconditions = tc.get('postconditions', [])
        
        killed_in_tc = 0
        total_in_tc = 0
        
        for pc in postconditions:
            assertion = pc.get('assertion')
            if not assertion: continue
            
            try:
                if not eval(assertion, {}, local_vars): continue
            except Exception: continue

            mutants = engine.generate_mutants(assertion)
            for m in mutants:
                total_in_tc += 1
                total_mutants_global += 1
                try:
                    if not eval(m['code'], {}, local_vars):
                        killed_in_tc += 1
                except Exception:
                    killed_in_tc += 1
        
        if total_in_tc > 0:
            test_case_scores.append(killed_in_tc / total_in_tc)
        else:
            # If a test case had no valid mutants generated or assertions failed initially, 
            # we might choose to ignore it or count it as 0. 
            # Here we ignore it to avoid skewing the average with "empty" tests.
            pass
            
    if not test_case_scores:
        return 0.0, total_mutants_global
        
    # Calculate the average of the individual test case scores
    final_average_score = sum(test_case_scores) / len(test_case_scores)
    
    return final_average_score, total_mutants_global

def process_database():
    print("Initializing Database Connection via config...")
    try:
        client, db = get_db_client()
    except Exception as e:
        print(f"Failed to connect to DB: {e}")
        return

    collection = db[COLLECTION_NAME]
    cursor = collection.find({})
    total_docs = collection.count_documents({})
    
    print(f"Found {total_docs} documents in '{COLLECTION_NAME}'. Starting mutation analysis...")

    updates_count = 0
    errors_count = 0

    for doc in cursor:
        prompt_id = doc.get('Prompt_ID')
        try:
            mutation_score, total_mutants = calculate_mutation_score(doc)
            if total_mutants > 0:
                collection.update_one(
                    {'_id': doc['_id']}, 
                    {'$set': {'Mutation_Score': float(mutation_score)}}
                )
                updates_count += 1
                print(f"[Prompt {prompt_id}] Updated Mutation Score: {mutation_score:.2f} (Total Mutants Processed: {total_mutants})")
        except Exception as e:
            print(f"[Prompt {prompt_id}] Error: {e}")
            errors_count += 1
            continue

    print(f"\nAnalysis complete. Updated: {updates_count}, Errors: {errors_count}")

if __name__ == "__main__":
    process_database()