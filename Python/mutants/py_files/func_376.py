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
def x_min_k__mutmut_orig(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res) 
def x_min_k__mutmut_1(test_list, K):
  res = None
  return (res) 
def x_min_k__mutmut_2(test_list, K):
  res = sorted(None, key = lambda x: x[1])[:K]
  return (res) 
def x_min_k__mutmut_3(test_list, K):
  res = sorted(test_list, key = None)[:K]
  return (res) 
def x_min_k__mutmut_4(test_list, K):
  res = sorted(key = lambda x: x[1])[:K]
  return (res) 
def x_min_k__mutmut_5(test_list, K):
  res = sorted(test_list, )[:K]
  return (res) 
def x_min_k__mutmut_6(test_list, K):
  res = sorted(test_list, key = lambda x: None)[:K]
  return (res) 
def x_min_k__mutmut_7(test_list, K):
  res = sorted(test_list, key = lambda x: x[2])[:K]
  return (res) 

x_min_k__mutmut_mutants : ClassVar[MutantDict] = {
'x_min_k__mutmut_1': x_min_k__mutmut_1, 
    'x_min_k__mutmut_2': x_min_k__mutmut_2, 
    'x_min_k__mutmut_3': x_min_k__mutmut_3, 
    'x_min_k__mutmut_4': x_min_k__mutmut_4, 
    'x_min_k__mutmut_5': x_min_k__mutmut_5, 
    'x_min_k__mutmut_6': x_min_k__mutmut_6, 
    'x_min_k__mutmut_7': x_min_k__mutmut_7
}

def min_k(*args, **kwargs):
  result = _mutmut_trampoline(x_min_k__mutmut_orig, x_min_k__mutmut_mutants, args, kwargs)
  return result 

min_k.__signature__ = _mutmut_signature(x_min_k__mutmut_orig)
x_min_k__mutmut_orig.__name__ = 'x_min_k'