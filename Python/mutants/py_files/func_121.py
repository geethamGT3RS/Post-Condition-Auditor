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
def x_next_Perfect_Square__mutmut_orig(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_1(N): 
    nextN = None
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_2(N): 
    nextN = math.floor(math.sqrt(N)) - 1
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_3(N): 
    nextN = math.floor(None) + 1
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_4(N): 
    nextN = math.floor(math.sqrt(None)) + 1
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_5(N): 
    nextN = math.floor(math.sqrt(N)) + 2
    return nextN * nextN 
def x_next_Perfect_Square__mutmut_6(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN / nextN 

x_next_Perfect_Square__mutmut_mutants : ClassVar[MutantDict] = {
'x_next_Perfect_Square__mutmut_1': x_next_Perfect_Square__mutmut_1, 
    'x_next_Perfect_Square__mutmut_2': x_next_Perfect_Square__mutmut_2, 
    'x_next_Perfect_Square__mutmut_3': x_next_Perfect_Square__mutmut_3, 
    'x_next_Perfect_Square__mutmut_4': x_next_Perfect_Square__mutmut_4, 
    'x_next_Perfect_Square__mutmut_5': x_next_Perfect_Square__mutmut_5, 
    'x_next_Perfect_Square__mutmut_6': x_next_Perfect_Square__mutmut_6
}

def next_Perfect_Square(*args, **kwargs):
    result = _mutmut_trampoline(x_next_Perfect_Square__mutmut_orig, x_next_Perfect_Square__mutmut_mutants, args, kwargs)
    return result 

next_Perfect_Square.__signature__ = _mutmut_signature(x_next_Perfect_Square__mutmut_orig)
x_next_Perfect_Square__mutmut_orig.__name__ = 'x_next_Perfect_Square'