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
def x_pair_wise__mutmut_orig(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_1(l1):
    temp = None
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_2(l1):
    temp = []
    for i in range(None):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_3(l1):
    temp = []
    for i in range(len(l1) + 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_4(l1):
    temp = []
    for i in range(len(l1) - 2):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_5(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = None
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_6(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i - 1]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_7(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 2]
        x = (current_element, next_element)
        temp.append(x)
    return temp
def x_pair_wise__mutmut_8(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = None
        temp.append(x)
    return temp
def x_pair_wise__mutmut_9(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = l1[i], l1[i + 1]
        x = (current_element, next_element)
        temp.append(None)
    return temp

x_pair_wise__mutmut_mutants : ClassVar[MutantDict] = {
'x_pair_wise__mutmut_1': x_pair_wise__mutmut_1, 
    'x_pair_wise__mutmut_2': x_pair_wise__mutmut_2, 
    'x_pair_wise__mutmut_3': x_pair_wise__mutmut_3, 
    'x_pair_wise__mutmut_4': x_pair_wise__mutmut_4, 
    'x_pair_wise__mutmut_5': x_pair_wise__mutmut_5, 
    'x_pair_wise__mutmut_6': x_pair_wise__mutmut_6, 
    'x_pair_wise__mutmut_7': x_pair_wise__mutmut_7, 
    'x_pair_wise__mutmut_8': x_pair_wise__mutmut_8, 
    'x_pair_wise__mutmut_9': x_pair_wise__mutmut_9
}

def pair_wise(*args, **kwargs):
    result = _mutmut_trampoline(x_pair_wise__mutmut_orig, x_pair_wise__mutmut_mutants, args, kwargs)
    return result 

pair_wise.__signature__ = _mutmut_signature(x_pair_wise__mutmut_orig)
x_pair_wise__mutmut_orig.__name__ = 'x_pair_wise'