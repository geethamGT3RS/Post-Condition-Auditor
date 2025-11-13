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
def x_perfect_squares__mutmut_orig(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_1(a, b):
    lists=None
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_2(a, b):
    lists=[]
    for i in range (None,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_3(a, b):
    lists=[]
    for i in range (a,None):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_4(a, b):
    lists=[]
    for i in range (b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_5(a, b):
    lists=[]
    for i in range (a,):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_6(a, b):
    lists=[]
    for i in range (a,b - 1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_7(a, b):
    lists=[]
    for i in range (a,b+2):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_8(a, b):
    lists=[]
    for i in range (a,b+1):
        j = None;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_9(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 2;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_10(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j / j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_11(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j < i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_12(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j / j == i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_13(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j != i:
                 lists.append(i)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_14(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(None)  
            j = j+1
        i = i+1
    return lists
def x_perfect_squares__mutmut_15(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = None
        i = i+1
    return lists
def x_perfect_squares__mutmut_16(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j - 1
        i = i+1
    return lists
def x_perfect_squares__mutmut_17(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+2
        i = i+1
    return lists
def x_perfect_squares__mutmut_18(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = None
    return lists
def x_perfect_squares__mutmut_19(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i - 1
    return lists
def x_perfect_squares__mutmut_20(a, b):
    lists=[]
    for i in range (a,b+1):
        j = 1;
        while j*j <= i:
            if j*j == i:
                 lists.append(i)  
            j = j+1
        i = i+2
    return lists

x_perfect_squares__mutmut_mutants : ClassVar[MutantDict] = {
'x_perfect_squares__mutmut_1': x_perfect_squares__mutmut_1, 
    'x_perfect_squares__mutmut_2': x_perfect_squares__mutmut_2, 
    'x_perfect_squares__mutmut_3': x_perfect_squares__mutmut_3, 
    'x_perfect_squares__mutmut_4': x_perfect_squares__mutmut_4, 
    'x_perfect_squares__mutmut_5': x_perfect_squares__mutmut_5, 
    'x_perfect_squares__mutmut_6': x_perfect_squares__mutmut_6, 
    'x_perfect_squares__mutmut_7': x_perfect_squares__mutmut_7, 
    'x_perfect_squares__mutmut_8': x_perfect_squares__mutmut_8, 
    'x_perfect_squares__mutmut_9': x_perfect_squares__mutmut_9, 
    'x_perfect_squares__mutmut_10': x_perfect_squares__mutmut_10, 
    'x_perfect_squares__mutmut_11': x_perfect_squares__mutmut_11, 
    'x_perfect_squares__mutmut_12': x_perfect_squares__mutmut_12, 
    'x_perfect_squares__mutmut_13': x_perfect_squares__mutmut_13, 
    'x_perfect_squares__mutmut_14': x_perfect_squares__mutmut_14, 
    'x_perfect_squares__mutmut_15': x_perfect_squares__mutmut_15, 
    'x_perfect_squares__mutmut_16': x_perfect_squares__mutmut_16, 
    'x_perfect_squares__mutmut_17': x_perfect_squares__mutmut_17, 
    'x_perfect_squares__mutmut_18': x_perfect_squares__mutmut_18, 
    'x_perfect_squares__mutmut_19': x_perfect_squares__mutmut_19, 
    'x_perfect_squares__mutmut_20': x_perfect_squares__mutmut_20
}

def perfect_squares(*args, **kwargs):
    result = _mutmut_trampoline(x_perfect_squares__mutmut_orig, x_perfect_squares__mutmut_mutants, args, kwargs)
    return result 

perfect_squares.__signature__ = _mutmut_signature(x_perfect_squares__mutmut_orig)
x_perfect_squares__mutmut_orig.__name__ = 'x_perfect_squares'