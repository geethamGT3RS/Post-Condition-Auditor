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
def x_bitwise_xor__mutmut_orig(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 
def x_bitwise_xor__mutmut_1(test_tup1, test_tup2):
  res = None
  return (res) 
def x_bitwise_xor__mutmut_2(test_tup1, test_tup2):
  res = tuple(None)
  return (res) 
def x_bitwise_xor__mutmut_3(test_tup1, test_tup2):
  res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 
def x_bitwise_xor__mutmut_4(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(None, test_tup2))
  return (res) 
def x_bitwise_xor__mutmut_5(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, None))
  return (res) 
def x_bitwise_xor__mutmut_6(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup2))
  return (res) 
def x_bitwise_xor__mutmut_7(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, ))
  return (res) 

x_bitwise_xor__mutmut_mutants : ClassVar[MutantDict] = {
'x_bitwise_xor__mutmut_1': x_bitwise_xor__mutmut_1, 
    'x_bitwise_xor__mutmut_2': x_bitwise_xor__mutmut_2, 
    'x_bitwise_xor__mutmut_3': x_bitwise_xor__mutmut_3, 
    'x_bitwise_xor__mutmut_4': x_bitwise_xor__mutmut_4, 
    'x_bitwise_xor__mutmut_5': x_bitwise_xor__mutmut_5, 
    'x_bitwise_xor__mutmut_6': x_bitwise_xor__mutmut_6, 
    'x_bitwise_xor__mutmut_7': x_bitwise_xor__mutmut_7
}

def bitwise_xor(*args, **kwargs):
  result = _mutmut_trampoline(x_bitwise_xor__mutmut_orig, x_bitwise_xor__mutmut_mutants, args, kwargs)
  return result 

bitwise_xor.__signature__ = _mutmut_signature(x_bitwise_xor__mutmut_orig)
x_bitwise_xor__mutmut_orig.__name__ = 'x_bitwise_xor'