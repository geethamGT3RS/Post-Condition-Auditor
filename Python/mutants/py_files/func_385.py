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
def x_find_min_diff__mutmut_orig(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_1(arr,n): 
    arr = None 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_2(arr,n): 
    arr = sorted(None) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_3(arr,n): 
    arr = sorted(arr) 
    diff = None 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_4(arr,n): 
    arr = sorted(arr) 
    diff = 10 * 20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_5(arr,n): 
    arr = sorted(arr) 
    diff = 11**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_6(arr,n): 
    arr = sorted(arr) 
    diff = 10**21 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_7(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(None): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_8(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n + 1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_9(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-2): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_10(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] + arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_11(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i - 1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_12(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+2] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_13(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] <= diff: 
            diff = arr[i+1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_14(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = None  
    return diff 
def x_find_min_diff__mutmut_15(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] + arr[i]  
    return diff 
def x_find_min_diff__mutmut_16(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i - 1] - arr[i]  
    return diff 
def x_find_min_diff__mutmut_17(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+2] - arr[i]  
    return diff 

x_find_min_diff__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_min_diff__mutmut_1': x_find_min_diff__mutmut_1, 
    'x_find_min_diff__mutmut_2': x_find_min_diff__mutmut_2, 
    'x_find_min_diff__mutmut_3': x_find_min_diff__mutmut_3, 
    'x_find_min_diff__mutmut_4': x_find_min_diff__mutmut_4, 
    'x_find_min_diff__mutmut_5': x_find_min_diff__mutmut_5, 
    'x_find_min_diff__mutmut_6': x_find_min_diff__mutmut_6, 
    'x_find_min_diff__mutmut_7': x_find_min_diff__mutmut_7, 
    'x_find_min_diff__mutmut_8': x_find_min_diff__mutmut_8, 
    'x_find_min_diff__mutmut_9': x_find_min_diff__mutmut_9, 
    'x_find_min_diff__mutmut_10': x_find_min_diff__mutmut_10, 
    'x_find_min_diff__mutmut_11': x_find_min_diff__mutmut_11, 
    'x_find_min_diff__mutmut_12': x_find_min_diff__mutmut_12, 
    'x_find_min_diff__mutmut_13': x_find_min_diff__mutmut_13, 
    'x_find_min_diff__mutmut_14': x_find_min_diff__mutmut_14, 
    'x_find_min_diff__mutmut_15': x_find_min_diff__mutmut_15, 
    'x_find_min_diff__mutmut_16': x_find_min_diff__mutmut_16, 
    'x_find_min_diff__mutmut_17': x_find_min_diff__mutmut_17
}

def find_min_diff(*args, **kwargs):
    result = _mutmut_trampoline(x_find_min_diff__mutmut_orig, x_find_min_diff__mutmut_mutants, args, kwargs)
    return result 

find_min_diff.__signature__ = _mutmut_signature(x_find_min_diff__mutmut_orig)
x_find_min_diff__mutmut_orig.__name__ = 'x_find_min_diff'