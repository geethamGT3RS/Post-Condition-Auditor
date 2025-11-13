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
def x_sum__mutmut_orig(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_1(a,b): 
    sum = None
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_2(a,b): 
    sum = 1
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_3(a,b): 
    sum = 0
    for i in range (None,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_4(a,b): 
    sum = 0
    for i in range (1,None): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_5(a,b): 
    sum = 0
    for i in range (min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_6(a,b): 
    sum = 0
    for i in range (1,): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_7(a,b): 
    sum = 0
    for i in range (2,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_8(a,b): 
    sum = 0
    for i in range (1,min(None,b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_9(a,b): 
    sum = 0
    for i in range (1,min(a,None)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_10(a,b): 
    sum = 0
    for i in range (1,min(b)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_11(a,b): 
    sum = 0
    for i in range (1,min(a,)): 
        if (a % i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_12(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 or b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_13(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a / i == 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_14(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i != 0 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_15(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 1 and b % i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_16(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b / i == 0): 
            sum += i 
    return sum
def x_sum__mutmut_17(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i != 0): 
            sum += i 
    return sum
def x_sum__mutmut_18(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 1): 
            sum += i 
    return sum
def x_sum__mutmut_19(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum = i 
    return sum
def x_sum__mutmut_20(a,b): 
    sum = 0
    for i in range (1,min(a,b)): 
        if (a % i == 0 and b % i == 0): 
            sum -= i 
    return sum

x_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum__mutmut_1': x_sum__mutmut_1, 
    'x_sum__mutmut_2': x_sum__mutmut_2, 
    'x_sum__mutmut_3': x_sum__mutmut_3, 
    'x_sum__mutmut_4': x_sum__mutmut_4, 
    'x_sum__mutmut_5': x_sum__mutmut_5, 
    'x_sum__mutmut_6': x_sum__mutmut_6, 
    'x_sum__mutmut_7': x_sum__mutmut_7, 
    'x_sum__mutmut_8': x_sum__mutmut_8, 
    'x_sum__mutmut_9': x_sum__mutmut_9, 
    'x_sum__mutmut_10': x_sum__mutmut_10, 
    'x_sum__mutmut_11': x_sum__mutmut_11, 
    'x_sum__mutmut_12': x_sum__mutmut_12, 
    'x_sum__mutmut_13': x_sum__mutmut_13, 
    'x_sum__mutmut_14': x_sum__mutmut_14, 
    'x_sum__mutmut_15': x_sum__mutmut_15, 
    'x_sum__mutmut_16': x_sum__mutmut_16, 
    'x_sum__mutmut_17': x_sum__mutmut_17, 
    'x_sum__mutmut_18': x_sum__mutmut_18, 
    'x_sum__mutmut_19': x_sum__mutmut_19, 
    'x_sum__mutmut_20': x_sum__mutmut_20
}

def sum(*args, **kwargs):
    result = _mutmut_trampoline(x_sum__mutmut_orig, x_sum__mutmut_mutants, args, kwargs)
    return result 

sum.__signature__ = _mutmut_signature(x_sum__mutmut_orig)
x_sum__mutmut_orig.__name__ = 'x_sum'