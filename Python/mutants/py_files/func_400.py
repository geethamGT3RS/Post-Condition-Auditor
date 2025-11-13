from itertools import combinations 
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
def x_find_combinations__mutmut_orig(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]
  return (res) 
def x_find_combinations__mutmut_1(test_list):
  res = None
  return (res) 
def x_find_combinations__mutmut_2(test_list):
  res = [(b1 - a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]
  return (res) 
def x_find_combinations__mutmut_3(test_list):
  res = [(b1 + a1, b2 - a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]
  return (res) 
def x_find_combinations__mutmut_4(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(None, 2)]
  return (res) 
def x_find_combinations__mutmut_5(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, None)]
  return (res) 
def x_find_combinations__mutmut_6(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(2)]
  return (res) 
def x_find_combinations__mutmut_7(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, )]
  return (res) 
def x_find_combinations__mutmut_8(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 3)]
  return (res) 

x_find_combinations__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_combinations__mutmut_1': x_find_combinations__mutmut_1, 
    'x_find_combinations__mutmut_2': x_find_combinations__mutmut_2, 
    'x_find_combinations__mutmut_3': x_find_combinations__mutmut_3, 
    'x_find_combinations__mutmut_4': x_find_combinations__mutmut_4, 
    'x_find_combinations__mutmut_5': x_find_combinations__mutmut_5, 
    'x_find_combinations__mutmut_6': x_find_combinations__mutmut_6, 
    'x_find_combinations__mutmut_7': x_find_combinations__mutmut_7, 
    'x_find_combinations__mutmut_8': x_find_combinations__mutmut_8
}

def find_combinations(*args, **kwargs):
  result = _mutmut_trampoline(x_find_combinations__mutmut_orig, x_find_combinations__mutmut_mutants, args, kwargs)
  return result 

find_combinations.__signature__ = _mutmut_signature(x_find_combinations__mutmut_orig)
x_find_combinations__mutmut_orig.__name__ = 'x_find_combinations'