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
def x_unique_sublists__mutmut_orig(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_1(list1):
    result =None
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_2(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(None) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_3(list1):
    result ={}
    for l in list1: 
        result.setdefault(None, list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_4(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), None).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_5(list1):
    result ={}
    for l in list1: 
        result.setdefault(list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_6(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), ).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_7(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(None), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_8(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(2) 
    for a, b in result.items(): 
        result[a] = sum(b)
    return result
def x_unique_sublists__mutmut_9(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = None
    return result
def x_unique_sublists__mutmut_10(list1):
    result ={}
    for l in list1: 
        result.setdefault(tuple(l), list()).append(1) 
    for a, b in result.items(): 
        result[a] = sum(None)
    return result

x_unique_sublists__mutmut_mutants : ClassVar[MutantDict] = {
'x_unique_sublists__mutmut_1': x_unique_sublists__mutmut_1, 
    'x_unique_sublists__mutmut_2': x_unique_sublists__mutmut_2, 
    'x_unique_sublists__mutmut_3': x_unique_sublists__mutmut_3, 
    'x_unique_sublists__mutmut_4': x_unique_sublists__mutmut_4, 
    'x_unique_sublists__mutmut_5': x_unique_sublists__mutmut_5, 
    'x_unique_sublists__mutmut_6': x_unique_sublists__mutmut_6, 
    'x_unique_sublists__mutmut_7': x_unique_sublists__mutmut_7, 
    'x_unique_sublists__mutmut_8': x_unique_sublists__mutmut_8, 
    'x_unique_sublists__mutmut_9': x_unique_sublists__mutmut_9, 
    'x_unique_sublists__mutmut_10': x_unique_sublists__mutmut_10
}

def unique_sublists(*args, **kwargs):
    result = _mutmut_trampoline(x_unique_sublists__mutmut_orig, x_unique_sublists__mutmut_mutants, args, kwargs)
    return result 

unique_sublists.__signature__ = _mutmut_signature(x_unique_sublists__mutmut_orig)
x_unique_sublists__mutmut_orig.__name__ = 'x_unique_sublists'