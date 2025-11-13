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
def x_count_occurance__mutmut_orig(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_1(s):
  count = None
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_2(s):
  count = 1
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_3(s):
  count = 0
  for i in range(None):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_4(s):
  count = 0
  for i in range(len(s) + 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_5(s):
  count = 0
  for i in range(len(s) - 3):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_6(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' or s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_7(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' or s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_8(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] != 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_9(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 'XXsXX' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_10(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 'S' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_11(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i - 1] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_12(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+2] == 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_13(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] != 't' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_14(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 'XXtXX' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_15(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 'T' and s[i+2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_16(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i - 2] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_17(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+3] == 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_18(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] != 'd'):
      count = count + 1
  return count
def x_count_occurance__mutmut_19(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'XXdXX'):
      count = count + 1
  return count
def x_count_occurance__mutmut_20(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'D'):
      count = count + 1
  return count
def x_count_occurance__mutmut_21(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = None
  return count
def x_count_occurance__mutmut_22(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count - 1
  return count
def x_count_occurance__mutmut_23(s):
  count = 0
  for i in range(len(s) - 2):
    if (s[i] == 's' and s[i+1] == 't' and s[i+2] == 'd'):
      count = count + 2
  return count

x_count_occurance__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_occurance__mutmut_1': x_count_occurance__mutmut_1, 
    'x_count_occurance__mutmut_2': x_count_occurance__mutmut_2, 
    'x_count_occurance__mutmut_3': x_count_occurance__mutmut_3, 
    'x_count_occurance__mutmut_4': x_count_occurance__mutmut_4, 
    'x_count_occurance__mutmut_5': x_count_occurance__mutmut_5, 
    'x_count_occurance__mutmut_6': x_count_occurance__mutmut_6, 
    'x_count_occurance__mutmut_7': x_count_occurance__mutmut_7, 
    'x_count_occurance__mutmut_8': x_count_occurance__mutmut_8, 
    'x_count_occurance__mutmut_9': x_count_occurance__mutmut_9, 
    'x_count_occurance__mutmut_10': x_count_occurance__mutmut_10, 
    'x_count_occurance__mutmut_11': x_count_occurance__mutmut_11, 
    'x_count_occurance__mutmut_12': x_count_occurance__mutmut_12, 
    'x_count_occurance__mutmut_13': x_count_occurance__mutmut_13, 
    'x_count_occurance__mutmut_14': x_count_occurance__mutmut_14, 
    'x_count_occurance__mutmut_15': x_count_occurance__mutmut_15, 
    'x_count_occurance__mutmut_16': x_count_occurance__mutmut_16, 
    'x_count_occurance__mutmut_17': x_count_occurance__mutmut_17, 
    'x_count_occurance__mutmut_18': x_count_occurance__mutmut_18, 
    'x_count_occurance__mutmut_19': x_count_occurance__mutmut_19, 
    'x_count_occurance__mutmut_20': x_count_occurance__mutmut_20, 
    'x_count_occurance__mutmut_21': x_count_occurance__mutmut_21, 
    'x_count_occurance__mutmut_22': x_count_occurance__mutmut_22, 
    'x_count_occurance__mutmut_23': x_count_occurance__mutmut_23
}

def count_occurance(*args, **kwargs):
  result = _mutmut_trampoline(x_count_occurance__mutmut_orig, x_count_occurance__mutmut_mutants, args, kwargs)
  return result 

count_occurance.__signature__ = _mutmut_signature(x_count_occurance__mutmut_orig)
x_count_occurance__mutmut_orig.__name__ = 'x_count_occurance'