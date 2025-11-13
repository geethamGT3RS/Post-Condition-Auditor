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
def x_check_monthnumber_number__mutmut_orig(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_1(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==9 and monthnum3==11
def x_check_monthnumber_number__mutmut_2(monthnum3):
  return monthnum3==4 or monthnum3==6 and monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_3(monthnum3):
  return monthnum3==4 and monthnum3==6 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_4(monthnum3):
  return monthnum3 != 4 or monthnum3==6 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_5(monthnum3):
  return monthnum3==5 or monthnum3==6 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_6(monthnum3):
  return monthnum3==4 or monthnum3 != 6 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_7(monthnum3):
  return monthnum3==4 or monthnum3==7 or monthnum3==9 or monthnum3==11
def x_check_monthnumber_number__mutmut_8(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3 != 9 or monthnum3==11
def x_check_monthnumber_number__mutmut_9(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==10 or monthnum3==11
def x_check_monthnumber_number__mutmut_10(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3 != 11
def x_check_monthnumber_number__mutmut_11(monthnum3):
  return monthnum3==4 or monthnum3==6 or monthnum3==9 or monthnum3==12

x_check_monthnumber_number__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_monthnumber_number__mutmut_1': x_check_monthnumber_number__mutmut_1, 
    'x_check_monthnumber_number__mutmut_2': x_check_monthnumber_number__mutmut_2, 
    'x_check_monthnumber_number__mutmut_3': x_check_monthnumber_number__mutmut_3, 
    'x_check_monthnumber_number__mutmut_4': x_check_monthnumber_number__mutmut_4, 
    'x_check_monthnumber_number__mutmut_5': x_check_monthnumber_number__mutmut_5, 
    'x_check_monthnumber_number__mutmut_6': x_check_monthnumber_number__mutmut_6, 
    'x_check_monthnumber_number__mutmut_7': x_check_monthnumber_number__mutmut_7, 
    'x_check_monthnumber_number__mutmut_8': x_check_monthnumber_number__mutmut_8, 
    'x_check_monthnumber_number__mutmut_9': x_check_monthnumber_number__mutmut_9, 
    'x_check_monthnumber_number__mutmut_10': x_check_monthnumber_number__mutmut_10, 
    'x_check_monthnumber_number__mutmut_11': x_check_monthnumber_number__mutmut_11
}

def check_monthnumber_number(*args, **kwargs):
  result = _mutmut_trampoline(x_check_monthnumber_number__mutmut_orig, x_check_monthnumber_number__mutmut_mutants, args, kwargs)
  return result 

check_monthnumber_number.__signature__ = _mutmut_signature(x_check_monthnumber_number__mutmut_orig)
x_check_monthnumber_number__mutmut_orig.__name__ = 'x_check_monthnumber_number'