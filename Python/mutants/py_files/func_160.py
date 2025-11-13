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
def x_square_Sum__mutmut_orig(n):  
    return int(2*n*(n+1)*(2*n+1)/3)
def x_square_Sum__mutmut_1(n):  
    return int(None)
def x_square_Sum__mutmut_2(n):  
    return int(2*n*(n+1)*(2*n+1) * 3)
def x_square_Sum__mutmut_3(n):  
    return int(2*n*(n+1) / (2*n+1)/3)
def x_square_Sum__mutmut_4(n):  
    return int(2*n / (n+1)*(2*n+1)/3)
def x_square_Sum__mutmut_5(n):  
    return int(2 / n*(n+1)*(2*n+1)/3)
def x_square_Sum__mutmut_6(n):  
    return int(3*n*(n+1)*(2*n+1)/3)
def x_square_Sum__mutmut_7(n):  
    return int(2*n*(n - 1)*(2*n+1)/3)
def x_square_Sum__mutmut_8(n):  
    return int(2*n*(n+2)*(2*n+1)/3)
def x_square_Sum__mutmut_9(n):  
    return int(2*n*(n+1)*(2*n - 1)/3)
def x_square_Sum__mutmut_10(n):  
    return int(2*n*(n+1)*(2 / n+1)/3)
def x_square_Sum__mutmut_11(n):  
    return int(2*n*(n+1)*(3*n+1)/3)
def x_square_Sum__mutmut_12(n):  
    return int(2*n*(n+1)*(2*n+2)/3)
def x_square_Sum__mutmut_13(n):  
    return int(2*n*(n+1)*(2*n+1)/4)

x_square_Sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_square_Sum__mutmut_1': x_square_Sum__mutmut_1, 
    'x_square_Sum__mutmut_2': x_square_Sum__mutmut_2, 
    'x_square_Sum__mutmut_3': x_square_Sum__mutmut_3, 
    'x_square_Sum__mutmut_4': x_square_Sum__mutmut_4, 
    'x_square_Sum__mutmut_5': x_square_Sum__mutmut_5, 
    'x_square_Sum__mutmut_6': x_square_Sum__mutmut_6, 
    'x_square_Sum__mutmut_7': x_square_Sum__mutmut_7, 
    'x_square_Sum__mutmut_8': x_square_Sum__mutmut_8, 
    'x_square_Sum__mutmut_9': x_square_Sum__mutmut_9, 
    'x_square_Sum__mutmut_10': x_square_Sum__mutmut_10, 
    'x_square_Sum__mutmut_11': x_square_Sum__mutmut_11, 
    'x_square_Sum__mutmut_12': x_square_Sum__mutmut_12, 
    'x_square_Sum__mutmut_13': x_square_Sum__mutmut_13
}

def square_Sum(*args, **kwargs):
    result = _mutmut_trampoline(x_square_Sum__mutmut_orig, x_square_Sum__mutmut_mutants, args, kwargs)
    return result 

square_Sum.__signature__ = _mutmut_signature(x_square_Sum__mutmut_orig)
x_square_Sum__mutmut_orig.__name__ = 'x_square_Sum'