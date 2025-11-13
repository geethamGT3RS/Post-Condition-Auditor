from array import array
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
def x_zero_count__mutmut_orig(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_1(nums):
    n = None
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_2(nums):
    n = len(nums)
    n1 = None
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_3(nums):
    n = len(nums)
    n1 = 1
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_4(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x != 0:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_5(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 1:
            n1 += 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_6(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 = 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_7(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 -= 1
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_8(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 2
        else:
          None
    return n1/(n-n1)
def x_zero_count__mutmut_9(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1 * (n-n1)
def x_zero_count__mutmut_10(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x == 0:
            n1 += 1
        else:
          None
    return n1/(n + n1)

x_zero_count__mutmut_mutants : ClassVar[MutantDict] = {
'x_zero_count__mutmut_1': x_zero_count__mutmut_1, 
    'x_zero_count__mutmut_2': x_zero_count__mutmut_2, 
    'x_zero_count__mutmut_3': x_zero_count__mutmut_3, 
    'x_zero_count__mutmut_4': x_zero_count__mutmut_4, 
    'x_zero_count__mutmut_5': x_zero_count__mutmut_5, 
    'x_zero_count__mutmut_6': x_zero_count__mutmut_6, 
    'x_zero_count__mutmut_7': x_zero_count__mutmut_7, 
    'x_zero_count__mutmut_8': x_zero_count__mutmut_8, 
    'x_zero_count__mutmut_9': x_zero_count__mutmut_9, 
    'x_zero_count__mutmut_10': x_zero_count__mutmut_10
}

def zero_count(*args, **kwargs):
    result = _mutmut_trampoline(x_zero_count__mutmut_orig, x_zero_count__mutmut_mutants, args, kwargs)
    return result 

zero_count.__signature__ = _mutmut_signature(x_zero_count__mutmut_orig)
x_zero_count__mutmut_orig.__name__ = 'x_zero_count'