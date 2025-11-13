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
def x_geometric_sum__mutmut_orig(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_1(n):
  if n <= 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_2(n):
  if n < 1:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_3(n):
  if n < 0:
    return 1
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_4(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) - geometric_sum(n - 1)
def x_geometric_sum__mutmut_5(n):
  if n < 0:
    return 0
  else:
    return 1 * (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_6(n):
  if n < 0:
    return 0
  else:
    return 2 / (pow(2, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_7(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(None, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_8(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, None)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_9(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_10(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, )) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_11(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(3, n)) + geometric_sum(n - 1)
def x_geometric_sum__mutmut_12(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(None)
def x_geometric_sum__mutmut_13(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n + 1)
def x_geometric_sum__mutmut_14(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 2)

x_geometric_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_geometric_sum__mutmut_1': x_geometric_sum__mutmut_1, 
    'x_geometric_sum__mutmut_2': x_geometric_sum__mutmut_2, 
    'x_geometric_sum__mutmut_3': x_geometric_sum__mutmut_3, 
    'x_geometric_sum__mutmut_4': x_geometric_sum__mutmut_4, 
    'x_geometric_sum__mutmut_5': x_geometric_sum__mutmut_5, 
    'x_geometric_sum__mutmut_6': x_geometric_sum__mutmut_6, 
    'x_geometric_sum__mutmut_7': x_geometric_sum__mutmut_7, 
    'x_geometric_sum__mutmut_8': x_geometric_sum__mutmut_8, 
    'x_geometric_sum__mutmut_9': x_geometric_sum__mutmut_9, 
    'x_geometric_sum__mutmut_10': x_geometric_sum__mutmut_10, 
    'x_geometric_sum__mutmut_11': x_geometric_sum__mutmut_11, 
    'x_geometric_sum__mutmut_12': x_geometric_sum__mutmut_12, 
    'x_geometric_sum__mutmut_13': x_geometric_sum__mutmut_13, 
    'x_geometric_sum__mutmut_14': x_geometric_sum__mutmut_14
}

def geometric_sum(*args, **kwargs):
  result = _mutmut_trampoline(x_geometric_sum__mutmut_orig, x_geometric_sum__mutmut_mutants, args, kwargs)
  return result 

geometric_sum.__signature__ = _mutmut_signature(x_geometric_sum__mutmut_orig)
x_geometric_sum__mutmut_orig.__name__ = 'x_geometric_sum'