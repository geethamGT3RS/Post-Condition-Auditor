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
def x_multiple_to_single__mutmut_orig(L):
  x = int("".join(map(str, L)))
  return x
def x_multiple_to_single__mutmut_1(L):
  x = None
  return x
def x_multiple_to_single__mutmut_2(L):
  x = int(None)
  return x
def x_multiple_to_single__mutmut_3(L):
  x = int("".join(None))
  return x
def x_multiple_to_single__mutmut_4(L):
  x = int("XXXX".join(map(str, L)))
  return x
def x_multiple_to_single__mutmut_5(L):
  x = int("".join(map(None, L)))
  return x
def x_multiple_to_single__mutmut_6(L):
  x = int("".join(map(str, None)))
  return x
def x_multiple_to_single__mutmut_7(L):
  x = int("".join(map(L)))
  return x
def x_multiple_to_single__mutmut_8(L):
  x = int("".join(map(str, )))
  return x

x_multiple_to_single__mutmut_mutants : ClassVar[MutantDict] = {
'x_multiple_to_single__mutmut_1': x_multiple_to_single__mutmut_1, 
    'x_multiple_to_single__mutmut_2': x_multiple_to_single__mutmut_2, 
    'x_multiple_to_single__mutmut_3': x_multiple_to_single__mutmut_3, 
    'x_multiple_to_single__mutmut_4': x_multiple_to_single__mutmut_4, 
    'x_multiple_to_single__mutmut_5': x_multiple_to_single__mutmut_5, 
    'x_multiple_to_single__mutmut_6': x_multiple_to_single__mutmut_6, 
    'x_multiple_to_single__mutmut_7': x_multiple_to_single__mutmut_7, 
    'x_multiple_to_single__mutmut_8': x_multiple_to_single__mutmut_8
}

def multiple_to_single(*args, **kwargs):
  result = _mutmut_trampoline(x_multiple_to_single__mutmut_orig, x_multiple_to_single__mutmut_mutants, args, kwargs)
  return result 

multiple_to_single.__signature__ = _mutmut_signature(x_multiple_to_single__mutmut_orig)
x_multiple_to_single__mutmut_orig.__name__ = 'x_multiple_to_single'