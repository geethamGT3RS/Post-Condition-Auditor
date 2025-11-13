import math 
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
def x_find_Index__mutmut_orig(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1)))
    return round(x)
def x_find_Index__mutmut_1(n): 
    x = None
    return round(x)
def x_find_Index__mutmut_2(n): 
    x = math.sqrt(None)
    return round(x)
def x_find_Index__mutmut_3(n): 
    x = math.sqrt(2 / math.pow(10,(n - 1)))
    return round(x)
def x_find_Index__mutmut_4(n): 
    x = math.sqrt(3 * math.pow(10,(n - 1)))
    return round(x)
def x_find_Index__mutmut_5(n): 
    x = math.sqrt(2 * math.pow(None,(n - 1)))
    return round(x)
def x_find_Index__mutmut_6(n): 
    x = math.sqrt(2 * math.pow(10,None))
    return round(x)
def x_find_Index__mutmut_7(n): 
    x = math.sqrt(2 * math.pow((n - 1)))
    return round(x)
def x_find_Index__mutmut_8(n): 
    x = math.sqrt(2 * math.pow(10,))
    return round(x)
def x_find_Index__mutmut_9(n): 
    x = math.sqrt(2 * math.pow(11,(n - 1)))
    return round(x)
def x_find_Index__mutmut_10(n): 
    x = math.sqrt(2 * math.pow(10,(n + 1)))
    return round(x)
def x_find_Index__mutmut_11(n): 
    x = math.sqrt(2 * math.pow(10,(n - 2)))
    return round(x)
def x_find_Index__mutmut_12(n): 
    x = math.sqrt(2 * math.pow(10,(n - 1)))
    return round(None)

x_find_Index__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_Index__mutmut_1': x_find_Index__mutmut_1, 
    'x_find_Index__mutmut_2': x_find_Index__mutmut_2, 
    'x_find_Index__mutmut_3': x_find_Index__mutmut_3, 
    'x_find_Index__mutmut_4': x_find_Index__mutmut_4, 
    'x_find_Index__mutmut_5': x_find_Index__mutmut_5, 
    'x_find_Index__mutmut_6': x_find_Index__mutmut_6, 
    'x_find_Index__mutmut_7': x_find_Index__mutmut_7, 
    'x_find_Index__mutmut_8': x_find_Index__mutmut_8, 
    'x_find_Index__mutmut_9': x_find_Index__mutmut_9, 
    'x_find_Index__mutmut_10': x_find_Index__mutmut_10, 
    'x_find_Index__mutmut_11': x_find_Index__mutmut_11, 
    'x_find_Index__mutmut_12': x_find_Index__mutmut_12
}

def find_Index(*args, **kwargs):
    result = _mutmut_trampoline(x_find_Index__mutmut_orig, x_find_Index__mutmut_mutants, args, kwargs)
    return result 

find_Index.__signature__ = _mutmut_signature(x_find_Index__mutmut_orig)
x_find_Index__mutmut_orig.__name__ = 'x_find_Index'