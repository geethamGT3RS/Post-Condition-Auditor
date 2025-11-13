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
def x_first_repeated_char__mutmut_orig(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c
def x_first_repeated_char__mutmut_1(str1):
  for index,c in enumerate(None):
    if str1[:index+1].count(c) > 1:
      return c
def x_first_repeated_char__mutmut_2(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(None) > 1:
      return c
def x_first_repeated_char__mutmut_3(str1):
  for index,c in enumerate(str1):
    if str1[:index - 1].count(c) > 1:
      return c
def x_first_repeated_char__mutmut_4(str1):
  for index,c in enumerate(str1):
    if str1[:index+2].count(c) > 1:
      return c
def x_first_repeated_char__mutmut_5(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) >= 1:
      return c
def x_first_repeated_char__mutmut_6(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 2:
      return c

x_first_repeated_char__mutmut_mutants : ClassVar[MutantDict] = {
'x_first_repeated_char__mutmut_1': x_first_repeated_char__mutmut_1, 
    'x_first_repeated_char__mutmut_2': x_first_repeated_char__mutmut_2, 
    'x_first_repeated_char__mutmut_3': x_first_repeated_char__mutmut_3, 
    'x_first_repeated_char__mutmut_4': x_first_repeated_char__mutmut_4, 
    'x_first_repeated_char__mutmut_5': x_first_repeated_char__mutmut_5, 
    'x_first_repeated_char__mutmut_6': x_first_repeated_char__mutmut_6
}

def first_repeated_char(*args, **kwargs):
  result = _mutmut_trampoline(x_first_repeated_char__mutmut_orig, x_first_repeated_char__mutmut_mutants, args, kwargs)
  return result 

first_repeated_char.__signature__ = _mutmut_signature(x_first_repeated_char__mutmut_orig)
x_first_repeated_char__mutmut_orig.__name__ = 'x_first_repeated_char'