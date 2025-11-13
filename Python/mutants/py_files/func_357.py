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
def x_sum_Of_Subarray_Prod__mutmut_orig(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_1(arr):
    ans = None
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_2(arr):
    ans = 1
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_3(arr):
    ans = 0
    res = None
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_4(arr):
    ans = 0
    res = 1
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_5(arr):
    ans = 0
    res = 0
    i = None
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_6(arr):
    ans = 0
    res = 0
    i = len(arr) + 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_7(arr):
    ans = 0
    res = 0
    i = len(arr) - 2
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_8(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i > 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_9(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 1):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_10(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = None
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_11(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i] / (1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_12(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 - res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_13(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(2 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_14(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans = incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_15(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans -= incr
        res = incr
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_16(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = None
        i -= 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_17(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i = 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_18(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i += 1
    return (ans)
def x_sum_Of_Subarray_Prod__mutmut_19(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 2
    return (ans)

x_sum_Of_Subarray_Prod__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_Of_Subarray_Prod__mutmut_1': x_sum_Of_Subarray_Prod__mutmut_1, 
    'x_sum_Of_Subarray_Prod__mutmut_2': x_sum_Of_Subarray_Prod__mutmut_2, 
    'x_sum_Of_Subarray_Prod__mutmut_3': x_sum_Of_Subarray_Prod__mutmut_3, 
    'x_sum_Of_Subarray_Prod__mutmut_4': x_sum_Of_Subarray_Prod__mutmut_4, 
    'x_sum_Of_Subarray_Prod__mutmut_5': x_sum_Of_Subarray_Prod__mutmut_5, 
    'x_sum_Of_Subarray_Prod__mutmut_6': x_sum_Of_Subarray_Prod__mutmut_6, 
    'x_sum_Of_Subarray_Prod__mutmut_7': x_sum_Of_Subarray_Prod__mutmut_7, 
    'x_sum_Of_Subarray_Prod__mutmut_8': x_sum_Of_Subarray_Prod__mutmut_8, 
    'x_sum_Of_Subarray_Prod__mutmut_9': x_sum_Of_Subarray_Prod__mutmut_9, 
    'x_sum_Of_Subarray_Prod__mutmut_10': x_sum_Of_Subarray_Prod__mutmut_10, 
    'x_sum_Of_Subarray_Prod__mutmut_11': x_sum_Of_Subarray_Prod__mutmut_11, 
    'x_sum_Of_Subarray_Prod__mutmut_12': x_sum_Of_Subarray_Prod__mutmut_12, 
    'x_sum_Of_Subarray_Prod__mutmut_13': x_sum_Of_Subarray_Prod__mutmut_13, 
    'x_sum_Of_Subarray_Prod__mutmut_14': x_sum_Of_Subarray_Prod__mutmut_14, 
    'x_sum_Of_Subarray_Prod__mutmut_15': x_sum_Of_Subarray_Prod__mutmut_15, 
    'x_sum_Of_Subarray_Prod__mutmut_16': x_sum_Of_Subarray_Prod__mutmut_16, 
    'x_sum_Of_Subarray_Prod__mutmut_17': x_sum_Of_Subarray_Prod__mutmut_17, 
    'x_sum_Of_Subarray_Prod__mutmut_18': x_sum_Of_Subarray_Prod__mutmut_18, 
    'x_sum_Of_Subarray_Prod__mutmut_19': x_sum_Of_Subarray_Prod__mutmut_19
}

def sum_Of_Subarray_Prod(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_Of_Subarray_Prod__mutmut_orig, x_sum_Of_Subarray_Prod__mutmut_mutants, args, kwargs)
    return result 

sum_Of_Subarray_Prod.__signature__ = _mutmut_signature(x_sum_Of_Subarray_Prod__mutmut_orig)
x_sum_Of_Subarray_Prod__mutmut_orig.__name__ = 'x_sum_Of_Subarray_Prod'