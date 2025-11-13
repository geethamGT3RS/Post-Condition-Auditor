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
def x_count_Primes_nums__mutmut_orig(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_1(n):
    ctr = None
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_2(n):
    ctr = 1
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_3(n):
    ctr = 0
    for num in range(None):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_4(n):
    ctr = 0
    for num in range(n):
        if num < 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_5(n):
    ctr = 0
    for num in range(n):
        if num <= 2:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_6(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            break
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_7(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(None,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_8(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,None):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_9(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_10(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_11(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(3,num):
            if (num % i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_12(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num / i) == 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_13(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) != 0:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_14(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 1:
                break
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_15(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                return
        else:
            ctr += 1
    return ctr
def x_count_Primes_nums__mutmut_16(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr = 1
    return ctr
def x_count_Primes_nums__mutmut_17(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr -= 1
    return ctr
def x_count_Primes_nums__mutmut_18(n):
    ctr = 0
    for num in range(n):
        if num <= 1:
            continue
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            ctr += 2
    return ctr

x_count_Primes_nums__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_Primes_nums__mutmut_1': x_count_Primes_nums__mutmut_1, 
    'x_count_Primes_nums__mutmut_2': x_count_Primes_nums__mutmut_2, 
    'x_count_Primes_nums__mutmut_3': x_count_Primes_nums__mutmut_3, 
    'x_count_Primes_nums__mutmut_4': x_count_Primes_nums__mutmut_4, 
    'x_count_Primes_nums__mutmut_5': x_count_Primes_nums__mutmut_5, 
    'x_count_Primes_nums__mutmut_6': x_count_Primes_nums__mutmut_6, 
    'x_count_Primes_nums__mutmut_7': x_count_Primes_nums__mutmut_7, 
    'x_count_Primes_nums__mutmut_8': x_count_Primes_nums__mutmut_8, 
    'x_count_Primes_nums__mutmut_9': x_count_Primes_nums__mutmut_9, 
    'x_count_Primes_nums__mutmut_10': x_count_Primes_nums__mutmut_10, 
    'x_count_Primes_nums__mutmut_11': x_count_Primes_nums__mutmut_11, 
    'x_count_Primes_nums__mutmut_12': x_count_Primes_nums__mutmut_12, 
    'x_count_Primes_nums__mutmut_13': x_count_Primes_nums__mutmut_13, 
    'x_count_Primes_nums__mutmut_14': x_count_Primes_nums__mutmut_14, 
    'x_count_Primes_nums__mutmut_15': x_count_Primes_nums__mutmut_15, 
    'x_count_Primes_nums__mutmut_16': x_count_Primes_nums__mutmut_16, 
    'x_count_Primes_nums__mutmut_17': x_count_Primes_nums__mutmut_17, 
    'x_count_Primes_nums__mutmut_18': x_count_Primes_nums__mutmut_18
}

def count_Primes_nums(*args, **kwargs):
    result = _mutmut_trampoline(x_count_Primes_nums__mutmut_orig, x_count_Primes_nums__mutmut_mutants, args, kwargs)
    return result 

count_Primes_nums.__signature__ = _mutmut_signature(x_count_Primes_nums__mutmut_orig)
x_count_Primes_nums__mutmut_orig.__name__ = 'x_count_Primes_nums'