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
def x_max_product__mutmut_orig(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_1(arr):   
  n = None
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_2(arr):   
  n = len(arr)
  mpis = None
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_3(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(None): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_4(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = None
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_5(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = None
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_6(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i - 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_7(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 2
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_8(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j <= n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_9(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j + 1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_10(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-2] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_11(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] >= arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_12(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        return
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_13(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod = arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_14(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod /= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_15(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod >= mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_16(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = None 
      j = j + 1
  return max(mpis)
def x_max_product__mutmut_17(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = None
  return max(mpis)
def x_max_product__mutmut_18(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j - 1
  return max(mpis)
def x_max_product__mutmut_19(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 2
  return max(mpis)
def x_max_product__mutmut_20(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(None)

x_max_product__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_product__mutmut_1': x_max_product__mutmut_1, 
    'x_max_product__mutmut_2': x_max_product__mutmut_2, 
    'x_max_product__mutmut_3': x_max_product__mutmut_3, 
    'x_max_product__mutmut_4': x_max_product__mutmut_4, 
    'x_max_product__mutmut_5': x_max_product__mutmut_5, 
    'x_max_product__mutmut_6': x_max_product__mutmut_6, 
    'x_max_product__mutmut_7': x_max_product__mutmut_7, 
    'x_max_product__mutmut_8': x_max_product__mutmut_8, 
    'x_max_product__mutmut_9': x_max_product__mutmut_9, 
    'x_max_product__mutmut_10': x_max_product__mutmut_10, 
    'x_max_product__mutmut_11': x_max_product__mutmut_11, 
    'x_max_product__mutmut_12': x_max_product__mutmut_12, 
    'x_max_product__mutmut_13': x_max_product__mutmut_13, 
    'x_max_product__mutmut_14': x_max_product__mutmut_14, 
    'x_max_product__mutmut_15': x_max_product__mutmut_15, 
    'x_max_product__mutmut_16': x_max_product__mutmut_16, 
    'x_max_product__mutmut_17': x_max_product__mutmut_17, 
    'x_max_product__mutmut_18': x_max_product__mutmut_18, 
    'x_max_product__mutmut_19': x_max_product__mutmut_19, 
    'x_max_product__mutmut_20': x_max_product__mutmut_20
}

def max_product(*args, **kwargs):
  result = _mutmut_trampoline(x_max_product__mutmut_orig, x_max_product__mutmut_mutants, args, kwargs)
  return result 

max_product.__signature__ = _mutmut_signature(x_max_product__mutmut_orig)
x_max_product__mutmut_orig.__name__ = 'x_max_product'