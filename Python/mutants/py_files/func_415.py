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
def x_sum_odd__mutmut_orig(n): 
    terms = (n + 1)//2
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_1(n): 
    terms = None
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_2(n): 
    terms = (n + 1) / 2
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_3(n): 
    terms = (n - 1)//2
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_4(n): 
    terms = (n + 2)//2
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_5(n): 
    terms = (n + 1)//3
    sum1 = terms * terms 
    return sum1  
def x_sum_odd__mutmut_6(n): 
    terms = (n + 1)//2
    sum1 = None 
    return sum1  
def x_sum_odd__mutmut_7(n): 
    terms = (n + 1)//2
    sum1 = terms / terms 
    return sum1  

x_sum_odd__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_odd__mutmut_1': x_sum_odd__mutmut_1, 
    'x_sum_odd__mutmut_2': x_sum_odd__mutmut_2, 
    'x_sum_odd__mutmut_3': x_sum_odd__mutmut_3, 
    'x_sum_odd__mutmut_4': x_sum_odd__mutmut_4, 
    'x_sum_odd__mutmut_5': x_sum_odd__mutmut_5, 
    'x_sum_odd__mutmut_6': x_sum_odd__mutmut_6, 
    'x_sum_odd__mutmut_7': x_sum_odd__mutmut_7
}

def sum_odd(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_odd__mutmut_orig, x_sum_odd__mutmut_mutants, args, kwargs)
    return result 

sum_odd.__signature__ = _mutmut_signature(x_sum_odd__mutmut_orig)
x_sum_odd__mutmut_orig.__name__ = 'x_sum_odd'
def x_sum_in_range__mutmut_orig(l,r): 
    return sum_odd(r) - sum_odd(l - 1)
def x_sum_in_range__mutmut_1(l,r): 
    return sum_odd(r) + sum_odd(l - 1)
def x_sum_in_range__mutmut_2(l,r): 
    return sum_odd(None) - sum_odd(l - 1)
def x_sum_in_range__mutmut_3(l,r): 
    return sum_odd(r) - sum_odd(None)
def x_sum_in_range__mutmut_4(l,r): 
    return sum_odd(r) - sum_odd(l + 1)
def x_sum_in_range__mutmut_5(l,r): 
    return sum_odd(r) - sum_odd(l - 2)

x_sum_in_range__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_in_range__mutmut_1': x_sum_in_range__mutmut_1, 
    'x_sum_in_range__mutmut_2': x_sum_in_range__mutmut_2, 
    'x_sum_in_range__mutmut_3': x_sum_in_range__mutmut_3, 
    'x_sum_in_range__mutmut_4': x_sum_in_range__mutmut_4, 
    'x_sum_in_range__mutmut_5': x_sum_in_range__mutmut_5
}

def sum_in_range(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_in_range__mutmut_orig, x_sum_in_range__mutmut_mutants, args, kwargs)
    return result 

sum_in_range.__signature__ = _mutmut_signature(x_sum_in_range__mutmut_orig)
x_sum_in_range__mutmut_orig.__name__ = 'x_sum_in_range'