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
def x_filter_oddnumbers__mutmut_orig(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_1(nums):
 odd_nums = None
 return odd_nums
def x_filter_oddnumbers__mutmut_2(nums):
 odd_nums = list(None)
 return odd_nums
def x_filter_oddnumbers__mutmut_3(nums):
 odd_nums = list(filter(None, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_4(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, None))
 return odd_nums
def x_filter_oddnumbers__mutmut_5(nums):
 odd_nums = list(filter(nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_6(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, ))
 return odd_nums
def x_filter_oddnumbers__mutmut_7(nums):
 odd_nums = list(filter(lambda x: None, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_8(nums):
 odd_nums = list(filter(lambda x: x / 2 != 0, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_9(nums):
 odd_nums = list(filter(lambda x: x%3 != 0, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_10(nums):
 odd_nums = list(filter(lambda x: x%2 == 0, nums))
 return odd_nums
def x_filter_oddnumbers__mutmut_11(nums):
 odd_nums = list(filter(lambda x: x%2 != 1, nums))
 return odd_nums

x_filter_oddnumbers__mutmut_mutants : ClassVar[MutantDict] = {
'x_filter_oddnumbers__mutmut_1': x_filter_oddnumbers__mutmut_1, 
    'x_filter_oddnumbers__mutmut_2': x_filter_oddnumbers__mutmut_2, 
    'x_filter_oddnumbers__mutmut_3': x_filter_oddnumbers__mutmut_3, 
    'x_filter_oddnumbers__mutmut_4': x_filter_oddnumbers__mutmut_4, 
    'x_filter_oddnumbers__mutmut_5': x_filter_oddnumbers__mutmut_5, 
    'x_filter_oddnumbers__mutmut_6': x_filter_oddnumbers__mutmut_6, 
    'x_filter_oddnumbers__mutmut_7': x_filter_oddnumbers__mutmut_7, 
    'x_filter_oddnumbers__mutmut_8': x_filter_oddnumbers__mutmut_8, 
    'x_filter_oddnumbers__mutmut_9': x_filter_oddnumbers__mutmut_9, 
    'x_filter_oddnumbers__mutmut_10': x_filter_oddnumbers__mutmut_10, 
    'x_filter_oddnumbers__mutmut_11': x_filter_oddnumbers__mutmut_11
}

def filter_oddnumbers(*args, **kwargs):
 result = _mutmut_trampoline(x_filter_oddnumbers__mutmut_orig, x_filter_oddnumbers__mutmut_mutants, args, kwargs)
 return result 

filter_oddnumbers.__signature__ = _mutmut_signature(x_filter_oddnumbers__mutmut_orig)
x_filter_oddnumbers__mutmut_orig.__name__ = 'x_filter_oddnumbers'