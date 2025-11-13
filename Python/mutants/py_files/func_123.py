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
def x_babylonian_squareroot__mutmut_orig(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_1(number):
    if(number != 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_2(number):
    if(number == 1):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_3(number):
    if(number == 0):
        return 1;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_4(number):
    if(number == 0):
        return 0;
    g = None;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_5(number):
    if(number == 0):
        return 0;
    g = number * 2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_6(number):
    if(number == 0):
        return 0;
    g = number/3.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_7(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = None;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_8(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g - 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_9(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 2;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_10(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g == g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_11(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = None;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_12(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number * g;
        g2 = g;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_13(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = None;
        g = (g + n)/2;
    return g;
def x_babylonian_squareroot__mutmut_14(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = None;
    return g;
def x_babylonian_squareroot__mutmut_15(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n) * 2;
    return g;
def x_babylonian_squareroot__mutmut_16(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g - n)/2;
    return g;
def x_babylonian_squareroot__mutmut_17(number):
    if(number == 0):
        return 0;
    g = number/2.0;
    g2 = g + 1;
    while(g != g2):
        n = number/ g;
        g2 = g;
        g = (g + n)/3;
    return g;

x_babylonian_squareroot__mutmut_mutants : ClassVar[MutantDict] = {
'x_babylonian_squareroot__mutmut_1': x_babylonian_squareroot__mutmut_1, 
    'x_babylonian_squareroot__mutmut_2': x_babylonian_squareroot__mutmut_2, 
    'x_babylonian_squareroot__mutmut_3': x_babylonian_squareroot__mutmut_3, 
    'x_babylonian_squareroot__mutmut_4': x_babylonian_squareroot__mutmut_4, 
    'x_babylonian_squareroot__mutmut_5': x_babylonian_squareroot__mutmut_5, 
    'x_babylonian_squareroot__mutmut_6': x_babylonian_squareroot__mutmut_6, 
    'x_babylonian_squareroot__mutmut_7': x_babylonian_squareroot__mutmut_7, 
    'x_babylonian_squareroot__mutmut_8': x_babylonian_squareroot__mutmut_8, 
    'x_babylonian_squareroot__mutmut_9': x_babylonian_squareroot__mutmut_9, 
    'x_babylonian_squareroot__mutmut_10': x_babylonian_squareroot__mutmut_10, 
    'x_babylonian_squareroot__mutmut_11': x_babylonian_squareroot__mutmut_11, 
    'x_babylonian_squareroot__mutmut_12': x_babylonian_squareroot__mutmut_12, 
    'x_babylonian_squareroot__mutmut_13': x_babylonian_squareroot__mutmut_13, 
    'x_babylonian_squareroot__mutmut_14': x_babylonian_squareroot__mutmut_14, 
    'x_babylonian_squareroot__mutmut_15': x_babylonian_squareroot__mutmut_15, 
    'x_babylonian_squareroot__mutmut_16': x_babylonian_squareroot__mutmut_16, 
    'x_babylonian_squareroot__mutmut_17': x_babylonian_squareroot__mutmut_17
}

def babylonian_squareroot(*args, **kwargs):
    result = _mutmut_trampoline(x_babylonian_squareroot__mutmut_orig, x_babylonian_squareroot__mutmut_mutants, args, kwargs)
    return result 

babylonian_squareroot.__signature__ = _mutmut_signature(x_babylonian_squareroot__mutmut_orig)
x_babylonian_squareroot__mutmut_orig.__name__ = 'x_babylonian_squareroot'