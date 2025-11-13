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
def x_tuple_to_dict__mutmut_orig(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_1(test_tup):
  res = None
  return (res) 
def x_tuple_to_dict__mutmut_2(test_tup):
  res = dict(None)
  return (res) 
def x_tuple_to_dict__mutmut_3(test_tup):
  res = dict(test_tup[idx : idx - 2] for idx in range(0, len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_4(test_tup):
  res = dict(test_tup[idx : idx + 3] for idx in range(0, len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_5(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(None, len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_6(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, None, 2))
  return (res) 
def x_tuple_to_dict__mutmut_7(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), None))
  return (res) 
def x_tuple_to_dict__mutmut_8(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_9(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, 2))
  return (res) 
def x_tuple_to_dict__mutmut_10(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), ))
  return (res) 
def x_tuple_to_dict__mutmut_11(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(1, len(test_tup), 2))
  return (res) 
def x_tuple_to_dict__mutmut_12(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 3))
  return (res) 

x_tuple_to_dict__mutmut_mutants : ClassVar[MutantDict] = {
'x_tuple_to_dict__mutmut_1': x_tuple_to_dict__mutmut_1, 
    'x_tuple_to_dict__mutmut_2': x_tuple_to_dict__mutmut_2, 
    'x_tuple_to_dict__mutmut_3': x_tuple_to_dict__mutmut_3, 
    'x_tuple_to_dict__mutmut_4': x_tuple_to_dict__mutmut_4, 
    'x_tuple_to_dict__mutmut_5': x_tuple_to_dict__mutmut_5, 
    'x_tuple_to_dict__mutmut_6': x_tuple_to_dict__mutmut_6, 
    'x_tuple_to_dict__mutmut_7': x_tuple_to_dict__mutmut_7, 
    'x_tuple_to_dict__mutmut_8': x_tuple_to_dict__mutmut_8, 
    'x_tuple_to_dict__mutmut_9': x_tuple_to_dict__mutmut_9, 
    'x_tuple_to_dict__mutmut_10': x_tuple_to_dict__mutmut_10, 
    'x_tuple_to_dict__mutmut_11': x_tuple_to_dict__mutmut_11, 
    'x_tuple_to_dict__mutmut_12': x_tuple_to_dict__mutmut_12
}

def tuple_to_dict(*args, **kwargs):
  result = _mutmut_trampoline(x_tuple_to_dict__mutmut_orig, x_tuple_to_dict__mutmut_mutants, args, kwargs)
  return result 

tuple_to_dict.__signature__ = _mutmut_signature(x_tuple_to_dict__mutmut_orig)
x_tuple_to_dict__mutmut_orig.__name__ = 'x_tuple_to_dict'