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
def x_get_Inv_Count__mutmut_orig(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_1(arr): 
    inv_count = None
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_2(arr): 
    inv_count = 1
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_3(arr): 
    inv_count = 0
    for i in range(None): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_4(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(None, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_5(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, None): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_6(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_7(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, ): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_8(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i - 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_9(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 2, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_10(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] >= arr[j]): 
                inv_count += 1
    return inv_count 
def x_get_Inv_Count__mutmut_11(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count = 1
    return inv_count 
def x_get_Inv_Count__mutmut_12(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count -= 1
    return inv_count 
def x_get_Inv_Count__mutmut_13(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 2
    return inv_count 

x_get_Inv_Count__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_Inv_Count__mutmut_1': x_get_Inv_Count__mutmut_1, 
    'x_get_Inv_Count__mutmut_2': x_get_Inv_Count__mutmut_2, 
    'x_get_Inv_Count__mutmut_3': x_get_Inv_Count__mutmut_3, 
    'x_get_Inv_Count__mutmut_4': x_get_Inv_Count__mutmut_4, 
    'x_get_Inv_Count__mutmut_5': x_get_Inv_Count__mutmut_5, 
    'x_get_Inv_Count__mutmut_6': x_get_Inv_Count__mutmut_6, 
    'x_get_Inv_Count__mutmut_7': x_get_Inv_Count__mutmut_7, 
    'x_get_Inv_Count__mutmut_8': x_get_Inv_Count__mutmut_8, 
    'x_get_Inv_Count__mutmut_9': x_get_Inv_Count__mutmut_9, 
    'x_get_Inv_Count__mutmut_10': x_get_Inv_Count__mutmut_10, 
    'x_get_Inv_Count__mutmut_11': x_get_Inv_Count__mutmut_11, 
    'x_get_Inv_Count__mutmut_12': x_get_Inv_Count__mutmut_12, 
    'x_get_Inv_Count__mutmut_13': x_get_Inv_Count__mutmut_13
}

def get_Inv_Count(*args, **kwargs):
    result = _mutmut_trampoline(x_get_Inv_Count__mutmut_orig, x_get_Inv_Count__mutmut_mutants, args, kwargs)
    return result 

get_Inv_Count.__signature__ = _mutmut_signature(x_get_Inv_Count__mutmut_orig)
x_get_Inv_Count__mutmut_orig.__name__ = 'x_get_Inv_Count'