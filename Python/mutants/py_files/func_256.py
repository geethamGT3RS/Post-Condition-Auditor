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
def x_find_remainder__mutmut_orig(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
def x_find_remainder__mutmut_1(arr, n): 
    mul = None
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
def x_find_remainder__mutmut_2(arr, n): 
    mul = 2
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
def x_find_remainder__mutmut_3(arr, n): 
    mul = 1
    for i in range(None):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 
def x_find_remainder__mutmut_4(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = None 
    return mul % n 
def x_find_remainder__mutmut_5(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) / n 
    return mul % n 
def x_find_remainder__mutmut_6(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul / (arr[i] % n)) % n 
    return mul % n 
def x_find_remainder__mutmut_7(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul * (arr[i] / n)) % n 
    return mul % n 
def x_find_remainder__mutmut_8(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) % n 
    return mul / n 

x_find_remainder__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_remainder__mutmut_1': x_find_remainder__mutmut_1, 
    'x_find_remainder__mutmut_2': x_find_remainder__mutmut_2, 
    'x_find_remainder__mutmut_3': x_find_remainder__mutmut_3, 
    'x_find_remainder__mutmut_4': x_find_remainder__mutmut_4, 
    'x_find_remainder__mutmut_5': x_find_remainder__mutmut_5, 
    'x_find_remainder__mutmut_6': x_find_remainder__mutmut_6, 
    'x_find_remainder__mutmut_7': x_find_remainder__mutmut_7, 
    'x_find_remainder__mutmut_8': x_find_remainder__mutmut_8
}

def find_remainder(*args, **kwargs):
    result = _mutmut_trampoline(x_find_remainder__mutmut_orig, x_find_remainder__mutmut_mutants, args, kwargs)
    return result 

find_remainder.__signature__ = _mutmut_signature(x_find_remainder__mutmut_orig)
x_find_remainder__mutmut_orig.__name__ = 'x_find_remainder'