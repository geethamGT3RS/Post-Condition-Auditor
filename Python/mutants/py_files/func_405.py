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
def x_tuple_str_int__mutmut_orig(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_1(test_str):
  res = None
  return (res) 
def x_tuple_str_int__mutmut_2(test_str):
  res = tuple(None)
  return (res) 
def x_tuple_str_int__mutmut_3(test_str):
  res = tuple(int(None) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_4(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split(None))
  return (res) 
def x_tuple_str_int__mutmut_5(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace(None, '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_6(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', None).split(', '))
  return (res) 
def x_tuple_str_int__mutmut_7(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_8(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', ).split(', '))
  return (res) 
def x_tuple_str_int__mutmut_9(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(None, '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_10(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', None).replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_11(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace('').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_12(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', ).replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_13(test_str):
  res = tuple(int(num) for num in test_str.replace(None, '').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_14(test_str):
  res = tuple(int(num) for num in test_str.replace('(', None).replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_15(test_str):
  res = tuple(int(num) for num in test_str.replace('').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_16(test_str):
  res = tuple(int(num) for num in test_str.replace('(', ).replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_17(test_str):
  res = tuple(int(num) for num in test_str.replace('XX(XX', '').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_18(test_str):
  res = tuple(int(num) for num in test_str.replace('(', 'XXXX').replace(')', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_19(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace('XX)XX', '').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_20(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', 'XXXX').replace('...', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_21(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('XX...XX', '').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_22(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', 'XXXX').split(', '))
  return (res) 
def x_tuple_str_int__mutmut_23(test_str):
  res = tuple(int(num) for num in test_str.replace('(', '').replace(')', '').replace('...', '').split('XX, XX'))
  return (res) 

x_tuple_str_int__mutmut_mutants : ClassVar[MutantDict] = {
'x_tuple_str_int__mutmut_1': x_tuple_str_int__mutmut_1, 
    'x_tuple_str_int__mutmut_2': x_tuple_str_int__mutmut_2, 
    'x_tuple_str_int__mutmut_3': x_tuple_str_int__mutmut_3, 
    'x_tuple_str_int__mutmut_4': x_tuple_str_int__mutmut_4, 
    'x_tuple_str_int__mutmut_5': x_tuple_str_int__mutmut_5, 
    'x_tuple_str_int__mutmut_6': x_tuple_str_int__mutmut_6, 
    'x_tuple_str_int__mutmut_7': x_tuple_str_int__mutmut_7, 
    'x_tuple_str_int__mutmut_8': x_tuple_str_int__mutmut_8, 
    'x_tuple_str_int__mutmut_9': x_tuple_str_int__mutmut_9, 
    'x_tuple_str_int__mutmut_10': x_tuple_str_int__mutmut_10, 
    'x_tuple_str_int__mutmut_11': x_tuple_str_int__mutmut_11, 
    'x_tuple_str_int__mutmut_12': x_tuple_str_int__mutmut_12, 
    'x_tuple_str_int__mutmut_13': x_tuple_str_int__mutmut_13, 
    'x_tuple_str_int__mutmut_14': x_tuple_str_int__mutmut_14, 
    'x_tuple_str_int__mutmut_15': x_tuple_str_int__mutmut_15, 
    'x_tuple_str_int__mutmut_16': x_tuple_str_int__mutmut_16, 
    'x_tuple_str_int__mutmut_17': x_tuple_str_int__mutmut_17, 
    'x_tuple_str_int__mutmut_18': x_tuple_str_int__mutmut_18, 
    'x_tuple_str_int__mutmut_19': x_tuple_str_int__mutmut_19, 
    'x_tuple_str_int__mutmut_20': x_tuple_str_int__mutmut_20, 
    'x_tuple_str_int__mutmut_21': x_tuple_str_int__mutmut_21, 
    'x_tuple_str_int__mutmut_22': x_tuple_str_int__mutmut_22, 
    'x_tuple_str_int__mutmut_23': x_tuple_str_int__mutmut_23
}

def tuple_str_int(*args, **kwargs):
  result = _mutmut_trampoline(x_tuple_str_int__mutmut_orig, x_tuple_str_int__mutmut_mutants, args, kwargs)
  return result 

tuple_str_int.__signature__ = _mutmut_signature(x_tuple_str_int__mutmut_orig)
x_tuple_str_int__mutmut_orig.__name__ = 'x_tuple_str_int'