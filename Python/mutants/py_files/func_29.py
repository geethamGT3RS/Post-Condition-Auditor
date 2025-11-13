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
def x_find_equal_tuple__mutmut_orig(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_1(Input):
  k = None
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_2(Input):
  k = 1 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_3(Input):
  k = 0 if Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_4(Input):
  k = 0 if not Input else len(Input[0])
  flag = None
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_5(Input):
  k = 0 if not Input else len(Input[0])
  flag = 2
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_6(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) == k:
      flag = 0
      break
  return flag
def x_find_equal_tuple__mutmut_7(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = None
      break
  return flag
def x_find_equal_tuple__mutmut_8(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 1
      break
  return flag
def x_find_equal_tuple__mutmut_9(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      return
  return flag

x_find_equal_tuple__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_equal_tuple__mutmut_1': x_find_equal_tuple__mutmut_1, 
    'x_find_equal_tuple__mutmut_2': x_find_equal_tuple__mutmut_2, 
    'x_find_equal_tuple__mutmut_3': x_find_equal_tuple__mutmut_3, 
    'x_find_equal_tuple__mutmut_4': x_find_equal_tuple__mutmut_4, 
    'x_find_equal_tuple__mutmut_5': x_find_equal_tuple__mutmut_5, 
    'x_find_equal_tuple__mutmut_6': x_find_equal_tuple__mutmut_6, 
    'x_find_equal_tuple__mutmut_7': x_find_equal_tuple__mutmut_7, 
    'x_find_equal_tuple__mutmut_8': x_find_equal_tuple__mutmut_8, 
    'x_find_equal_tuple__mutmut_9': x_find_equal_tuple__mutmut_9
}

def find_equal_tuple(*args, **kwargs):
  result = _mutmut_trampoline(x_find_equal_tuple__mutmut_orig, x_find_equal_tuple__mutmut_mutants, args, kwargs)
  return result 

find_equal_tuple.__signature__ = _mutmut_signature(x_find_equal_tuple__mutmut_orig)
x_find_equal_tuple__mutmut_orig.__name__ = 'x_find_equal_tuple'
def x_get_equal__mutmut_orig(Input):
  return find_equal_tuple(Input) == 1
def x_get_equal__mutmut_1(Input):
  return find_equal_tuple(None) == 1
def x_get_equal__mutmut_2(Input):
  return find_equal_tuple(Input) != 1
def x_get_equal__mutmut_3(Input):
  return find_equal_tuple(Input) == 2

x_get_equal__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_equal__mutmut_1': x_get_equal__mutmut_1, 
    'x_get_equal__mutmut_2': x_get_equal__mutmut_2, 
    'x_get_equal__mutmut_3': x_get_equal__mutmut_3
}

def get_equal(*args, **kwargs):
  result = _mutmut_trampoline(x_get_equal__mutmut_orig, x_get_equal__mutmut_mutants, args, kwargs)
  return result 

get_equal.__signature__ = _mutmut_signature(x_get_equal__mutmut_orig)
x_get_equal__mutmut_orig.__name__ = 'x_get_equal'