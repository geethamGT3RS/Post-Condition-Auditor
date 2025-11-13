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
def x_swap_List__mutmut_orig(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_1(newList): 
    size = None 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_2(newList): 
    size = len(newList) 
    temp = None 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_3(newList): 
    size = len(newList) 
    temp = newList[1] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_4(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = None 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_5(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[1] = newList[size - 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_6(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size + 1] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_7(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 2] 
    newList[size - 1] = temp   
    return newList 
def x_swap_List__mutmut_8(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 1] = None   
    return newList 
def x_swap_List__mutmut_9(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size + 1] = temp   
    return newList 
def x_swap_List__mutmut_10(newList): 
    size = len(newList) 
    temp = newList[0] 
    newList[0] = newList[size - 1] 
    newList[size - 2] = temp   
    return newList 

x_swap_List__mutmut_mutants : ClassVar[MutantDict] = {
'x_swap_List__mutmut_1': x_swap_List__mutmut_1, 
    'x_swap_List__mutmut_2': x_swap_List__mutmut_2, 
    'x_swap_List__mutmut_3': x_swap_List__mutmut_3, 
    'x_swap_List__mutmut_4': x_swap_List__mutmut_4, 
    'x_swap_List__mutmut_5': x_swap_List__mutmut_5, 
    'x_swap_List__mutmut_6': x_swap_List__mutmut_6, 
    'x_swap_List__mutmut_7': x_swap_List__mutmut_7, 
    'x_swap_List__mutmut_8': x_swap_List__mutmut_8, 
    'x_swap_List__mutmut_9': x_swap_List__mutmut_9, 
    'x_swap_List__mutmut_10': x_swap_List__mutmut_10
}

def swap_List(*args, **kwargs):
    result = _mutmut_trampoline(x_swap_List__mutmut_orig, x_swap_List__mutmut_mutants, args, kwargs)
    return result 

swap_List.__signature__ = _mutmut_signature(x_swap_List__mutmut_orig)
x_swap_List__mutmut_orig.__name__ = 'x_swap_List'