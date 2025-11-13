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
def x_last__mutmut_orig(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_1(arr,x):
    n = None
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_2(arr,x):
    n = len(arr)
    low = None
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_3(arr,x):
    n = len(arr)
    low = 1
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_4(arr,x):
    n = len(arr)
    low = 0
    high = None
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_5(arr,x):
    n = len(arr)
    low = 0
    high = n + 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_6(arr,x):
    n = len(arr)
    low = 0
    high = n - 2
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_7(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = None  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_8(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = +1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_9(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -2  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_10(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low < high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_11(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = None 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_12(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) / 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_13(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low - high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_14(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 3 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_15(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] >= x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_16(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = None
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_17(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_18(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 2
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_19(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] <= x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_20(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = None
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_21(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid - 1
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_22(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 2
        else:
            res = mid
            low = mid + 1
    return res
def x_last__mutmut_23(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = None
            low = mid + 1
    return res
def x_last__mutmut_24(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = None
    return res
def x_last__mutmut_25(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid - 1
    return res
def x_last__mutmut_26(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 2
    return res

x_last__mutmut_mutants : ClassVar[MutantDict] = {
'x_last__mutmut_1': x_last__mutmut_1, 
    'x_last__mutmut_2': x_last__mutmut_2, 
    'x_last__mutmut_3': x_last__mutmut_3, 
    'x_last__mutmut_4': x_last__mutmut_4, 
    'x_last__mutmut_5': x_last__mutmut_5, 
    'x_last__mutmut_6': x_last__mutmut_6, 
    'x_last__mutmut_7': x_last__mutmut_7, 
    'x_last__mutmut_8': x_last__mutmut_8, 
    'x_last__mutmut_9': x_last__mutmut_9, 
    'x_last__mutmut_10': x_last__mutmut_10, 
    'x_last__mutmut_11': x_last__mutmut_11, 
    'x_last__mutmut_12': x_last__mutmut_12, 
    'x_last__mutmut_13': x_last__mutmut_13, 
    'x_last__mutmut_14': x_last__mutmut_14, 
    'x_last__mutmut_15': x_last__mutmut_15, 
    'x_last__mutmut_16': x_last__mutmut_16, 
    'x_last__mutmut_17': x_last__mutmut_17, 
    'x_last__mutmut_18': x_last__mutmut_18, 
    'x_last__mutmut_19': x_last__mutmut_19, 
    'x_last__mutmut_20': x_last__mutmut_20, 
    'x_last__mutmut_21': x_last__mutmut_21, 
    'x_last__mutmut_22': x_last__mutmut_22, 
    'x_last__mutmut_23': x_last__mutmut_23, 
    'x_last__mutmut_24': x_last__mutmut_24, 
    'x_last__mutmut_25': x_last__mutmut_25, 
    'x_last__mutmut_26': x_last__mutmut_26
}

def last(*args, **kwargs):
    result = _mutmut_trampoline(x_last__mutmut_orig, x_last__mutmut_mutants, args, kwargs)
    return result 

last.__signature__ = _mutmut_signature(x_last__mutmut_orig)
x_last__mutmut_orig.__name__ = 'x_last'