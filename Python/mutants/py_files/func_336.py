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
def x_pair_xor_Sum__mutmut_orig(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_1(arr,n) : 
    ans = None 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_2(arr,n) : 
    ans = 1 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_3(arr,n) : 
    ans = 0 
    for i in range(None,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_4(arr,n) : 
    ans = 0 
    for i in range(0,None) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_5(arr,n) : 
    ans = 0 
    for i in range(n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_6(arr,n) : 
    ans = 0 
    for i in range(0,) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_7(arr,n) : 
    ans = 0 
    for i in range(1,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_8(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(None,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_9(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,None) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_10(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_11(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_12(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i - 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_13(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 2,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_14(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = None          
    return ans 
def x_pair_xor_Sum__mutmut_15(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans - (arr[i] ^ arr[j])          
    return ans 
def x_pair_xor_Sum__mutmut_16(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] & arr[j])          
    return ans 

x_pair_xor_Sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_pair_xor_Sum__mutmut_1': x_pair_xor_Sum__mutmut_1, 
    'x_pair_xor_Sum__mutmut_2': x_pair_xor_Sum__mutmut_2, 
    'x_pair_xor_Sum__mutmut_3': x_pair_xor_Sum__mutmut_3, 
    'x_pair_xor_Sum__mutmut_4': x_pair_xor_Sum__mutmut_4, 
    'x_pair_xor_Sum__mutmut_5': x_pair_xor_Sum__mutmut_5, 
    'x_pair_xor_Sum__mutmut_6': x_pair_xor_Sum__mutmut_6, 
    'x_pair_xor_Sum__mutmut_7': x_pair_xor_Sum__mutmut_7, 
    'x_pair_xor_Sum__mutmut_8': x_pair_xor_Sum__mutmut_8, 
    'x_pair_xor_Sum__mutmut_9': x_pair_xor_Sum__mutmut_9, 
    'x_pair_xor_Sum__mutmut_10': x_pair_xor_Sum__mutmut_10, 
    'x_pair_xor_Sum__mutmut_11': x_pair_xor_Sum__mutmut_11, 
    'x_pair_xor_Sum__mutmut_12': x_pair_xor_Sum__mutmut_12, 
    'x_pair_xor_Sum__mutmut_13': x_pair_xor_Sum__mutmut_13, 
    'x_pair_xor_Sum__mutmut_14': x_pair_xor_Sum__mutmut_14, 
    'x_pair_xor_Sum__mutmut_15': x_pair_xor_Sum__mutmut_15, 
    'x_pair_xor_Sum__mutmut_16': x_pair_xor_Sum__mutmut_16
}

def pair_xor_Sum(*args, **kwargs):
    result = _mutmut_trampoline(x_pair_xor_Sum__mutmut_orig, x_pair_xor_Sum__mutmut_mutants, args, kwargs)
    return result 

pair_xor_Sum.__signature__ = _mutmut_signature(x_pair_xor_Sum__mutmut_orig)
x_pair_xor_Sum__mutmut_orig.__name__ = 'x_pair_xor_Sum'