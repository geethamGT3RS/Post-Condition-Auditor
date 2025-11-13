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
def x_max_Abs_Diff__mutmut_orig(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_1(arr): 
    n = None
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_2(arr): 
    n = len(arr)
    minEle = None 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_3(arr): 
    n = len(arr)
    minEle = arr[1] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_4(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = None 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_5(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[1] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_6(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(None, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_7(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, None): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_8(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_9(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, ): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_10(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(2, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_11(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = None 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_12(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(None,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_13(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,None) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_14(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_15(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_16(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = None 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_17(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(None,arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_18(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,None) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_19(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(arr[i]) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_20(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,) 
    return (maxEle - minEle) 
def x_max_Abs_Diff__mutmut_21(arr): 
    n = len(arr)
    minEle = arr[0] 
    maxEle = arr[0] 
    for i in range(1, n): 
        minEle = min(minEle,arr[i]) 
        maxEle = max(maxEle,arr[i]) 
    return (maxEle + minEle) 

x_max_Abs_Diff__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_Abs_Diff__mutmut_1': x_max_Abs_Diff__mutmut_1, 
    'x_max_Abs_Diff__mutmut_2': x_max_Abs_Diff__mutmut_2, 
    'x_max_Abs_Diff__mutmut_3': x_max_Abs_Diff__mutmut_3, 
    'x_max_Abs_Diff__mutmut_4': x_max_Abs_Diff__mutmut_4, 
    'x_max_Abs_Diff__mutmut_5': x_max_Abs_Diff__mutmut_5, 
    'x_max_Abs_Diff__mutmut_6': x_max_Abs_Diff__mutmut_6, 
    'x_max_Abs_Diff__mutmut_7': x_max_Abs_Diff__mutmut_7, 
    'x_max_Abs_Diff__mutmut_8': x_max_Abs_Diff__mutmut_8, 
    'x_max_Abs_Diff__mutmut_9': x_max_Abs_Diff__mutmut_9, 
    'x_max_Abs_Diff__mutmut_10': x_max_Abs_Diff__mutmut_10, 
    'x_max_Abs_Diff__mutmut_11': x_max_Abs_Diff__mutmut_11, 
    'x_max_Abs_Diff__mutmut_12': x_max_Abs_Diff__mutmut_12, 
    'x_max_Abs_Diff__mutmut_13': x_max_Abs_Diff__mutmut_13, 
    'x_max_Abs_Diff__mutmut_14': x_max_Abs_Diff__mutmut_14, 
    'x_max_Abs_Diff__mutmut_15': x_max_Abs_Diff__mutmut_15, 
    'x_max_Abs_Diff__mutmut_16': x_max_Abs_Diff__mutmut_16, 
    'x_max_Abs_Diff__mutmut_17': x_max_Abs_Diff__mutmut_17, 
    'x_max_Abs_Diff__mutmut_18': x_max_Abs_Diff__mutmut_18, 
    'x_max_Abs_Diff__mutmut_19': x_max_Abs_Diff__mutmut_19, 
    'x_max_Abs_Diff__mutmut_20': x_max_Abs_Diff__mutmut_20, 
    'x_max_Abs_Diff__mutmut_21': x_max_Abs_Diff__mutmut_21
}

def max_Abs_Diff(*args, **kwargs):
    result = _mutmut_trampoline(x_max_Abs_Diff__mutmut_orig, x_max_Abs_Diff__mutmut_mutants, args, kwargs)
    return result 

max_Abs_Diff.__signature__ = _mutmut_signature(x_max_Abs_Diff__mutmut_orig)
x_max_Abs_Diff__mutmut_orig.__name__ = 'x_max_Abs_Diff'