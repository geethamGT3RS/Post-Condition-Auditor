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
def x_count_char_position__mutmut_orig(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_1(str1): 
    count_chars = None
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_2(str1): 
    count_chars = 1
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_3(str1): 
    count_chars = 0
    for i in range(None):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_4(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) and (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_5(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i != ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_6(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) + ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_7(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(None) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_8(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord(None)) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_9(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('XXAXX')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_10(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('a')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_11(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i != ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_12(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) + ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_13(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(None) - ord('a'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_14(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord(None))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_15(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('XXaXX'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_16(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('A'))): 
            count_chars += 1
    return count_chars 
def x_count_char_position__mutmut_17(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars = 1
    return count_chars 
def x_count_char_position__mutmut_18(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars -= 1
    return count_chars 
def x_count_char_position__mutmut_19(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 2
    return count_chars 

x_count_char_position__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_char_position__mutmut_1': x_count_char_position__mutmut_1, 
    'x_count_char_position__mutmut_2': x_count_char_position__mutmut_2, 
    'x_count_char_position__mutmut_3': x_count_char_position__mutmut_3, 
    'x_count_char_position__mutmut_4': x_count_char_position__mutmut_4, 
    'x_count_char_position__mutmut_5': x_count_char_position__mutmut_5, 
    'x_count_char_position__mutmut_6': x_count_char_position__mutmut_6, 
    'x_count_char_position__mutmut_7': x_count_char_position__mutmut_7, 
    'x_count_char_position__mutmut_8': x_count_char_position__mutmut_8, 
    'x_count_char_position__mutmut_9': x_count_char_position__mutmut_9, 
    'x_count_char_position__mutmut_10': x_count_char_position__mutmut_10, 
    'x_count_char_position__mutmut_11': x_count_char_position__mutmut_11, 
    'x_count_char_position__mutmut_12': x_count_char_position__mutmut_12, 
    'x_count_char_position__mutmut_13': x_count_char_position__mutmut_13, 
    'x_count_char_position__mutmut_14': x_count_char_position__mutmut_14, 
    'x_count_char_position__mutmut_15': x_count_char_position__mutmut_15, 
    'x_count_char_position__mutmut_16': x_count_char_position__mutmut_16, 
    'x_count_char_position__mutmut_17': x_count_char_position__mutmut_17, 
    'x_count_char_position__mutmut_18': x_count_char_position__mutmut_18, 
    'x_count_char_position__mutmut_19': x_count_char_position__mutmut_19
}

def count_char_position(*args, **kwargs):
    result = _mutmut_trampoline(x_count_char_position__mutmut_orig, x_count_char_position__mutmut_mutants, args, kwargs)
    return result 

count_char_position.__signature__ = _mutmut_signature(x_count_char_position__mutmut_orig)
x_count_char_position__mutmut_orig.__name__ = 'x_count_char_position'