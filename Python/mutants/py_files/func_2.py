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
def x_is_not_prime__mutmut_orig(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_1(n):
    result = None
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_2(n):
    result = True
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_3(n):
    result = False
    for i in range(None,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_4(n):
    result = False
    for i in range(2,None):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_5(n):
    result = False
    for i in range(int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_6(n):
    result = False
    for i in range(2,):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_7(n):
    result = False
    for i in range(3,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_8(n):
    result = False
    for i in range(2,int(math.sqrt(n)) - 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_9(n):
    result = False
    for i in range(2,int(None) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_10(n):
    result = False
    for i in range(2,int(math.sqrt(None)) + 1):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_11(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 2):
        if n % i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_12(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n / i == 0:
            result = True
    return result
def x_is_not_prime__mutmut_13(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i != 0:
            result = True
    return result
def x_is_not_prime__mutmut_14(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 1:
            result = True
    return result
def x_is_not_prime__mutmut_15(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = None
    return result
def x_is_not_prime__mutmut_16(n):
    result = False
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            result = False
    return result

x_is_not_prime__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_not_prime__mutmut_1': x_is_not_prime__mutmut_1, 
    'x_is_not_prime__mutmut_2': x_is_not_prime__mutmut_2, 
    'x_is_not_prime__mutmut_3': x_is_not_prime__mutmut_3, 
    'x_is_not_prime__mutmut_4': x_is_not_prime__mutmut_4, 
    'x_is_not_prime__mutmut_5': x_is_not_prime__mutmut_5, 
    'x_is_not_prime__mutmut_6': x_is_not_prime__mutmut_6, 
    'x_is_not_prime__mutmut_7': x_is_not_prime__mutmut_7, 
    'x_is_not_prime__mutmut_8': x_is_not_prime__mutmut_8, 
    'x_is_not_prime__mutmut_9': x_is_not_prime__mutmut_9, 
    'x_is_not_prime__mutmut_10': x_is_not_prime__mutmut_10, 
    'x_is_not_prime__mutmut_11': x_is_not_prime__mutmut_11, 
    'x_is_not_prime__mutmut_12': x_is_not_prime__mutmut_12, 
    'x_is_not_prime__mutmut_13': x_is_not_prime__mutmut_13, 
    'x_is_not_prime__mutmut_14': x_is_not_prime__mutmut_14, 
    'x_is_not_prime__mutmut_15': x_is_not_prime__mutmut_15, 
    'x_is_not_prime__mutmut_16': x_is_not_prime__mutmut_16
}

def is_not_prime(*args, **kwargs):
    result = _mutmut_trampoline(x_is_not_prime__mutmut_orig, x_is_not_prime__mutmut_mutants, args, kwargs)
    return result 

is_not_prime.__signature__ = _mutmut_signature(x_is_not_prime__mutmut_orig)
x_is_not_prime__mutmut_orig.__name__ = 'x_is_not_prime'