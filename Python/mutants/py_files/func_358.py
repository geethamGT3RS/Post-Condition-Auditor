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
def x_set_middle_bits__mutmut_orig(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_1(n):  
    n = n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_2(n):  
    n &= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_3(n):  
    n |= n << 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_4(n):  
    n |= n >> 2; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_5(n):  
    n |= n >> 1; 
    n = n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_6(n):  
    n |= n >> 1; 
    n &= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_7(n):  
    n |= n >> 1; 
    n |= n << 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_8(n):  
    n |= n >> 1; 
    n |= n >> 3; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_9(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n = n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_10(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n &= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_11(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n << 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_12(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 5; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_13(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n = n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_14(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n &= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_15(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n << 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_16(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 9; 
    n |= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_17(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n = n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_18(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n &= n >> 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_19(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n << 16;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_20(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 17;  
    return (n >> 1) ^ 1
def x_set_middle_bits__mutmut_21(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) & 1
def x_set_middle_bits__mutmut_22(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n << 1) ^ 1
def x_set_middle_bits__mutmut_23(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 2) ^ 1
def x_set_middle_bits__mutmut_24(n):  
    n |= n >> 1; 
    n |= n >> 2; 
    n |= n >> 4; 
    n |= n >> 8; 
    n |= n >> 16;  
    return (n >> 1) ^ 2

x_set_middle_bits__mutmut_mutants : ClassVar[MutantDict] = {
'x_set_middle_bits__mutmut_1': x_set_middle_bits__mutmut_1, 
    'x_set_middle_bits__mutmut_2': x_set_middle_bits__mutmut_2, 
    'x_set_middle_bits__mutmut_3': x_set_middle_bits__mutmut_3, 
    'x_set_middle_bits__mutmut_4': x_set_middle_bits__mutmut_4, 
    'x_set_middle_bits__mutmut_5': x_set_middle_bits__mutmut_5, 
    'x_set_middle_bits__mutmut_6': x_set_middle_bits__mutmut_6, 
    'x_set_middle_bits__mutmut_7': x_set_middle_bits__mutmut_7, 
    'x_set_middle_bits__mutmut_8': x_set_middle_bits__mutmut_8, 
    'x_set_middle_bits__mutmut_9': x_set_middle_bits__mutmut_9, 
    'x_set_middle_bits__mutmut_10': x_set_middle_bits__mutmut_10, 
    'x_set_middle_bits__mutmut_11': x_set_middle_bits__mutmut_11, 
    'x_set_middle_bits__mutmut_12': x_set_middle_bits__mutmut_12, 
    'x_set_middle_bits__mutmut_13': x_set_middle_bits__mutmut_13, 
    'x_set_middle_bits__mutmut_14': x_set_middle_bits__mutmut_14, 
    'x_set_middle_bits__mutmut_15': x_set_middle_bits__mutmut_15, 
    'x_set_middle_bits__mutmut_16': x_set_middle_bits__mutmut_16, 
    'x_set_middle_bits__mutmut_17': x_set_middle_bits__mutmut_17, 
    'x_set_middle_bits__mutmut_18': x_set_middle_bits__mutmut_18, 
    'x_set_middle_bits__mutmut_19': x_set_middle_bits__mutmut_19, 
    'x_set_middle_bits__mutmut_20': x_set_middle_bits__mutmut_20, 
    'x_set_middle_bits__mutmut_21': x_set_middle_bits__mutmut_21, 
    'x_set_middle_bits__mutmut_22': x_set_middle_bits__mutmut_22, 
    'x_set_middle_bits__mutmut_23': x_set_middle_bits__mutmut_23, 
    'x_set_middle_bits__mutmut_24': x_set_middle_bits__mutmut_24
}

def set_middle_bits(*args, **kwargs):
    result = _mutmut_trampoline(x_set_middle_bits__mutmut_orig, x_set_middle_bits__mutmut_mutants, args, kwargs)
    return result 

set_middle_bits.__signature__ = _mutmut_signature(x_set_middle_bits__mutmut_orig)
x_set_middle_bits__mutmut_orig.__name__ = 'x_set_middle_bits'
def x_toggle_middle_bits__mutmut_orig(n): 
    if (n == 1): 
        return 1
    return n ^ set_middle_bits(n) 
def x_toggle_middle_bits__mutmut_1(n): 
    if (n != 1): 
        return 1
    return n ^ set_middle_bits(n) 
def x_toggle_middle_bits__mutmut_2(n): 
    if (n == 2): 
        return 1
    return n ^ set_middle_bits(n) 
def x_toggle_middle_bits__mutmut_3(n): 
    if (n == 1): 
        return 2
    return n ^ set_middle_bits(n) 
def x_toggle_middle_bits__mutmut_4(n): 
    if (n == 1): 
        return 1
    return n & set_middle_bits(n) 
def x_toggle_middle_bits__mutmut_5(n): 
    if (n == 1): 
        return 1
    return n ^ set_middle_bits(None) 

x_toggle_middle_bits__mutmut_mutants : ClassVar[MutantDict] = {
'x_toggle_middle_bits__mutmut_1': x_toggle_middle_bits__mutmut_1, 
    'x_toggle_middle_bits__mutmut_2': x_toggle_middle_bits__mutmut_2, 
    'x_toggle_middle_bits__mutmut_3': x_toggle_middle_bits__mutmut_3, 
    'x_toggle_middle_bits__mutmut_4': x_toggle_middle_bits__mutmut_4, 
    'x_toggle_middle_bits__mutmut_5': x_toggle_middle_bits__mutmut_5
}

def toggle_middle_bits(*args, **kwargs):
    result = _mutmut_trampoline(x_toggle_middle_bits__mutmut_orig, x_toggle_middle_bits__mutmut_mutants, args, kwargs)
    return result 

toggle_middle_bits.__signature__ = _mutmut_signature(x_toggle_middle_bits__mutmut_orig)
x_toggle_middle_bits__mutmut_orig.__name__ = 'x_toggle_middle_bits'