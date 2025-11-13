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
def x_volume_cone__mutmut_orig(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume
def x_volume_cone__mutmut_1(r,h):
  volume = None
  return volume
def x_volume_cone__mutmut_2(r,h):
  volume = (1.0/3) * math.pi * r * r / h
  return volume
def x_volume_cone__mutmut_3(r,h):
  volume = (1.0/3) * math.pi * r / r * h
  return volume
def x_volume_cone__mutmut_4(r,h):
  volume = (1.0/3) * math.pi / r * r * h
  return volume
def x_volume_cone__mutmut_5(r,h):
  volume = (1.0/3) / math.pi * r * r * h
  return volume
def x_volume_cone__mutmut_6(r,h):
  volume = (1.0 * 3) * math.pi * r * r * h
  return volume
def x_volume_cone__mutmut_7(r,h):
  volume = (2.0/3) * math.pi * r * r * h
  return volume
def x_volume_cone__mutmut_8(r,h):
  volume = (1.0/4) * math.pi * r * r * h
  return volume

x_volume_cone__mutmut_mutants : ClassVar[MutantDict] = {
'x_volume_cone__mutmut_1': x_volume_cone__mutmut_1, 
    'x_volume_cone__mutmut_2': x_volume_cone__mutmut_2, 
    'x_volume_cone__mutmut_3': x_volume_cone__mutmut_3, 
    'x_volume_cone__mutmut_4': x_volume_cone__mutmut_4, 
    'x_volume_cone__mutmut_5': x_volume_cone__mutmut_5, 
    'x_volume_cone__mutmut_6': x_volume_cone__mutmut_6, 
    'x_volume_cone__mutmut_7': x_volume_cone__mutmut_7, 
    'x_volume_cone__mutmut_8': x_volume_cone__mutmut_8
}

def volume_cone(*args, **kwargs):
  result = _mutmut_trampoline(x_volume_cone__mutmut_orig, x_volume_cone__mutmut_mutants, args, kwargs)
  return result 

volume_cone.__signature__ = _mutmut_signature(x_volume_cone__mutmut_orig)
x_volume_cone__mutmut_orig.__name__ = 'x_volume_cone'