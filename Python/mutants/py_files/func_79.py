from collections import defaultdict
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
def x_max_occurrences__mutmut_orig(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_1(nums):
    dict = None
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_2(nums):
    dict = defaultdict(None)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_3(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] = 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_4(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] -= 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_5(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 2
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_6(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = None 
    return result[0]
def x_max_occurrences__mutmut_7(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(None, key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_8(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=None) 
    return result[0]
def x_max_occurrences__mutmut_9(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(key=lambda x: x[1]) 
    return result[0]
def x_max_occurrences__mutmut_10(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), ) 
    return result[0]
def x_max_occurrences__mutmut_11(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: None) 
    return result[0]
def x_max_occurrences__mutmut_12(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[2]) 
    return result[0]
def x_max_occurrences__mutmut_13(nums):
    dict = defaultdict(int)
    for i in nums:
        dict[i] += 1
    result = max(dict.items(), key=lambda x: x[1]) 
    return result[1]

x_max_occurrences__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_occurrences__mutmut_1': x_max_occurrences__mutmut_1, 
    'x_max_occurrences__mutmut_2': x_max_occurrences__mutmut_2, 
    'x_max_occurrences__mutmut_3': x_max_occurrences__mutmut_3, 
    'x_max_occurrences__mutmut_4': x_max_occurrences__mutmut_4, 
    'x_max_occurrences__mutmut_5': x_max_occurrences__mutmut_5, 
    'x_max_occurrences__mutmut_6': x_max_occurrences__mutmut_6, 
    'x_max_occurrences__mutmut_7': x_max_occurrences__mutmut_7, 
    'x_max_occurrences__mutmut_8': x_max_occurrences__mutmut_8, 
    'x_max_occurrences__mutmut_9': x_max_occurrences__mutmut_9, 
    'x_max_occurrences__mutmut_10': x_max_occurrences__mutmut_10, 
    'x_max_occurrences__mutmut_11': x_max_occurrences__mutmut_11, 
    'x_max_occurrences__mutmut_12': x_max_occurrences__mutmut_12, 
    'x_max_occurrences__mutmut_13': x_max_occurrences__mutmut_13
}

def max_occurrences(*args, **kwargs):
    result = _mutmut_trampoline(x_max_occurrences__mutmut_orig, x_max_occurrences__mutmut_mutants, args, kwargs)
    return result 

max_occurrences.__signature__ = _mutmut_signature(x_max_occurrences__mutmut_orig)
x_max_occurrences__mutmut_orig.__name__ = 'x_max_occurrences'