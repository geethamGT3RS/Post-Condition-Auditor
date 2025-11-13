import re
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
def x_snake_to_camel__mutmut_orig(word):
  return ''.join(x.capitalize() or '_' for x in word.split('_'))
def x_snake_to_camel__mutmut_1(word):
  return ''.join(None)
def x_snake_to_camel__mutmut_2(word):
  return 'XXXX'.join(x.capitalize() or '_' for x in word.split('_'))
def x_snake_to_camel__mutmut_3(word):
  return ''.join(x.capitalize() and '_' for x in word.split('_'))
def x_snake_to_camel__mutmut_4(word):
  return ''.join(x.capitalize() or 'XX_XX' for x in word.split('_'))
def x_snake_to_camel__mutmut_5(word):
  return ''.join(x.capitalize() or '_' for x in word.split(None))
def x_snake_to_camel__mutmut_6(word):
  return ''.join(x.capitalize() or '_' for x in word.split('XX_XX'))

x_snake_to_camel__mutmut_mutants : ClassVar[MutantDict] = {
'x_snake_to_camel__mutmut_1': x_snake_to_camel__mutmut_1, 
    'x_snake_to_camel__mutmut_2': x_snake_to_camel__mutmut_2, 
    'x_snake_to_camel__mutmut_3': x_snake_to_camel__mutmut_3, 
    'x_snake_to_camel__mutmut_4': x_snake_to_camel__mutmut_4, 
    'x_snake_to_camel__mutmut_5': x_snake_to_camel__mutmut_5, 
    'x_snake_to_camel__mutmut_6': x_snake_to_camel__mutmut_6
}

def snake_to_camel(*args, **kwargs):
  result = _mutmut_trampoline(x_snake_to_camel__mutmut_orig, x_snake_to_camel__mutmut_mutants, args, kwargs)
  return result 

snake_to_camel.__signature__ = _mutmut_signature(x_snake_to_camel__mutmut_orig)
x_snake_to_camel__mutmut_orig.__name__ = 'x_snake_to_camel'