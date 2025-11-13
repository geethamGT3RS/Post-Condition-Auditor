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
def x_add_nested_tuples__mutmut_orig(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_1(test_tup1, test_tup2):
  res = None
  return (res) 
def x_add_nested_tuples__mutmut_2(test_tup1, test_tup2):
  res = tuple(None)
  return (res) 
def x_add_nested_tuples__mutmut_3(test_tup1, test_tup2):
  res = tuple(tuple(None)
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_4(test_tup1, test_tup2):
  res = tuple(tuple(a - b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_5(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(None, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_6(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, None))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_7(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_8(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, ))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_9(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(None, test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_10(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, None))
  return (res) 
def x_add_nested_tuples__mutmut_11(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup2))
  return (res) 
def x_add_nested_tuples__mutmut_12(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, ))
  return (res) 

x_add_nested_tuples__mutmut_mutants : ClassVar[MutantDict] = {
'x_add_nested_tuples__mutmut_1': x_add_nested_tuples__mutmut_1, 
    'x_add_nested_tuples__mutmut_2': x_add_nested_tuples__mutmut_2, 
    'x_add_nested_tuples__mutmut_3': x_add_nested_tuples__mutmut_3, 
    'x_add_nested_tuples__mutmut_4': x_add_nested_tuples__mutmut_4, 
    'x_add_nested_tuples__mutmut_5': x_add_nested_tuples__mutmut_5, 
    'x_add_nested_tuples__mutmut_6': x_add_nested_tuples__mutmut_6, 
    'x_add_nested_tuples__mutmut_7': x_add_nested_tuples__mutmut_7, 
    'x_add_nested_tuples__mutmut_8': x_add_nested_tuples__mutmut_8, 
    'x_add_nested_tuples__mutmut_9': x_add_nested_tuples__mutmut_9, 
    'x_add_nested_tuples__mutmut_10': x_add_nested_tuples__mutmut_10, 
    'x_add_nested_tuples__mutmut_11': x_add_nested_tuples__mutmut_11, 
    'x_add_nested_tuples__mutmut_12': x_add_nested_tuples__mutmut_12
}

def add_nested_tuples(*args, **kwargs):
  result = _mutmut_trampoline(x_add_nested_tuples__mutmut_orig, x_add_nested_tuples__mutmut_mutants, args, kwargs)
  return result 

add_nested_tuples.__signature__ = _mutmut_signature(x_add_nested_tuples__mutmut_orig)
x_add_nested_tuples__mutmut_orig.__name__ = 'x_add_nested_tuples'