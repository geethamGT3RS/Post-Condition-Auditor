from collections import deque
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
def x_check_expression__mutmut_orig(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_1(exp):
    if len(exp) | 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_2(exp):
    if len(exp) & 2:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_3(exp):
    if len(exp) & 1:
        return True
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_4(exp):
    if len(exp) & 1:
        return False
    stack = None
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_5(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' and ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_6(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' and ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_7(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch != '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_8(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == 'XX(XX' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_9(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch != '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_10(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == 'XX{XX' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_11(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch != '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_12(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == 'XX[XX':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_13(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(None)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_14(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' and ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_15(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' and ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_16(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch != ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_17(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == 'XX)XX' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_18(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch != '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_19(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == 'XX}XX' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_20(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch != ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_21(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == 'XX]XX':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_22(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_23(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return True
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_24(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = None
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_25(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') and (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_26(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' or ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_27(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top != '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_28(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == 'XX(XX' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_29(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch == ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_30(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != 'XX)XX') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_31(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' and (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_32(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' or ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_33(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top != '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_34(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == 'XX{XX' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_35(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch == '}' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_36(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != 'XX}XX' or (top == '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_37(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' or ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_38(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top != '[' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_39(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == 'XX[XX' and ch != ']')):
                return False
    return not stack
def x_check_expression__mutmut_40(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch == ']')):
                return False
    return not stack
def x_check_expression__mutmut_41(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != 'XX]XX')):
                return False
    return not stack
def x_check_expression__mutmut_42(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return True
    return not stack
def x_check_expression__mutmut_43(exp):
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and ch != ')') or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                return False
    return stack

x_check_expression__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_expression__mutmut_1': x_check_expression__mutmut_1, 
    'x_check_expression__mutmut_2': x_check_expression__mutmut_2, 
    'x_check_expression__mutmut_3': x_check_expression__mutmut_3, 
    'x_check_expression__mutmut_4': x_check_expression__mutmut_4, 
    'x_check_expression__mutmut_5': x_check_expression__mutmut_5, 
    'x_check_expression__mutmut_6': x_check_expression__mutmut_6, 
    'x_check_expression__mutmut_7': x_check_expression__mutmut_7, 
    'x_check_expression__mutmut_8': x_check_expression__mutmut_8, 
    'x_check_expression__mutmut_9': x_check_expression__mutmut_9, 
    'x_check_expression__mutmut_10': x_check_expression__mutmut_10, 
    'x_check_expression__mutmut_11': x_check_expression__mutmut_11, 
    'x_check_expression__mutmut_12': x_check_expression__mutmut_12, 
    'x_check_expression__mutmut_13': x_check_expression__mutmut_13, 
    'x_check_expression__mutmut_14': x_check_expression__mutmut_14, 
    'x_check_expression__mutmut_15': x_check_expression__mutmut_15, 
    'x_check_expression__mutmut_16': x_check_expression__mutmut_16, 
    'x_check_expression__mutmut_17': x_check_expression__mutmut_17, 
    'x_check_expression__mutmut_18': x_check_expression__mutmut_18, 
    'x_check_expression__mutmut_19': x_check_expression__mutmut_19, 
    'x_check_expression__mutmut_20': x_check_expression__mutmut_20, 
    'x_check_expression__mutmut_21': x_check_expression__mutmut_21, 
    'x_check_expression__mutmut_22': x_check_expression__mutmut_22, 
    'x_check_expression__mutmut_23': x_check_expression__mutmut_23, 
    'x_check_expression__mutmut_24': x_check_expression__mutmut_24, 
    'x_check_expression__mutmut_25': x_check_expression__mutmut_25, 
    'x_check_expression__mutmut_26': x_check_expression__mutmut_26, 
    'x_check_expression__mutmut_27': x_check_expression__mutmut_27, 
    'x_check_expression__mutmut_28': x_check_expression__mutmut_28, 
    'x_check_expression__mutmut_29': x_check_expression__mutmut_29, 
    'x_check_expression__mutmut_30': x_check_expression__mutmut_30, 
    'x_check_expression__mutmut_31': x_check_expression__mutmut_31, 
    'x_check_expression__mutmut_32': x_check_expression__mutmut_32, 
    'x_check_expression__mutmut_33': x_check_expression__mutmut_33, 
    'x_check_expression__mutmut_34': x_check_expression__mutmut_34, 
    'x_check_expression__mutmut_35': x_check_expression__mutmut_35, 
    'x_check_expression__mutmut_36': x_check_expression__mutmut_36, 
    'x_check_expression__mutmut_37': x_check_expression__mutmut_37, 
    'x_check_expression__mutmut_38': x_check_expression__mutmut_38, 
    'x_check_expression__mutmut_39': x_check_expression__mutmut_39, 
    'x_check_expression__mutmut_40': x_check_expression__mutmut_40, 
    'x_check_expression__mutmut_41': x_check_expression__mutmut_41, 
    'x_check_expression__mutmut_42': x_check_expression__mutmut_42, 
    'x_check_expression__mutmut_43': x_check_expression__mutmut_43
}

def check_expression(*args, **kwargs):
    result = _mutmut_trampoline(x_check_expression__mutmut_orig, x_check_expression__mutmut_mutants, args, kwargs)
    return result 

check_expression.__signature__ = _mutmut_signature(x_check_expression__mutmut_orig)
x_check_expression__mutmut_orig.__name__ = 'x_check_expression'