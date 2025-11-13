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
def x_odd_values_string__mutmut_orig(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_1(str):
  result = None 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_2(str):
  result = "XXXX" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_3(str):
  result = "" 
  for i in range(None):
    if i % 2 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_4(str):
  result = "" 
  for i in range(len(str)):
    if i / 2 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_5(str):
  result = "" 
  for i in range(len(str)):
    if i % 3 == 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_6(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 != 0:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_7(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 1:
      result = result + str[i]
  return result
def x_odd_values_string__mutmut_8(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = None
  return result
def x_odd_values_string__mutmut_9(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result - str[i]
  return result

x_odd_values_string__mutmut_mutants : ClassVar[MutantDict] = {
'x_odd_values_string__mutmut_1': x_odd_values_string__mutmut_1, 
    'x_odd_values_string__mutmut_2': x_odd_values_string__mutmut_2, 
    'x_odd_values_string__mutmut_3': x_odd_values_string__mutmut_3, 
    'x_odd_values_string__mutmut_4': x_odd_values_string__mutmut_4, 
    'x_odd_values_string__mutmut_5': x_odd_values_string__mutmut_5, 
    'x_odd_values_string__mutmut_6': x_odd_values_string__mutmut_6, 
    'x_odd_values_string__mutmut_7': x_odd_values_string__mutmut_7, 
    'x_odd_values_string__mutmut_8': x_odd_values_string__mutmut_8, 
    'x_odd_values_string__mutmut_9': x_odd_values_string__mutmut_9
}

def odd_values_string(*args, **kwargs):
  result = _mutmut_trampoline(x_odd_values_string__mutmut_orig, x_odd_values_string__mutmut_mutants, args, kwargs)
  return result 

odd_values_string.__signature__ = _mutmut_signature(x_odd_values_string__mutmut_orig)
x_odd_values_string__mutmut_orig.__name__ = 'x_odd_values_string'