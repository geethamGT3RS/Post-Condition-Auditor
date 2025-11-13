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
def x_round_and_sum__mutmut_orig(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_1(list1):
  lenght=None
  round_and_sum=sum(list(map(round,list1))* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_2(list1):
  lenght=len(list1)
  round_and_sum=None
  return round_and_sum
def x_round_and_sum__mutmut_3(list1):
  lenght=len(list1)
  round_and_sum=sum(None)
  return round_and_sum
def x_round_and_sum__mutmut_4(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,list1)) / lenght)
  return round_and_sum
def x_round_and_sum__mutmut_5(list1):
  lenght=len(list1)
  round_and_sum=sum(list(None)* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_6(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(None,list1))* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_7(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,None))* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_8(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(list1))* lenght)
  return round_and_sum
def x_round_and_sum__mutmut_9(list1):
  lenght=len(list1)
  round_and_sum=sum(list(map(round,))* lenght)
  return round_and_sum

x_round_and_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_round_and_sum__mutmut_1': x_round_and_sum__mutmut_1, 
    'x_round_and_sum__mutmut_2': x_round_and_sum__mutmut_2, 
    'x_round_and_sum__mutmut_3': x_round_and_sum__mutmut_3, 
    'x_round_and_sum__mutmut_4': x_round_and_sum__mutmut_4, 
    'x_round_and_sum__mutmut_5': x_round_and_sum__mutmut_5, 
    'x_round_and_sum__mutmut_6': x_round_and_sum__mutmut_6, 
    'x_round_and_sum__mutmut_7': x_round_and_sum__mutmut_7, 
    'x_round_and_sum__mutmut_8': x_round_and_sum__mutmut_8, 
    'x_round_and_sum__mutmut_9': x_round_and_sum__mutmut_9
}

def round_and_sum(*args, **kwargs):
  result = _mutmut_trampoline(x_round_and_sum__mutmut_orig, x_round_and_sum__mutmut_mutants, args, kwargs)
  return result 

round_and_sum.__signature__ = _mutmut_signature(x_round_and_sum__mutmut_orig)
x_round_and_sum__mutmut_orig.__name__ = 'x_round_and_sum'