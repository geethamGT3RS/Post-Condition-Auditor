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
def x_count_rotation__mutmut_orig(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_1(arr):   
    for i in range (None,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_2(arr):   
    for i in range (1,None): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_3(arr):   
    for i in range (len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_4(arr):   
    for i in range (1,): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_5(arr):   
    for i in range (2,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_6(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] <= arr[i - 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_7(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i + 1]): 
            return i  
    return 0
def x_count_rotation__mutmut_8(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i - 2]): 
            return i  
    return 0
def x_count_rotation__mutmut_9(arr):   
    for i in range (1,len(arr)): 
        if (arr[i] < arr[i - 1]): 
            return i  
    return 1

x_count_rotation__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_rotation__mutmut_1': x_count_rotation__mutmut_1, 
    'x_count_rotation__mutmut_2': x_count_rotation__mutmut_2, 
    'x_count_rotation__mutmut_3': x_count_rotation__mutmut_3, 
    'x_count_rotation__mutmut_4': x_count_rotation__mutmut_4, 
    'x_count_rotation__mutmut_5': x_count_rotation__mutmut_5, 
    'x_count_rotation__mutmut_6': x_count_rotation__mutmut_6, 
    'x_count_rotation__mutmut_7': x_count_rotation__mutmut_7, 
    'x_count_rotation__mutmut_8': x_count_rotation__mutmut_8, 
    'x_count_rotation__mutmut_9': x_count_rotation__mutmut_9
}

def count_rotation(*args, **kwargs):
    result = _mutmut_trampoline(x_count_rotation__mutmut_orig, x_count_rotation__mutmut_mutants, args, kwargs)
    return result 

count_rotation.__signature__ = _mutmut_signature(x_count_rotation__mutmut_orig)
x_count_rotation__mutmut_orig.__name__ = 'x_count_rotation'