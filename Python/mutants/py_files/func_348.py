from operator import eq
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
def x_count_same_pair__mutmut_orig(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result
def x_count_same_pair__mutmut_1(nums1, nums2):
    result = None
    return result
def x_count_same_pair__mutmut_2(nums1, nums2):
    result = sum(None)
    return result
def x_count_same_pair__mutmut_3(nums1, nums2):
    result = sum(map(None, nums1, nums2))
    return result
def x_count_same_pair__mutmut_4(nums1, nums2):
    result = sum(map(eq, None, nums2))
    return result
def x_count_same_pair__mutmut_5(nums1, nums2):
    result = sum(map(eq, nums1, None))
    return result
def x_count_same_pair__mutmut_6(nums1, nums2):
    result = sum(map(nums1, nums2))
    return result
def x_count_same_pair__mutmut_7(nums1, nums2):
    result = sum(map(eq, nums2))
    return result
def x_count_same_pair__mutmut_8(nums1, nums2):
    result = sum(map(eq, nums1, ))
    return result

x_count_same_pair__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_same_pair__mutmut_1': x_count_same_pair__mutmut_1, 
    'x_count_same_pair__mutmut_2': x_count_same_pair__mutmut_2, 
    'x_count_same_pair__mutmut_3': x_count_same_pair__mutmut_3, 
    'x_count_same_pair__mutmut_4': x_count_same_pair__mutmut_4, 
    'x_count_same_pair__mutmut_5': x_count_same_pair__mutmut_5, 
    'x_count_same_pair__mutmut_6': x_count_same_pair__mutmut_6, 
    'x_count_same_pair__mutmut_7': x_count_same_pair__mutmut_7, 
    'x_count_same_pair__mutmut_8': x_count_same_pair__mutmut_8
}

def count_same_pair(*args, **kwargs):
    result = _mutmut_trampoline(x_count_same_pair__mutmut_orig, x_count_same_pair__mutmut_mutants, args, kwargs)
    return result 

count_same_pair.__signature__ = _mutmut_signature(x_count_same_pair__mutmut_orig)
x_count_same_pair__mutmut_orig.__name__ = 'x_count_same_pair'