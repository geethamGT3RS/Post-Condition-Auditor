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
def x_Split__mutmut_orig(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_1(list): 
    od_li = None 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_2(list): 
    od_li = [] 
    for i in list: 
        if (i / 2 != 0): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_3(list): 
    od_li = [] 
    for i in list: 
        if (i % 3 != 0): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_4(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 == 0): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_5(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 != 1): 
            od_li.append(i)  
    return od_li
def x_Split__mutmut_6(list): 
    od_li = [] 
    for i in list: 
        if (i % 2 != 0): 
            od_li.append(None)  
    return od_li

x_Split__mutmut_mutants : ClassVar[MutantDict] = {
'x_Split__mutmut_1': x_Split__mutmut_1, 
    'x_Split__mutmut_2': x_Split__mutmut_2, 
    'x_Split__mutmut_3': x_Split__mutmut_3, 
    'x_Split__mutmut_4': x_Split__mutmut_4, 
    'x_Split__mutmut_5': x_Split__mutmut_5, 
    'x_Split__mutmut_6': x_Split__mutmut_6
}

def Split(*args, **kwargs):
    result = _mutmut_trampoline(x_Split__mutmut_orig, x_Split__mutmut_mutants, args, kwargs)
    return result 

Split.__signature__ = _mutmut_signature(x_Split__mutmut_orig)
x_Split__mutmut_orig.__name__ = 'x_Split'