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
def x_difference__mutmut_orig(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_1(n) :  
    S = None;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_2(n) :  
    S = (n*(n + 1)) / 2;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_3(n) :  
    S = (n / (n + 1))//2;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_4(n) :  
    S = (n*(n - 1))//2;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_5(n) :  
    S = (n*(n + 2))//2;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_6(n) :  
    S = (n*(n + 1))//3;  
    res = S*(S-1);  
    return res;  
def x_difference__mutmut_7(n) :  
    S = (n*(n + 1))//2;  
    res = None;  
    return res;  
def x_difference__mutmut_8(n) :  
    S = (n*(n + 1))//2;  
    res = S / (S-1);  
    return res;  
def x_difference__mutmut_9(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S + 1);  
    return res;  
def x_difference__mutmut_10(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-2);  
    return res;  

x_difference__mutmut_mutants : ClassVar[MutantDict] = {
'x_difference__mutmut_1': x_difference__mutmut_1, 
    'x_difference__mutmut_2': x_difference__mutmut_2, 
    'x_difference__mutmut_3': x_difference__mutmut_3, 
    'x_difference__mutmut_4': x_difference__mutmut_4, 
    'x_difference__mutmut_5': x_difference__mutmut_5, 
    'x_difference__mutmut_6': x_difference__mutmut_6, 
    'x_difference__mutmut_7': x_difference__mutmut_7, 
    'x_difference__mutmut_8': x_difference__mutmut_8, 
    'x_difference__mutmut_9': x_difference__mutmut_9, 
    'x_difference__mutmut_10': x_difference__mutmut_10
}

def difference(*args, **kwargs):
    result = _mutmut_trampoline(x_difference__mutmut_orig, x_difference__mutmut_mutants, args, kwargs)
    return result 

difference.__signature__ = _mutmut_signature(x_difference__mutmut_orig)
x_difference__mutmut_orig.__name__ = 'x_difference'