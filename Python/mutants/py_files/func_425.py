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
def x_first_odd__mutmut_orig(nums):
  first_odd = next((el for el in nums if el%2!=0),-1)
  return first_odd
def x_first_odd__mutmut_1(nums):
  first_odd = None
  return first_odd
def x_first_odd__mutmut_2(nums):
  first_odd = next(None,-1)
  return first_odd
def x_first_odd__mutmut_3(nums):
  first_odd = next((el for el in nums if el%2!=0),None)
  return first_odd
def x_first_odd__mutmut_4(nums):
  first_odd = next(-1)
  return first_odd
def x_first_odd__mutmut_5(nums):
  first_odd = next((el for el in nums if el%2!=0),)
  return first_odd
def x_first_odd__mutmut_6(nums):
  first_odd = next((el for el in nums if el / 2!=0),-1)
  return first_odd
def x_first_odd__mutmut_7(nums):
  first_odd = next((el for el in nums if el%3!=0),-1)
  return first_odd
def x_first_odd__mutmut_8(nums):
  first_odd = next((el for el in nums if el%2 == 0),-1)
  return first_odd
def x_first_odd__mutmut_9(nums):
  first_odd = next((el for el in nums if el%2!=1),-1)
  return first_odd
def x_first_odd__mutmut_10(nums):
  first_odd = next((el for el in nums if el%2!=0),+1)
  return first_odd
def x_first_odd__mutmut_11(nums):
  first_odd = next((el for el in nums if el%2!=0),-2)
  return first_odd

x_first_odd__mutmut_mutants : ClassVar[MutantDict] = {
'x_first_odd__mutmut_1': x_first_odd__mutmut_1, 
    'x_first_odd__mutmut_2': x_first_odd__mutmut_2, 
    'x_first_odd__mutmut_3': x_first_odd__mutmut_3, 
    'x_first_odd__mutmut_4': x_first_odd__mutmut_4, 
    'x_first_odd__mutmut_5': x_first_odd__mutmut_5, 
    'x_first_odd__mutmut_6': x_first_odd__mutmut_6, 
    'x_first_odd__mutmut_7': x_first_odd__mutmut_7, 
    'x_first_odd__mutmut_8': x_first_odd__mutmut_8, 
    'x_first_odd__mutmut_9': x_first_odd__mutmut_9, 
    'x_first_odd__mutmut_10': x_first_odd__mutmut_10, 
    'x_first_odd__mutmut_11': x_first_odd__mutmut_11
}

def first_odd(*args, **kwargs):
  result = _mutmut_trampoline(x_first_odd__mutmut_orig, x_first_odd__mutmut_mutants, args, kwargs)
  return result 

first_odd.__signature__ = _mutmut_signature(x_first_odd__mutmut_orig)
x_first_odd__mutmut_orig.__name__ = 'x_first_odd'