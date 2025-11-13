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
def x_rev__mutmut_orig(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_1(num):    
    rev_num = None
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_2(num):    
    rev_num = 1
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_3(num):    
    rev_num = 0
    while (num >= 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_4(num):    
    rev_num = 0
    while (num > 1):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_5(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = None 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_6(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 - num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_7(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num / 10 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_8(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 11 + num % 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_9(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num / 10) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_10(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 11) 
        num = num // 10  
    return rev_num  
def x_rev__mutmut_11(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = None  
    return rev_num  
def x_rev__mutmut_12(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num / 10  
    return rev_num  
def x_rev__mutmut_13(num):    
    rev_num = 0
    while (num > 0):  
        rev_num = (rev_num * 10 + num % 10) 
        num = num // 11  
    return rev_num  

x_rev__mutmut_mutants : ClassVar[MutantDict] = {
'x_rev__mutmut_1': x_rev__mutmut_1, 
    'x_rev__mutmut_2': x_rev__mutmut_2, 
    'x_rev__mutmut_3': x_rev__mutmut_3, 
    'x_rev__mutmut_4': x_rev__mutmut_4, 
    'x_rev__mutmut_5': x_rev__mutmut_5, 
    'x_rev__mutmut_6': x_rev__mutmut_6, 
    'x_rev__mutmut_7': x_rev__mutmut_7, 
    'x_rev__mutmut_8': x_rev__mutmut_8, 
    'x_rev__mutmut_9': x_rev__mutmut_9, 
    'x_rev__mutmut_10': x_rev__mutmut_10, 
    'x_rev__mutmut_11': x_rev__mutmut_11, 
    'x_rev__mutmut_12': x_rev__mutmut_12, 
    'x_rev__mutmut_13': x_rev__mutmut_13
}

def rev(*args, **kwargs):
    result = _mutmut_trampoline(x_rev__mutmut_orig, x_rev__mutmut_mutants, args, kwargs)
    return result 

rev.__signature__ = _mutmut_signature(x_rev__mutmut_orig)
x_rev__mutmut_orig.__name__ = 'x_rev'
def x_check__mutmut_orig(n):    
    return (2 * rev(n) == n + 1)  
def x_check__mutmut_1(n):    
    return (2 / rev(n) == n + 1)  
def x_check__mutmut_2(n):    
    return (3 * rev(n) == n + 1)  
def x_check__mutmut_3(n):    
    return (2 * rev(None) == n + 1)  
def x_check__mutmut_4(n):    
    return (2 * rev(n) != n + 1)  
def x_check__mutmut_5(n):    
    return (2 * rev(n) == n - 1)  
def x_check__mutmut_6(n):    
    return (2 * rev(n) == n + 2)  

x_check__mutmut_mutants : ClassVar[MutantDict] = {
'x_check__mutmut_1': x_check__mutmut_1, 
    'x_check__mutmut_2': x_check__mutmut_2, 
    'x_check__mutmut_3': x_check__mutmut_3, 
    'x_check__mutmut_4': x_check__mutmut_4, 
    'x_check__mutmut_5': x_check__mutmut_5, 
    'x_check__mutmut_6': x_check__mutmut_6
}

def check(*args, **kwargs):
    result = _mutmut_trampoline(x_check__mutmut_orig, x_check__mutmut_mutants, args, kwargs)
    return result 

check.__signature__ = _mutmut_signature(x_check__mutmut_orig)
x_check__mutmut_orig.__name__ = 'x_check'