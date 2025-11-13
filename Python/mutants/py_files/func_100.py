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
def x_frequency__mutmut_orig(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count += 1

    return count 
def x_frequency__mutmut_1(a,x): 
    count = None  
    for i in a: 
      if i == x: 
        count += 1

    return count 
def x_frequency__mutmut_2(a,x): 
    count = 1  
    for i in a: 
      if i == x: 
        count += 1

    return count 
def x_frequency__mutmut_3(a,x): 
    count = 0  
    for i in a: 
      if i != x: 
        count += 1

    return count 
def x_frequency__mutmut_4(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count = 1

    return count 
def x_frequency__mutmut_5(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count -= 1

    return count 
def x_frequency__mutmut_6(a,x): 
    count = 0  
    for i in a: 
      if i == x: 
        count += 2

    return count 

x_frequency__mutmut_mutants : ClassVar[MutantDict] = {
'x_frequency__mutmut_1': x_frequency__mutmut_1, 
    'x_frequency__mutmut_2': x_frequency__mutmut_2, 
    'x_frequency__mutmut_3': x_frequency__mutmut_3, 
    'x_frequency__mutmut_4': x_frequency__mutmut_4, 
    'x_frequency__mutmut_5': x_frequency__mutmut_5, 
    'x_frequency__mutmut_6': x_frequency__mutmut_6
}

def frequency(*args, **kwargs):
    result = _mutmut_trampoline(x_frequency__mutmut_orig, x_frequency__mutmut_mutants, args, kwargs)
    return result 

frequency.__signature__ = _mutmut_signature(x_frequency__mutmut_orig)
x_frequency__mutmut_orig.__name__ = 'x_frequency'