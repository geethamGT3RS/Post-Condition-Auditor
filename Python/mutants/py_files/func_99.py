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
def x_next_power_of_2__mutmut_orig(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_1(n): 
  if n or not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_2(n): 
  if n and n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_3(n): 
  if n and not n | (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_4(n): 
  if n and not n & (n + 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_5(n): 
  if n and not n & (n - 2):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_6(n): 
  if n and not n & (n - 1):
    return n

  count = None
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_7(n): 
  if n and not n & (n - 1):
    return n

  count = 1
  while n != 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_8(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n == 0: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_9(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 1: 
    n >>= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_10(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n = 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_11(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n <<= 1
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_12(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 2
    count += 1

  return 1 << count; 
def x_next_power_of_2__mutmut_13(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count = 1

  return 1 << count; 
def x_next_power_of_2__mutmut_14(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count -= 1

  return 1 << count; 
def x_next_power_of_2__mutmut_15(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 2

  return 1 << count; 
def x_next_power_of_2__mutmut_16(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 1 >> count; 
def x_next_power_of_2__mutmut_17(n): 
  if n and not n & (n - 1):
    return n

  count = 0
  while n != 0: 
    n >>= 1
    count += 1

  return 2 << count; 

x_next_power_of_2__mutmut_mutants : ClassVar[MutantDict] = {
'x_next_power_of_2__mutmut_1': x_next_power_of_2__mutmut_1, 
    'x_next_power_of_2__mutmut_2': x_next_power_of_2__mutmut_2, 
    'x_next_power_of_2__mutmut_3': x_next_power_of_2__mutmut_3, 
    'x_next_power_of_2__mutmut_4': x_next_power_of_2__mutmut_4, 
    'x_next_power_of_2__mutmut_5': x_next_power_of_2__mutmut_5, 
    'x_next_power_of_2__mutmut_6': x_next_power_of_2__mutmut_6, 
    'x_next_power_of_2__mutmut_7': x_next_power_of_2__mutmut_7, 
    'x_next_power_of_2__mutmut_8': x_next_power_of_2__mutmut_8, 
    'x_next_power_of_2__mutmut_9': x_next_power_of_2__mutmut_9, 
    'x_next_power_of_2__mutmut_10': x_next_power_of_2__mutmut_10, 
    'x_next_power_of_2__mutmut_11': x_next_power_of_2__mutmut_11, 
    'x_next_power_of_2__mutmut_12': x_next_power_of_2__mutmut_12, 
    'x_next_power_of_2__mutmut_13': x_next_power_of_2__mutmut_13, 
    'x_next_power_of_2__mutmut_14': x_next_power_of_2__mutmut_14, 
    'x_next_power_of_2__mutmut_15': x_next_power_of_2__mutmut_15, 
    'x_next_power_of_2__mutmut_16': x_next_power_of_2__mutmut_16, 
    'x_next_power_of_2__mutmut_17': x_next_power_of_2__mutmut_17
}

def next_power_of_2(*args, **kwargs):
  result = _mutmut_trampoline(x_next_power_of_2__mutmut_orig, x_next_power_of_2__mutmut_mutants, args, kwargs)
  return result 

next_power_of_2.__signature__ = _mutmut_signature(x_next_power_of_2__mutmut_orig)
x_next_power_of_2__mutmut_orig.__name__ = 'x_next_power_of_2'