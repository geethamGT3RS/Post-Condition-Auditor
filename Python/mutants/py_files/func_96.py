import math 
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
def x_div_sum__mutmut_orig(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_1(n): 
  total = None
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_2(n): 
  total = 2
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_3(n): 
  total = 1
  i = None

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_4(n): 
  total = 1
  i = 3

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_5(n): 
  total = 1
  i = 2

  while i / i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_6(n): 
  total = 1
  i = 2

  while i * i < n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_7(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n / i == 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_8(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i != 0):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_9(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 1):
      total = (total + i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_10(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = None
    i += 1

  return total
def x_div_sum__mutmut_11(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i - math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_12(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total - i + math.floor(n / i))
    i += 1

  return total
def x_div_sum__mutmut_13(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(None))
    i += 1

  return total
def x_div_sum__mutmut_14(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n * i))
    i += 1

  return total
def x_div_sum__mutmut_15(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i = 1

  return total
def x_div_sum__mutmut_16(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i -= 1

  return total
def x_div_sum__mutmut_17(n): 
  total = 1
  i = 2

  while i * i <= n:
    if (n % i == 0):
      total = (total + i + math.floor(n / i))
    i += 2

  return total

x_div_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_div_sum__mutmut_1': x_div_sum__mutmut_1, 
    'x_div_sum__mutmut_2': x_div_sum__mutmut_2, 
    'x_div_sum__mutmut_3': x_div_sum__mutmut_3, 
    'x_div_sum__mutmut_4': x_div_sum__mutmut_4, 
    'x_div_sum__mutmut_5': x_div_sum__mutmut_5, 
    'x_div_sum__mutmut_6': x_div_sum__mutmut_6, 
    'x_div_sum__mutmut_7': x_div_sum__mutmut_7, 
    'x_div_sum__mutmut_8': x_div_sum__mutmut_8, 
    'x_div_sum__mutmut_9': x_div_sum__mutmut_9, 
    'x_div_sum__mutmut_10': x_div_sum__mutmut_10, 
    'x_div_sum__mutmut_11': x_div_sum__mutmut_11, 
    'x_div_sum__mutmut_12': x_div_sum__mutmut_12, 
    'x_div_sum__mutmut_13': x_div_sum__mutmut_13, 
    'x_div_sum__mutmut_14': x_div_sum__mutmut_14, 
    'x_div_sum__mutmut_15': x_div_sum__mutmut_15, 
    'x_div_sum__mutmut_16': x_div_sum__mutmut_16, 
    'x_div_sum__mutmut_17': x_div_sum__mutmut_17
}

def div_sum(*args, **kwargs):
  result = _mutmut_trampoline(x_div_sum__mutmut_orig, x_div_sum__mutmut_mutants, args, kwargs)
  return result 

div_sum.__signature__ = _mutmut_signature(x_div_sum__mutmut_orig)
x_div_sum__mutmut_orig.__name__ = 'x_div_sum'

def x_are_equivalent__mutmut_orig(num1, num2): 
    return div_sum(num1) == div_sum(num2); 

def x_are_equivalent__mutmut_1(num1, num2): 
    return div_sum(None) == div_sum(num2); 

def x_are_equivalent__mutmut_2(num1, num2): 
    return div_sum(num1) != div_sum(num2); 

def x_are_equivalent__mutmut_3(num1, num2): 
    return div_sum(num1) == div_sum(None); 

x_are_equivalent__mutmut_mutants : ClassVar[MutantDict] = {
'x_are_equivalent__mutmut_1': x_are_equivalent__mutmut_1, 
    'x_are_equivalent__mutmut_2': x_are_equivalent__mutmut_2, 
    'x_are_equivalent__mutmut_3': x_are_equivalent__mutmut_3
}

def are_equivalent(*args, **kwargs):
  result = _mutmut_trampoline(x_are_equivalent__mutmut_orig, x_are_equivalent__mutmut_mutants, args, kwargs)
  return result 

are_equivalent.__signature__ = _mutmut_signature(x_are_equivalent__mutmut_orig)
x_are_equivalent__mutmut_orig.__name__ = 'x_are_equivalent'