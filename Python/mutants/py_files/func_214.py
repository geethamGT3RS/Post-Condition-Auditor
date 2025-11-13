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
def x_count_element_in_list__mutmut_orig(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr
def x_count_element_in_list__mutmut_1(list1, x): 
    ctr = None
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr
def x_count_element_in_list__mutmut_2(list1, x): 
    ctr = 1
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr
def x_count_element_in_list__mutmut_3(list1, x): 
    ctr = 0
    for i in range(None): 
        if x in list1[i]: 
            ctr+= 1          
    return ctr
def x_count_element_in_list__mutmut_4(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x not in list1[i]: 
            ctr+= 1          
    return ctr
def x_count_element_in_list__mutmut_5(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr = 1          
    return ctr
def x_count_element_in_list__mutmut_6(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr -= 1          
    return ctr
def x_count_element_in_list__mutmut_7(list1, x): 
    ctr = 0
    for i in range(len(list1)): 
        if x in list1[i]: 
            ctr+= 2          
    return ctr

x_count_element_in_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_element_in_list__mutmut_1': x_count_element_in_list__mutmut_1, 
    'x_count_element_in_list__mutmut_2': x_count_element_in_list__mutmut_2, 
    'x_count_element_in_list__mutmut_3': x_count_element_in_list__mutmut_3, 
    'x_count_element_in_list__mutmut_4': x_count_element_in_list__mutmut_4, 
    'x_count_element_in_list__mutmut_5': x_count_element_in_list__mutmut_5, 
    'x_count_element_in_list__mutmut_6': x_count_element_in_list__mutmut_6, 
    'x_count_element_in_list__mutmut_7': x_count_element_in_list__mutmut_7
}

def count_element_in_list(*args, **kwargs):
    result = _mutmut_trampoline(x_count_element_in_list__mutmut_orig, x_count_element_in_list__mutmut_mutants, args, kwargs)
    return result 

count_element_in_list.__signature__ = _mutmut_signature(x_count_element_in_list__mutmut_orig)
x_count_element_in_list__mutmut_orig.__name__ = 'x_count_element_in_list'