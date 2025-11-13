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
def x_sum_negativenum__mutmut_orig(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_1(nums):
  sum_negativenum = None
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_2(nums):
  sum_negativenum = list(None)
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_3(nums):
  sum_negativenum = list(filter(None,nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_4(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,None))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_5(nums):
  sum_negativenum = list(filter(nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_6(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_7(nums):
  sum_negativenum = list(filter(lambda nums:None,nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_8(nums):
  sum_negativenum = list(filter(lambda nums:nums <= 0,nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_9(nums):
  sum_negativenum = list(filter(lambda nums:nums<1,nums))
  return sum(sum_negativenum)
def x_sum_negativenum__mutmut_10(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,nums))
  return sum(None)

x_sum_negativenum__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_negativenum__mutmut_1': x_sum_negativenum__mutmut_1, 
    'x_sum_negativenum__mutmut_2': x_sum_negativenum__mutmut_2, 
    'x_sum_negativenum__mutmut_3': x_sum_negativenum__mutmut_3, 
    'x_sum_negativenum__mutmut_4': x_sum_negativenum__mutmut_4, 
    'x_sum_negativenum__mutmut_5': x_sum_negativenum__mutmut_5, 
    'x_sum_negativenum__mutmut_6': x_sum_negativenum__mutmut_6, 
    'x_sum_negativenum__mutmut_7': x_sum_negativenum__mutmut_7, 
    'x_sum_negativenum__mutmut_8': x_sum_negativenum__mutmut_8, 
    'x_sum_negativenum__mutmut_9': x_sum_negativenum__mutmut_9, 
    'x_sum_negativenum__mutmut_10': x_sum_negativenum__mutmut_10
}

def sum_negativenum(*args, **kwargs):
  result = _mutmut_trampoline(x_sum_negativenum__mutmut_orig, x_sum_negativenum__mutmut_mutants, args, kwargs)
  return result 

sum_negativenum.__signature__ = _mutmut_signature(x_sum_negativenum__mutmut_orig)
x_sum_negativenum__mutmut_orig.__name__ = 'x_sum_negativenum'