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
def x_surface_Area__mutmut_orig(b,s): 
    return 2 * b * s + pow(b,2) 
def x_surface_Area__mutmut_1(b,s): 
    return 2 * b * s - pow(b,2) 
def x_surface_Area__mutmut_2(b,s): 
    return 2 * b / s + pow(b,2) 
def x_surface_Area__mutmut_3(b,s): 
    return 2 / b * s + pow(b,2) 
def x_surface_Area__mutmut_4(b,s): 
    return 3 * b * s + pow(b,2) 
def x_surface_Area__mutmut_5(b,s): 
    return 2 * b * s + pow(None,2) 
def x_surface_Area__mutmut_6(b,s): 
    return 2 * b * s + pow(b,None) 
def x_surface_Area__mutmut_7(b,s): 
    return 2 * b * s + pow(2) 
def x_surface_Area__mutmut_8(b,s): 
    return 2 * b * s + pow(b,) 
def x_surface_Area__mutmut_9(b,s): 
    return 2 * b * s + pow(b,3) 

x_surface_Area__mutmut_mutants : ClassVar[MutantDict] = {
'x_surface_Area__mutmut_1': x_surface_Area__mutmut_1, 
    'x_surface_Area__mutmut_2': x_surface_Area__mutmut_2, 
    'x_surface_Area__mutmut_3': x_surface_Area__mutmut_3, 
    'x_surface_Area__mutmut_4': x_surface_Area__mutmut_4, 
    'x_surface_Area__mutmut_5': x_surface_Area__mutmut_5, 
    'x_surface_Area__mutmut_6': x_surface_Area__mutmut_6, 
    'x_surface_Area__mutmut_7': x_surface_Area__mutmut_7, 
    'x_surface_Area__mutmut_8': x_surface_Area__mutmut_8, 
    'x_surface_Area__mutmut_9': x_surface_Area__mutmut_9
}

def surface_Area(*args, **kwargs):
    result = _mutmut_trampoline(x_surface_Area__mutmut_orig, x_surface_Area__mutmut_mutants, args, kwargs)
    return result 

surface_Area.__signature__ = _mutmut_signature(x_surface_Area__mutmut_orig)
x_surface_Area__mutmut_orig.__name__ = 'x_surface_Area'