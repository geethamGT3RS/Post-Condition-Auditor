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
def x_is_Sub_Array__mutmut_orig(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_1(A,B): 
    n = None
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_2(A,B): 
    n = len(A)
    m = None
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_3(A,B): 
    n = len(A)
    m = len(B)
    i = None; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_4(A,B): 
    n = len(A)
    m = len(B)
    i = 1; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_5(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = None; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_6(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 1; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_7(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n or j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_8(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i <= n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_9(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j <= m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_10(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] != B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_11(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i = 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_12(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i -= 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_13(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 2; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_14(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j = 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_15(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j -= 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_16(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 2; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_17(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j != m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_18(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return False;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_19(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = None; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_20(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j - 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_21(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i + j + 1; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_22(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 2; 
            j = 0;       
    return False; 
def x_is_Sub_Array__mutmut_23(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = None;       
    return False; 
def x_is_Sub_Array__mutmut_24(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 1;       
    return False; 
def x_is_Sub_Array__mutmut_25(A,B): 
    n = len(A)
    m = len(B)
    i = 0; j = 0; 
    while (i < n and j < m):  
        if (A[i] == B[j]): 
            i += 1; 
            j += 1; 
            if (j == m): 
                return True;  
        else: 
            i = i - j + 1; 
            j = 0;       
    return True; 

x_is_Sub_Array__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_Sub_Array__mutmut_1': x_is_Sub_Array__mutmut_1, 
    'x_is_Sub_Array__mutmut_2': x_is_Sub_Array__mutmut_2, 
    'x_is_Sub_Array__mutmut_3': x_is_Sub_Array__mutmut_3, 
    'x_is_Sub_Array__mutmut_4': x_is_Sub_Array__mutmut_4, 
    'x_is_Sub_Array__mutmut_5': x_is_Sub_Array__mutmut_5, 
    'x_is_Sub_Array__mutmut_6': x_is_Sub_Array__mutmut_6, 
    'x_is_Sub_Array__mutmut_7': x_is_Sub_Array__mutmut_7, 
    'x_is_Sub_Array__mutmut_8': x_is_Sub_Array__mutmut_8, 
    'x_is_Sub_Array__mutmut_9': x_is_Sub_Array__mutmut_9, 
    'x_is_Sub_Array__mutmut_10': x_is_Sub_Array__mutmut_10, 
    'x_is_Sub_Array__mutmut_11': x_is_Sub_Array__mutmut_11, 
    'x_is_Sub_Array__mutmut_12': x_is_Sub_Array__mutmut_12, 
    'x_is_Sub_Array__mutmut_13': x_is_Sub_Array__mutmut_13, 
    'x_is_Sub_Array__mutmut_14': x_is_Sub_Array__mutmut_14, 
    'x_is_Sub_Array__mutmut_15': x_is_Sub_Array__mutmut_15, 
    'x_is_Sub_Array__mutmut_16': x_is_Sub_Array__mutmut_16, 
    'x_is_Sub_Array__mutmut_17': x_is_Sub_Array__mutmut_17, 
    'x_is_Sub_Array__mutmut_18': x_is_Sub_Array__mutmut_18, 
    'x_is_Sub_Array__mutmut_19': x_is_Sub_Array__mutmut_19, 
    'x_is_Sub_Array__mutmut_20': x_is_Sub_Array__mutmut_20, 
    'x_is_Sub_Array__mutmut_21': x_is_Sub_Array__mutmut_21, 
    'x_is_Sub_Array__mutmut_22': x_is_Sub_Array__mutmut_22, 
    'x_is_Sub_Array__mutmut_23': x_is_Sub_Array__mutmut_23, 
    'x_is_Sub_Array__mutmut_24': x_is_Sub_Array__mutmut_24, 
    'x_is_Sub_Array__mutmut_25': x_is_Sub_Array__mutmut_25
}

def is_Sub_Array(*args, **kwargs):
    result = _mutmut_trampoline(x_is_Sub_Array__mutmut_orig, x_is_Sub_Array__mutmut_mutants, args, kwargs)
    return result 

is_Sub_Array.__signature__ = _mutmut_signature(x_is_Sub_Array__mutmut_orig)
x_is_Sub_Array__mutmut_orig.__name__ = 'x_is_Sub_Array'