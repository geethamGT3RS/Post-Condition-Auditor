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
def x_kth_element__mutmut_orig(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_1(arr, k):
  n = None
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_2(arr, k):
  n = len(arr)
  for i in range(None):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_3(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(None, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_4(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, None):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_5(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_6(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, ):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_7(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(1, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_8(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i + 1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_9(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n + i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_10(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-2):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_11(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] >= arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_12(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j - 1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_13(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+2]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_14(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j - 1] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_15(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+2] == arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_16(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] != arr[j+1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_17(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j - 1], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_18(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+2], arr[j]
  return arr[k-1]
def x_kth_element__mutmut_19(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k + 1]
def x_kth_element__mutmut_20(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-2]

x_kth_element__mutmut_mutants : ClassVar[MutantDict] = {
'x_kth_element__mutmut_1': x_kth_element__mutmut_1, 
    'x_kth_element__mutmut_2': x_kth_element__mutmut_2, 
    'x_kth_element__mutmut_3': x_kth_element__mutmut_3, 
    'x_kth_element__mutmut_4': x_kth_element__mutmut_4, 
    'x_kth_element__mutmut_5': x_kth_element__mutmut_5, 
    'x_kth_element__mutmut_6': x_kth_element__mutmut_6, 
    'x_kth_element__mutmut_7': x_kth_element__mutmut_7, 
    'x_kth_element__mutmut_8': x_kth_element__mutmut_8, 
    'x_kth_element__mutmut_9': x_kth_element__mutmut_9, 
    'x_kth_element__mutmut_10': x_kth_element__mutmut_10, 
    'x_kth_element__mutmut_11': x_kth_element__mutmut_11, 
    'x_kth_element__mutmut_12': x_kth_element__mutmut_12, 
    'x_kth_element__mutmut_13': x_kth_element__mutmut_13, 
    'x_kth_element__mutmut_14': x_kth_element__mutmut_14, 
    'x_kth_element__mutmut_15': x_kth_element__mutmut_15, 
    'x_kth_element__mutmut_16': x_kth_element__mutmut_16, 
    'x_kth_element__mutmut_17': x_kth_element__mutmut_17, 
    'x_kth_element__mutmut_18': x_kth_element__mutmut_18, 
    'x_kth_element__mutmut_19': x_kth_element__mutmut_19, 
    'x_kth_element__mutmut_20': x_kth_element__mutmut_20
}

def kth_element(*args, **kwargs):
  result = _mutmut_trampoline(x_kth_element__mutmut_orig, x_kth_element__mutmut_mutants, args, kwargs)
  return result 

kth_element.__signature__ = _mutmut_signature(x_kth_element__mutmut_orig)
x_kth_element__mutmut_orig.__name__ = 'x_kth_element'