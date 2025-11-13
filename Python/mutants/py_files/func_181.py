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
def x_highest_Power_of_2__mutmut_orig(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_1(n): 
    res = None 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_2(n): 
    res = 1 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_3(n): 
    res = 0 
    for i in range(None, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_4(n): 
    res = 0 
    for i in range(n, None, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_5(n): 
    res = 0 
    for i in range(n, 0, None): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_6(n): 
    res = 0 
    for i in range(0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_7(n): 
    res = 0 
    for i in range(n, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_8(n): 
    res = 0 
    for i in range(n, 0, ): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_9(n): 
    res = 0 
    for i in range(n, 1, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_10(n): 
    res = 0 
    for i in range(n, 0, +1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_11(n): 
    res = 0 
    for i in range(n, 0, -2): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_12(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i | (i - 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_13(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i + 1)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_14(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 2)) == 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_15(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) != 0): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_16(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 1): 
            res = i 
            break 
    return res 
def x_highest_Power_of_2__mutmut_17(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = None 
            break 
    return res 
def x_highest_Power_of_2__mutmut_18(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            return 
    return res 

x_highest_Power_of_2__mutmut_mutants : ClassVar[MutantDict] = {
'x_highest_Power_of_2__mutmut_1': x_highest_Power_of_2__mutmut_1, 
    'x_highest_Power_of_2__mutmut_2': x_highest_Power_of_2__mutmut_2, 
    'x_highest_Power_of_2__mutmut_3': x_highest_Power_of_2__mutmut_3, 
    'x_highest_Power_of_2__mutmut_4': x_highest_Power_of_2__mutmut_4, 
    'x_highest_Power_of_2__mutmut_5': x_highest_Power_of_2__mutmut_5, 
    'x_highest_Power_of_2__mutmut_6': x_highest_Power_of_2__mutmut_6, 
    'x_highest_Power_of_2__mutmut_7': x_highest_Power_of_2__mutmut_7, 
    'x_highest_Power_of_2__mutmut_8': x_highest_Power_of_2__mutmut_8, 
    'x_highest_Power_of_2__mutmut_9': x_highest_Power_of_2__mutmut_9, 
    'x_highest_Power_of_2__mutmut_10': x_highest_Power_of_2__mutmut_10, 
    'x_highest_Power_of_2__mutmut_11': x_highest_Power_of_2__mutmut_11, 
    'x_highest_Power_of_2__mutmut_12': x_highest_Power_of_2__mutmut_12, 
    'x_highest_Power_of_2__mutmut_13': x_highest_Power_of_2__mutmut_13, 
    'x_highest_Power_of_2__mutmut_14': x_highest_Power_of_2__mutmut_14, 
    'x_highest_Power_of_2__mutmut_15': x_highest_Power_of_2__mutmut_15, 
    'x_highest_Power_of_2__mutmut_16': x_highest_Power_of_2__mutmut_16, 
    'x_highest_Power_of_2__mutmut_17': x_highest_Power_of_2__mutmut_17, 
    'x_highest_Power_of_2__mutmut_18': x_highest_Power_of_2__mutmut_18
}

def highest_Power_of_2(*args, **kwargs):
    result = _mutmut_trampoline(x_highest_Power_of_2__mutmut_orig, x_highest_Power_of_2__mutmut_mutants, args, kwargs)
    return result 

highest_Power_of_2.__signature__ = _mutmut_signature(x_highest_Power_of_2__mutmut_orig)
x_highest_Power_of_2__mutmut_orig.__name__ = 'x_highest_Power_of_2'