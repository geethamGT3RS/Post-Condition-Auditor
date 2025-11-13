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
def x_set_left_most_unset_bit__mutmut_orig(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_1(n): 
    if (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_2(n): 
    if not (n | (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_3(n): 
    if not (n & (n - 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_4(n): 
    if not (n & (n + 2)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_5(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = None 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_6(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 1, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_7(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 1 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_8(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_9(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp | 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_10(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 2): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_11(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = None      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_12(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count = 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_13(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count -= 1; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_14(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 2; temp>>=1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_15(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp = 1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_16(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp <<= 1
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_17(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=2
    return (n | (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_18(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n & (1 << (pos))) 
def x_set_left_most_unset_bit__mutmut_19(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 >> (pos))) 
def x_set_left_most_unset_bit__mutmut_20(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (2 << (pos))) 

x_set_left_most_unset_bit__mutmut_mutants : ClassVar[MutantDict] = {
'x_set_left_most_unset_bit__mutmut_1': x_set_left_most_unset_bit__mutmut_1, 
    'x_set_left_most_unset_bit__mutmut_2': x_set_left_most_unset_bit__mutmut_2, 
    'x_set_left_most_unset_bit__mutmut_3': x_set_left_most_unset_bit__mutmut_3, 
    'x_set_left_most_unset_bit__mutmut_4': x_set_left_most_unset_bit__mutmut_4, 
    'x_set_left_most_unset_bit__mutmut_5': x_set_left_most_unset_bit__mutmut_5, 
    'x_set_left_most_unset_bit__mutmut_6': x_set_left_most_unset_bit__mutmut_6, 
    'x_set_left_most_unset_bit__mutmut_7': x_set_left_most_unset_bit__mutmut_7, 
    'x_set_left_most_unset_bit__mutmut_8': x_set_left_most_unset_bit__mutmut_8, 
    'x_set_left_most_unset_bit__mutmut_9': x_set_left_most_unset_bit__mutmut_9, 
    'x_set_left_most_unset_bit__mutmut_10': x_set_left_most_unset_bit__mutmut_10, 
    'x_set_left_most_unset_bit__mutmut_11': x_set_left_most_unset_bit__mutmut_11, 
    'x_set_left_most_unset_bit__mutmut_12': x_set_left_most_unset_bit__mutmut_12, 
    'x_set_left_most_unset_bit__mutmut_13': x_set_left_most_unset_bit__mutmut_13, 
    'x_set_left_most_unset_bit__mutmut_14': x_set_left_most_unset_bit__mutmut_14, 
    'x_set_left_most_unset_bit__mutmut_15': x_set_left_most_unset_bit__mutmut_15, 
    'x_set_left_most_unset_bit__mutmut_16': x_set_left_most_unset_bit__mutmut_16, 
    'x_set_left_most_unset_bit__mutmut_17': x_set_left_most_unset_bit__mutmut_17, 
    'x_set_left_most_unset_bit__mutmut_18': x_set_left_most_unset_bit__mutmut_18, 
    'x_set_left_most_unset_bit__mutmut_19': x_set_left_most_unset_bit__mutmut_19, 
    'x_set_left_most_unset_bit__mutmut_20': x_set_left_most_unset_bit__mutmut_20
}

def set_left_most_unset_bit(*args, **kwargs):
    result = _mutmut_trampoline(x_set_left_most_unset_bit__mutmut_orig, x_set_left_most_unset_bit__mutmut_mutants, args, kwargs)
    return result 

set_left_most_unset_bit.__signature__ = _mutmut_signature(x_set_left_most_unset_bit__mutmut_orig)
x_set_left_most_unset_bit__mutmut_orig.__name__ = 'x_set_left_most_unset_bit'