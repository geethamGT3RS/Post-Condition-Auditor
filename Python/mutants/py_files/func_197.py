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
def x_find_Parity__mutmut_orig(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_1(x): 
    y = None; 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_2(x): 
    y = x & (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_3(x): 
    y = x ^ (x << 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_4(x): 
    y = x ^ (x >> 2); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_5(x): 
    y = x ^ (x >> 1); 
    y = None; 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_6(x): 
    y = x ^ (x >> 1); 
    y = y & (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_7(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y << 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_8(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 3); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_9(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = None; 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_10(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y & (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_11(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y << 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_12(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 5); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_13(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = None; 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_14(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y & (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_15(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y << 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_16(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 9); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_17(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = None; 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_18(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y & (y >> 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_19(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y << 16); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_20(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 17); 
    if (y & 1): 
        return True
    return False
def x_find_Parity__mutmut_21(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y | 1): 
        return True
    return False
def x_find_Parity__mutmut_22(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 2): 
        return True
    return False
def x_find_Parity__mutmut_23(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return False
    return False
def x_find_Parity__mutmut_24(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return True

x_find_Parity__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_Parity__mutmut_1': x_find_Parity__mutmut_1, 
    'x_find_Parity__mutmut_2': x_find_Parity__mutmut_2, 
    'x_find_Parity__mutmut_3': x_find_Parity__mutmut_3, 
    'x_find_Parity__mutmut_4': x_find_Parity__mutmut_4, 
    'x_find_Parity__mutmut_5': x_find_Parity__mutmut_5, 
    'x_find_Parity__mutmut_6': x_find_Parity__mutmut_6, 
    'x_find_Parity__mutmut_7': x_find_Parity__mutmut_7, 
    'x_find_Parity__mutmut_8': x_find_Parity__mutmut_8, 
    'x_find_Parity__mutmut_9': x_find_Parity__mutmut_9, 
    'x_find_Parity__mutmut_10': x_find_Parity__mutmut_10, 
    'x_find_Parity__mutmut_11': x_find_Parity__mutmut_11, 
    'x_find_Parity__mutmut_12': x_find_Parity__mutmut_12, 
    'x_find_Parity__mutmut_13': x_find_Parity__mutmut_13, 
    'x_find_Parity__mutmut_14': x_find_Parity__mutmut_14, 
    'x_find_Parity__mutmut_15': x_find_Parity__mutmut_15, 
    'x_find_Parity__mutmut_16': x_find_Parity__mutmut_16, 
    'x_find_Parity__mutmut_17': x_find_Parity__mutmut_17, 
    'x_find_Parity__mutmut_18': x_find_Parity__mutmut_18, 
    'x_find_Parity__mutmut_19': x_find_Parity__mutmut_19, 
    'x_find_Parity__mutmut_20': x_find_Parity__mutmut_20, 
    'x_find_Parity__mutmut_21': x_find_Parity__mutmut_21, 
    'x_find_Parity__mutmut_22': x_find_Parity__mutmut_22, 
    'x_find_Parity__mutmut_23': x_find_Parity__mutmut_23, 
    'x_find_Parity__mutmut_24': x_find_Parity__mutmut_24
}

def find_Parity(*args, **kwargs):
    result = _mutmut_trampoline(x_find_Parity__mutmut_orig, x_find_Parity__mutmut_mutants, args, kwargs)
    return result 

find_Parity.__signature__ = _mutmut_signature(x_find_Parity__mutmut_orig)
x_find_Parity__mutmut_orig.__name__ = 'x_find_Parity'