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
def x_binomial_Coeff__mutmut_orig(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_1(n,k): 
    C = None; 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_2(n,k): 
    C = [0] / (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_3(n,k): 
    C = [1] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_4(n,k): 
    C = [0] * (k - 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_5(n,k): 
    C = [0] * (k + 2); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_6(n,k): 
    C = [0] * (k + 1); 
    C[0] = None; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_7(n,k): 
    C = [0] * (k + 1); 
    C[1] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_8(n,k): 
    C = [0] * (k + 1); 
    C[0] = 2; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_9(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(None,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_10(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,None):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_11(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_12(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_13(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(2,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_14(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n - 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_15(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 2):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_16(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(None,0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_17(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),None,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_18(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,None): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_19(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_20(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_21(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_22(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(None, k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_23(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, None),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_24(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(k),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_25(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, ),0,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_26(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),1,-1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_27(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,+1): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_28(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-2): 
            C[j] = C[j] + C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_29(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = None; 
    return C[k]; 
def x_binomial_Coeff__mutmut_30(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] - C[j - 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_31(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j + 1]; 
    return C[k]; 
def x_binomial_Coeff__mutmut_32(n,k): 
    C = [0] * (k + 1); 
    C[0] = 1; # nC0 is 1 
    for i in range(1,n + 1):  
        for j in range(min(i, k),0,-1): 
            C[j] = C[j] + C[j - 2]; 
    return C[k]; 

x_binomial_Coeff__mutmut_mutants : ClassVar[MutantDict] = {
'x_binomial_Coeff__mutmut_1': x_binomial_Coeff__mutmut_1, 
    'x_binomial_Coeff__mutmut_2': x_binomial_Coeff__mutmut_2, 
    'x_binomial_Coeff__mutmut_3': x_binomial_Coeff__mutmut_3, 
    'x_binomial_Coeff__mutmut_4': x_binomial_Coeff__mutmut_4, 
    'x_binomial_Coeff__mutmut_5': x_binomial_Coeff__mutmut_5, 
    'x_binomial_Coeff__mutmut_6': x_binomial_Coeff__mutmut_6, 
    'x_binomial_Coeff__mutmut_7': x_binomial_Coeff__mutmut_7, 
    'x_binomial_Coeff__mutmut_8': x_binomial_Coeff__mutmut_8, 
    'x_binomial_Coeff__mutmut_9': x_binomial_Coeff__mutmut_9, 
    'x_binomial_Coeff__mutmut_10': x_binomial_Coeff__mutmut_10, 
    'x_binomial_Coeff__mutmut_11': x_binomial_Coeff__mutmut_11, 
    'x_binomial_Coeff__mutmut_12': x_binomial_Coeff__mutmut_12, 
    'x_binomial_Coeff__mutmut_13': x_binomial_Coeff__mutmut_13, 
    'x_binomial_Coeff__mutmut_14': x_binomial_Coeff__mutmut_14, 
    'x_binomial_Coeff__mutmut_15': x_binomial_Coeff__mutmut_15, 
    'x_binomial_Coeff__mutmut_16': x_binomial_Coeff__mutmut_16, 
    'x_binomial_Coeff__mutmut_17': x_binomial_Coeff__mutmut_17, 
    'x_binomial_Coeff__mutmut_18': x_binomial_Coeff__mutmut_18, 
    'x_binomial_Coeff__mutmut_19': x_binomial_Coeff__mutmut_19, 
    'x_binomial_Coeff__mutmut_20': x_binomial_Coeff__mutmut_20, 
    'x_binomial_Coeff__mutmut_21': x_binomial_Coeff__mutmut_21, 
    'x_binomial_Coeff__mutmut_22': x_binomial_Coeff__mutmut_22, 
    'x_binomial_Coeff__mutmut_23': x_binomial_Coeff__mutmut_23, 
    'x_binomial_Coeff__mutmut_24': x_binomial_Coeff__mutmut_24, 
    'x_binomial_Coeff__mutmut_25': x_binomial_Coeff__mutmut_25, 
    'x_binomial_Coeff__mutmut_26': x_binomial_Coeff__mutmut_26, 
    'x_binomial_Coeff__mutmut_27': x_binomial_Coeff__mutmut_27, 
    'x_binomial_Coeff__mutmut_28': x_binomial_Coeff__mutmut_28, 
    'x_binomial_Coeff__mutmut_29': x_binomial_Coeff__mutmut_29, 
    'x_binomial_Coeff__mutmut_30': x_binomial_Coeff__mutmut_30, 
    'x_binomial_Coeff__mutmut_31': x_binomial_Coeff__mutmut_31, 
    'x_binomial_Coeff__mutmut_32': x_binomial_Coeff__mutmut_32
}

def binomial_Coeff(*args, **kwargs):
    result = _mutmut_trampoline(x_binomial_Coeff__mutmut_orig, x_binomial_Coeff__mutmut_mutants, args, kwargs)
    return result 

binomial_Coeff.__signature__ = _mutmut_signature(x_binomial_Coeff__mutmut_orig)
x_binomial_Coeff__mutmut_orig.__name__ = 'x_binomial_Coeff'
def x_sum_Of_product__mutmut_orig(n): 
    return binomial_Coeff(2 * n,n - 1); 
def x_sum_Of_product__mutmut_1(n): 
    return binomial_Coeff(None,n - 1); 
def x_sum_Of_product__mutmut_2(n): 
    return binomial_Coeff(2 * n,None); 
def x_sum_Of_product__mutmut_3(n): 
    return binomial_Coeff(n - 1); 
def x_sum_Of_product__mutmut_4(n): 
    return binomial_Coeff(2 * n,); 
def x_sum_Of_product__mutmut_5(n): 
    return binomial_Coeff(2 / n,n - 1); 
def x_sum_Of_product__mutmut_6(n): 
    return binomial_Coeff(3 * n,n - 1); 
def x_sum_Of_product__mutmut_7(n): 
    return binomial_Coeff(2 * n,n + 1); 
def x_sum_Of_product__mutmut_8(n): 
    return binomial_Coeff(2 * n,n - 2); 

x_sum_Of_product__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_Of_product__mutmut_1': x_sum_Of_product__mutmut_1, 
    'x_sum_Of_product__mutmut_2': x_sum_Of_product__mutmut_2, 
    'x_sum_Of_product__mutmut_3': x_sum_Of_product__mutmut_3, 
    'x_sum_Of_product__mutmut_4': x_sum_Of_product__mutmut_4, 
    'x_sum_Of_product__mutmut_5': x_sum_Of_product__mutmut_5, 
    'x_sum_Of_product__mutmut_6': x_sum_Of_product__mutmut_6, 
    'x_sum_Of_product__mutmut_7': x_sum_Of_product__mutmut_7, 
    'x_sum_Of_product__mutmut_8': x_sum_Of_product__mutmut_8
}

def sum_Of_product(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_Of_product__mutmut_orig, x_sum_Of_product__mutmut_mutants, args, kwargs)
    return result 

sum_Of_product.__signature__ = _mutmut_signature(x_sum_Of_product__mutmut_orig)
x_sum_Of_product__mutmut_orig.__name__ = 'x_sum_Of_product'