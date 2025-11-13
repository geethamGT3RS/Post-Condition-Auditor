import collections as ct
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
def x_merge_dictionaries_three__mutmut_orig(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_1(dict1,dict2, dict3):
    merged_dict = None
    return merged_dict
def x_merge_dictionaries_three__mutmut_2(dict1,dict2, dict3):
    merged_dict = dict(None)
    return merged_dict
def x_merge_dictionaries_three__mutmut_3(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap(None,dict1,dict2,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_4(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},None,dict2,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_5(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,None,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_6(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,None))
    return merged_dict
def x_merge_dictionaries_three__mutmut_7(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap(dict1,dict2,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_8(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict2,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_9(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict3))
    return merged_dict
def x_merge_dictionaries_three__mutmut_10(dict1,dict2, dict3):
    merged_dict = dict(ct.ChainMap({},dict1,dict2,))
    return merged_dict

x_merge_dictionaries_three__mutmut_mutants : ClassVar[MutantDict] = {
'x_merge_dictionaries_three__mutmut_1': x_merge_dictionaries_three__mutmut_1, 
    'x_merge_dictionaries_three__mutmut_2': x_merge_dictionaries_three__mutmut_2, 
    'x_merge_dictionaries_three__mutmut_3': x_merge_dictionaries_three__mutmut_3, 
    'x_merge_dictionaries_three__mutmut_4': x_merge_dictionaries_three__mutmut_4, 
    'x_merge_dictionaries_three__mutmut_5': x_merge_dictionaries_three__mutmut_5, 
    'x_merge_dictionaries_three__mutmut_6': x_merge_dictionaries_three__mutmut_6, 
    'x_merge_dictionaries_three__mutmut_7': x_merge_dictionaries_three__mutmut_7, 
    'x_merge_dictionaries_three__mutmut_8': x_merge_dictionaries_three__mutmut_8, 
    'x_merge_dictionaries_three__mutmut_9': x_merge_dictionaries_three__mutmut_9, 
    'x_merge_dictionaries_three__mutmut_10': x_merge_dictionaries_three__mutmut_10
}

def merge_dictionaries_three(*args, **kwargs):
    result = _mutmut_trampoline(x_merge_dictionaries_three__mutmut_orig, x_merge_dictionaries_three__mutmut_mutants, args, kwargs)
    return result 

merge_dictionaries_three.__signature__ = _mutmut_signature(x_merge_dictionaries_three__mutmut_orig)
x_merge_dictionaries_three__mutmut_orig.__name__ = 'x_merge_dictionaries_three'