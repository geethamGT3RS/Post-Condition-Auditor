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
def x_odd_length_sum__mutmut_orig(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_1(arr):
    Sum = None
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_2(arr):
    Sum = 1
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_3(arr):
    Sum = 0
    l = None
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_4(arr):
    Sum = 0
    l = len(arr)
    for i in range(None):
        Sum += ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_5(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum = ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_6(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum -= ((((i + 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_7(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 2) / arr[i])
    return Sum
def x_odd_length_sum__mutmut_8(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) / 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_9(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) - 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_10(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) / (l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_11(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i - 1) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_12(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 2) *(l - i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_13(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l + i) + 1) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_14(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 2) // 2) * arr[i])
    return Sum
def x_odd_length_sum__mutmut_15(arr):
    Sum = 0
    l = len(arr)
    for i in range(l):
        Sum += ((((i + 1) *(l - i) + 1) // 3) * arr[i])
    return Sum

x_odd_length_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_odd_length_sum__mutmut_1': x_odd_length_sum__mutmut_1, 
    'x_odd_length_sum__mutmut_2': x_odd_length_sum__mutmut_2, 
    'x_odd_length_sum__mutmut_3': x_odd_length_sum__mutmut_3, 
    'x_odd_length_sum__mutmut_4': x_odd_length_sum__mutmut_4, 
    'x_odd_length_sum__mutmut_5': x_odd_length_sum__mutmut_5, 
    'x_odd_length_sum__mutmut_6': x_odd_length_sum__mutmut_6, 
    'x_odd_length_sum__mutmut_7': x_odd_length_sum__mutmut_7, 
    'x_odd_length_sum__mutmut_8': x_odd_length_sum__mutmut_8, 
    'x_odd_length_sum__mutmut_9': x_odd_length_sum__mutmut_9, 
    'x_odd_length_sum__mutmut_10': x_odd_length_sum__mutmut_10, 
    'x_odd_length_sum__mutmut_11': x_odd_length_sum__mutmut_11, 
    'x_odd_length_sum__mutmut_12': x_odd_length_sum__mutmut_12, 
    'x_odd_length_sum__mutmut_13': x_odd_length_sum__mutmut_13, 
    'x_odd_length_sum__mutmut_14': x_odd_length_sum__mutmut_14, 
    'x_odd_length_sum__mutmut_15': x_odd_length_sum__mutmut_15
}

def odd_length_sum(*args, **kwargs):
    result = _mutmut_trampoline(x_odd_length_sum__mutmut_orig, x_odd_length_sum__mutmut_mutants, args, kwargs)
    return result 

odd_length_sum.__signature__ = _mutmut_signature(x_odd_length_sum__mutmut_orig)
x_odd_length_sum__mutmut_orig.__name__ = 'x_odd_length_sum'