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
def x_max_Product__mutmut_orig(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_1(arr): 
    arr_len = None 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_2(arr): 
    arr_len = len(arr) 
    if (arr_len <= 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_3(arr): 
    arr_len = len(arr) 
    if (arr_len < 3): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_4(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("XXNo pairs existsXX")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_5(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("no pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_6(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("NO PAIRS EXISTS")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_7(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = None; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_8(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[1]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_9(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = None      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_10(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[2]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_11(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(None,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_12(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,None): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_13(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_14(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_15(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(1,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_16(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(None,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_17(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,None): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_18(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_19(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_20(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i - 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_21(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 2,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_22(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] / arr[j] > x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_23(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] >= x * y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_24(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x / y): 
                x = arr[i]; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_25(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = None; y = arr[j] 
    return x,y    
def x_max_Product__mutmut_26(arr): 
    arr_len = len(arr) 
    if (arr_len < 2): 
        return ("No pairs exists")           
    x = arr[0]; y = arr[1]      
    for i in range(0,arr_len): 
        for j in range(i + 1,arr_len): 
            if (arr[i] * arr[j] > x * y): 
                x = arr[i]; y = None 
    return x,y    

x_max_Product__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_Product__mutmut_1': x_max_Product__mutmut_1, 
    'x_max_Product__mutmut_2': x_max_Product__mutmut_2, 
    'x_max_Product__mutmut_3': x_max_Product__mutmut_3, 
    'x_max_Product__mutmut_4': x_max_Product__mutmut_4, 
    'x_max_Product__mutmut_5': x_max_Product__mutmut_5, 
    'x_max_Product__mutmut_6': x_max_Product__mutmut_6, 
    'x_max_Product__mutmut_7': x_max_Product__mutmut_7, 
    'x_max_Product__mutmut_8': x_max_Product__mutmut_8, 
    'x_max_Product__mutmut_9': x_max_Product__mutmut_9, 
    'x_max_Product__mutmut_10': x_max_Product__mutmut_10, 
    'x_max_Product__mutmut_11': x_max_Product__mutmut_11, 
    'x_max_Product__mutmut_12': x_max_Product__mutmut_12, 
    'x_max_Product__mutmut_13': x_max_Product__mutmut_13, 
    'x_max_Product__mutmut_14': x_max_Product__mutmut_14, 
    'x_max_Product__mutmut_15': x_max_Product__mutmut_15, 
    'x_max_Product__mutmut_16': x_max_Product__mutmut_16, 
    'x_max_Product__mutmut_17': x_max_Product__mutmut_17, 
    'x_max_Product__mutmut_18': x_max_Product__mutmut_18, 
    'x_max_Product__mutmut_19': x_max_Product__mutmut_19, 
    'x_max_Product__mutmut_20': x_max_Product__mutmut_20, 
    'x_max_Product__mutmut_21': x_max_Product__mutmut_21, 
    'x_max_Product__mutmut_22': x_max_Product__mutmut_22, 
    'x_max_Product__mutmut_23': x_max_Product__mutmut_23, 
    'x_max_Product__mutmut_24': x_max_Product__mutmut_24, 
    'x_max_Product__mutmut_25': x_max_Product__mutmut_25, 
    'x_max_Product__mutmut_26': x_max_Product__mutmut_26
}

def max_Product(*args, **kwargs):
    result = _mutmut_trampoline(x_max_Product__mutmut_orig, x_max_Product__mutmut_mutants, args, kwargs)
    return result 

max_Product.__signature__ = _mutmut_signature(x_max_Product__mutmut_orig)
x_max_Product__mutmut_orig.__name__ = 'x_max_Product'