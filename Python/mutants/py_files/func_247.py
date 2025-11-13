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
def x_remove_uppercase__mutmut_orig(str1):
  return re.sub('[A-Z]', '', str1)
def x_remove_uppercase__mutmut_1(str1):
  return re.sub(None, '', str1)
def x_remove_uppercase__mutmut_2(str1):
  return re.sub('[A-Z]', None, str1)
def x_remove_uppercase__mutmut_3(str1):
  return re.sub('[A-Z]', '', None)
def x_remove_uppercase__mutmut_4(str1):
  return re.sub('', str1)
def x_remove_uppercase__mutmut_5(str1):
  return re.sub('[A-Z]', str1)
def x_remove_uppercase__mutmut_6(str1):
  return re.sub('[A-Z]', '', )
def x_remove_uppercase__mutmut_7(str1):
  return re.sub('XX[A-Z]XX', '', str1)
def x_remove_uppercase__mutmut_8(str1):
  return re.sub('[a-z]', '', str1)
def x_remove_uppercase__mutmut_9(str1):
  return re.sub('[A-Z]', 'XXXX', str1)

x_remove_uppercase__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_uppercase__mutmut_1': x_remove_uppercase__mutmut_1, 
    'x_remove_uppercase__mutmut_2': x_remove_uppercase__mutmut_2, 
    'x_remove_uppercase__mutmut_3': x_remove_uppercase__mutmut_3, 
    'x_remove_uppercase__mutmut_4': x_remove_uppercase__mutmut_4, 
    'x_remove_uppercase__mutmut_5': x_remove_uppercase__mutmut_5, 
    'x_remove_uppercase__mutmut_6': x_remove_uppercase__mutmut_6, 
    'x_remove_uppercase__mutmut_7': x_remove_uppercase__mutmut_7, 
    'x_remove_uppercase__mutmut_8': x_remove_uppercase__mutmut_8, 
    'x_remove_uppercase__mutmut_9': x_remove_uppercase__mutmut_9
}

def remove_uppercase(*args, **kwargs):
  result = _mutmut_trampoline(x_remove_uppercase__mutmut_orig, x_remove_uppercase__mutmut_mutants, args, kwargs)
  return result 

remove_uppercase.__signature__ = _mutmut_signature(x_remove_uppercase__mutmut_orig)
x_remove_uppercase__mutmut_orig.__name__ = 'x_remove_uppercase'