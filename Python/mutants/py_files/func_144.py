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
def x_sum_even_and_even_index__mutmut_orig(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_1(arr):  
    i = None
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_2(arr):  
    i = 1
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_3(arr):  
    i = 0
    sum = None
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_4(arr):  
    i = 0
    sum = 1
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_5(arr):  
    i = 0
    sum = 0
    for i in range(None, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_6(arr):  
    i = 0
    sum = 0
    for i in range(0, None,2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_7(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),None): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_8(arr):  
    i = 0
    sum = 0
    for i in range(len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_9(arr):  
    i = 0
    sum = 0
    for i in range(0, 2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_10(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_11(arr):  
    i = 0
    sum = 0
    for i in range(1, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_12(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),3): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_13(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] / 2 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_14(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 3 == 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_15(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 != 0) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_16(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 1) : 
            sum += arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_17(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum = arr[i]  
    return sum
def x_sum_even_and_even_index__mutmut_18(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum -= arr[i]  
    return sum

x_sum_even_and_even_index__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_even_and_even_index__mutmut_1': x_sum_even_and_even_index__mutmut_1, 
    'x_sum_even_and_even_index__mutmut_2': x_sum_even_and_even_index__mutmut_2, 
    'x_sum_even_and_even_index__mutmut_3': x_sum_even_and_even_index__mutmut_3, 
    'x_sum_even_and_even_index__mutmut_4': x_sum_even_and_even_index__mutmut_4, 
    'x_sum_even_and_even_index__mutmut_5': x_sum_even_and_even_index__mutmut_5, 
    'x_sum_even_and_even_index__mutmut_6': x_sum_even_and_even_index__mutmut_6, 
    'x_sum_even_and_even_index__mutmut_7': x_sum_even_and_even_index__mutmut_7, 
    'x_sum_even_and_even_index__mutmut_8': x_sum_even_and_even_index__mutmut_8, 
    'x_sum_even_and_even_index__mutmut_9': x_sum_even_and_even_index__mutmut_9, 
    'x_sum_even_and_even_index__mutmut_10': x_sum_even_and_even_index__mutmut_10, 
    'x_sum_even_and_even_index__mutmut_11': x_sum_even_and_even_index__mutmut_11, 
    'x_sum_even_and_even_index__mutmut_12': x_sum_even_and_even_index__mutmut_12, 
    'x_sum_even_and_even_index__mutmut_13': x_sum_even_and_even_index__mutmut_13, 
    'x_sum_even_and_even_index__mutmut_14': x_sum_even_and_even_index__mutmut_14, 
    'x_sum_even_and_even_index__mutmut_15': x_sum_even_and_even_index__mutmut_15, 
    'x_sum_even_and_even_index__mutmut_16': x_sum_even_and_even_index__mutmut_16, 
    'x_sum_even_and_even_index__mutmut_17': x_sum_even_and_even_index__mutmut_17, 
    'x_sum_even_and_even_index__mutmut_18': x_sum_even_and_even_index__mutmut_18
}

def sum_even_and_even_index(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_even_and_even_index__mutmut_orig, x_sum_even_and_even_index__mutmut_mutants, args, kwargs)
    return result 

sum_even_and_even_index.__signature__ = _mutmut_signature(x_sum_even_and_even_index__mutmut_orig)
x_sum_even_and_even_index__mutmut_orig.__name__ = 'x_sum_even_and_even_index'