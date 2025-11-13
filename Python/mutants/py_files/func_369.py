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
def x_sector_area__mutmut_orig(r,a):
    if a > 360:
        return None
    return (math.pi*r**2) * (a/360)
def x_sector_area__mutmut_1(r,a):
    if a >= 360:
        return None
    return (math.pi*r**2) * (a/360)
def x_sector_area__mutmut_2(r,a):
    if a > 361:
        return None
    return (math.pi*r**2) * (a/360)
def x_sector_area__mutmut_3(r,a):
    if a > 360:
        return None
    return (math.pi*r**2) / (a/360)
def x_sector_area__mutmut_4(r,a):
    if a > 360:
        return None
    return (math.pi / r**2) * (a/360)
def x_sector_area__mutmut_5(r,a):
    if a > 360:
        return None
    return (math.pi*r * 2) * (a/360)
def x_sector_area__mutmut_6(r,a):
    if a > 360:
        return None
    return (math.pi*r**3) * (a/360)
def x_sector_area__mutmut_7(r,a):
    if a > 360:
        return None
    return (math.pi*r**2) * (a * 360)
def x_sector_area__mutmut_8(r,a):
    if a > 360:
        return None
    return (math.pi*r**2) * (a/361)

x_sector_area__mutmut_mutants : ClassVar[MutantDict] = {
'x_sector_area__mutmut_1': x_sector_area__mutmut_1, 
    'x_sector_area__mutmut_2': x_sector_area__mutmut_2, 
    'x_sector_area__mutmut_3': x_sector_area__mutmut_3, 
    'x_sector_area__mutmut_4': x_sector_area__mutmut_4, 
    'x_sector_area__mutmut_5': x_sector_area__mutmut_5, 
    'x_sector_area__mutmut_6': x_sector_area__mutmut_6, 
    'x_sector_area__mutmut_7': x_sector_area__mutmut_7, 
    'x_sector_area__mutmut_8': x_sector_area__mutmut_8
}

def sector_area(*args, **kwargs):
    result = _mutmut_trampoline(x_sector_area__mutmut_orig, x_sector_area__mutmut_mutants, args, kwargs)
    return result 

sector_area.__signature__ = _mutmut_signature(x_sector_area__mutmut_orig)
x_sector_area__mutmut_orig.__name__ = 'x_sector_area'