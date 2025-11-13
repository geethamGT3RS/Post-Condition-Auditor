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
def x_re_arrange_array__mutmut_orig(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_1(arr, n):
  j=None
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_2(arr, n):
  j=1
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_3(arr, n):
  j=0
  for i in range(None, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_4(arr, n):
  j=0
  for i in range(0, None):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_5(arr, n):
  j=0
  for i in range(n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_6(arr, n):
  j=0
  for i in range(0, ):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_7(arr, n):
  j=0
  for i in range(1, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_8(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] <= 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_9(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 1):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_10(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = None
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_11(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = None
      arr[j] = temp
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_12(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = None
      j = j + 1
  return arr
def x_re_arrange_array__mutmut_13(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = None
  return arr
def x_re_arrange_array__mutmut_14(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j - 1
  return arr
def x_re_arrange_array__mutmut_15(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 2
  return arr

x_re_arrange_array__mutmut_mutants : ClassVar[MutantDict] = {
'x_re_arrange_array__mutmut_1': x_re_arrange_array__mutmut_1, 
    'x_re_arrange_array__mutmut_2': x_re_arrange_array__mutmut_2, 
    'x_re_arrange_array__mutmut_3': x_re_arrange_array__mutmut_3, 
    'x_re_arrange_array__mutmut_4': x_re_arrange_array__mutmut_4, 
    'x_re_arrange_array__mutmut_5': x_re_arrange_array__mutmut_5, 
    'x_re_arrange_array__mutmut_6': x_re_arrange_array__mutmut_6, 
    'x_re_arrange_array__mutmut_7': x_re_arrange_array__mutmut_7, 
    'x_re_arrange_array__mutmut_8': x_re_arrange_array__mutmut_8, 
    'x_re_arrange_array__mutmut_9': x_re_arrange_array__mutmut_9, 
    'x_re_arrange_array__mutmut_10': x_re_arrange_array__mutmut_10, 
    'x_re_arrange_array__mutmut_11': x_re_arrange_array__mutmut_11, 
    'x_re_arrange_array__mutmut_12': x_re_arrange_array__mutmut_12, 
    'x_re_arrange_array__mutmut_13': x_re_arrange_array__mutmut_13, 
    'x_re_arrange_array__mutmut_14': x_re_arrange_array__mutmut_14, 
    'x_re_arrange_array__mutmut_15': x_re_arrange_array__mutmut_15
}

def re_arrange_array(*args, **kwargs):
  result = _mutmut_trampoline(x_re_arrange_array__mutmut_orig, x_re_arrange_array__mutmut_mutants, args, kwargs)
  return result 

re_arrange_array.__signature__ = _mutmut_signature(x_re_arrange_array__mutmut_orig)
x_re_arrange_array__mutmut_orig.__name__ = 'x_re_arrange_array'