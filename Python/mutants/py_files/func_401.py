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
def x_count_divisors__mutmut_orig(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_1(n) : 
    count = None
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_2(n) : 
    count = 1
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_3(n) : 
    count = 0
    for i in range(None, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_4(n) : 
    count = 0
    for i in range(1, None) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_5(n) : 
    count = 0
    for i in range((int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_6(n) : 
    count = 0
    for i in range(1, ) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_7(n) : 
    count = 0
    for i in range(2, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_8(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) - 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_9(n) : 
    count = 0
    for i in range(1, (int)(None) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_10(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(None)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_11(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 3) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_12(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n / i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_13(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i != 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_14(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 1) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_15(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n / i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_16(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i != i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_17(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = None
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_18(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count - 1
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_19(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 2
            else : 
                count = count + 2
    return count % 2 == 0
def x_count_divisors__mutmut_20(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = None
    return count % 2 == 0
def x_count_divisors__mutmut_21(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count - 2
    return count % 2 == 0
def x_count_divisors__mutmut_22(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 3
    return count % 2 == 0
def x_count_divisors__mutmut_23(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count / 2 == 0
def x_count_divisors__mutmut_24(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 3 == 0
def x_count_divisors__mutmut_25(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 != 0
def x_count_divisors__mutmut_26(n) : 
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 2) : 
        if (n % i == 0) : 
            if( n // i == i) : 
                count = count + 1
            else : 
                count = count + 2
    return count % 2 == 1

x_count_divisors__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_divisors__mutmut_1': x_count_divisors__mutmut_1, 
    'x_count_divisors__mutmut_2': x_count_divisors__mutmut_2, 
    'x_count_divisors__mutmut_3': x_count_divisors__mutmut_3, 
    'x_count_divisors__mutmut_4': x_count_divisors__mutmut_4, 
    'x_count_divisors__mutmut_5': x_count_divisors__mutmut_5, 
    'x_count_divisors__mutmut_6': x_count_divisors__mutmut_6, 
    'x_count_divisors__mutmut_7': x_count_divisors__mutmut_7, 
    'x_count_divisors__mutmut_8': x_count_divisors__mutmut_8, 
    'x_count_divisors__mutmut_9': x_count_divisors__mutmut_9, 
    'x_count_divisors__mutmut_10': x_count_divisors__mutmut_10, 
    'x_count_divisors__mutmut_11': x_count_divisors__mutmut_11, 
    'x_count_divisors__mutmut_12': x_count_divisors__mutmut_12, 
    'x_count_divisors__mutmut_13': x_count_divisors__mutmut_13, 
    'x_count_divisors__mutmut_14': x_count_divisors__mutmut_14, 
    'x_count_divisors__mutmut_15': x_count_divisors__mutmut_15, 
    'x_count_divisors__mutmut_16': x_count_divisors__mutmut_16, 
    'x_count_divisors__mutmut_17': x_count_divisors__mutmut_17, 
    'x_count_divisors__mutmut_18': x_count_divisors__mutmut_18, 
    'x_count_divisors__mutmut_19': x_count_divisors__mutmut_19, 
    'x_count_divisors__mutmut_20': x_count_divisors__mutmut_20, 
    'x_count_divisors__mutmut_21': x_count_divisors__mutmut_21, 
    'x_count_divisors__mutmut_22': x_count_divisors__mutmut_22, 
    'x_count_divisors__mutmut_23': x_count_divisors__mutmut_23, 
    'x_count_divisors__mutmut_24': x_count_divisors__mutmut_24, 
    'x_count_divisors__mutmut_25': x_count_divisors__mutmut_25, 
    'x_count_divisors__mutmut_26': x_count_divisors__mutmut_26
}

def count_divisors(*args, **kwargs):
    result = _mutmut_trampoline(x_count_divisors__mutmut_orig, x_count_divisors__mutmut_mutants, args, kwargs)
    return result 

count_divisors.__signature__ = _mutmut_signature(x_count_divisors__mutmut_orig)
x_count_divisors__mutmut_orig.__name__ = 'x_count_divisors'