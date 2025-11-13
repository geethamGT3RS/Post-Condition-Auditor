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
def x_frequency_lists__mutmut_orig(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_1(list1):
    list1 = None
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_2(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = None
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_3(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num not in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_4(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] = 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_5(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] -= 1
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_6(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 2
        else:
            key = num
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_7(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = None
            value = 1
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_8(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = None
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_9(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 2
            dic_data[key] = value
    return dic_data
def x_frequency_lists__mutmut_10(list1):
    list1 = [item for sublist in list1 for item in sublist]
    dic_data = {}
    for num in list1:
        if num in dic_data.keys():
            dic_data[num] += 1
        else:
            key = num
            value = 1
            dic_data[key] = None
    return dic_data

x_frequency_lists__mutmut_mutants : ClassVar[MutantDict] = {
'x_frequency_lists__mutmut_1': x_frequency_lists__mutmut_1, 
    'x_frequency_lists__mutmut_2': x_frequency_lists__mutmut_2, 
    'x_frequency_lists__mutmut_3': x_frequency_lists__mutmut_3, 
    'x_frequency_lists__mutmut_4': x_frequency_lists__mutmut_4, 
    'x_frequency_lists__mutmut_5': x_frequency_lists__mutmut_5, 
    'x_frequency_lists__mutmut_6': x_frequency_lists__mutmut_6, 
    'x_frequency_lists__mutmut_7': x_frequency_lists__mutmut_7, 
    'x_frequency_lists__mutmut_8': x_frequency_lists__mutmut_8, 
    'x_frequency_lists__mutmut_9': x_frequency_lists__mutmut_9, 
    'x_frequency_lists__mutmut_10': x_frequency_lists__mutmut_10
}

def frequency_lists(*args, **kwargs):
    result = _mutmut_trampoline(x_frequency_lists__mutmut_orig, x_frequency_lists__mutmut_mutants, args, kwargs)
    return result 

frequency_lists.__signature__ = _mutmut_signature(x_frequency_lists__mutmut_orig)
x_frequency_lists__mutmut_orig.__name__ = 'x_frequency_lists'
