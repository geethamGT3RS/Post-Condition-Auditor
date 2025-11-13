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
def x_find_sum__mutmut_orig(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_1(arr): 
    arr.sort() 
    sum = None 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_2(arr): 
    arr.sort() 
    sum = arr[1] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_3(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(None): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_4(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr) + 1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_5(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-2): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_6(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] == arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_7(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i - 1]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_8(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+2]): 
            sum = sum + arr[i+1]   
    return sum
def x_find_sum__mutmut_9(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = None   
    return sum
def x_find_sum__mutmut_10(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum - arr[i+1]   
    return sum
def x_find_sum__mutmut_11(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i - 1]   
    return sum
def x_find_sum__mutmut_12(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+2]   
    return sum

x_find_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_sum__mutmut_1': x_find_sum__mutmut_1, 
    'x_find_sum__mutmut_2': x_find_sum__mutmut_2, 
    'x_find_sum__mutmut_3': x_find_sum__mutmut_3, 
    'x_find_sum__mutmut_4': x_find_sum__mutmut_4, 
    'x_find_sum__mutmut_5': x_find_sum__mutmut_5, 
    'x_find_sum__mutmut_6': x_find_sum__mutmut_6, 
    'x_find_sum__mutmut_7': x_find_sum__mutmut_7, 
    'x_find_sum__mutmut_8': x_find_sum__mutmut_8, 
    'x_find_sum__mutmut_9': x_find_sum__mutmut_9, 
    'x_find_sum__mutmut_10': x_find_sum__mutmut_10, 
    'x_find_sum__mutmut_11': x_find_sum__mutmut_11, 
    'x_find_sum__mutmut_12': x_find_sum__mutmut_12
}

def find_sum(*args, **kwargs):
    result = _mutmut_trampoline(x_find_sum__mutmut_orig, x_find_sum__mutmut_mutants, args, kwargs)
    return result 

find_sum.__signature__ = _mutmut_signature(x_find_sum__mutmut_orig)
x_find_sum__mutmut_orig.__name__ = 'x_find_sum'