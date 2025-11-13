from math import tan, pi
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
def x_area_polygon__mutmut_orig(s, l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area
def x_area_polygon__mutmut_1(s, l):
  area = None
  return area
def x_area_polygon__mutmut_2(s, l):
  area = s * (l ** 2) * (4 * tan(pi / s))
  return area
def x_area_polygon__mutmut_3(s, l):
  area = s / (l ** 2) / (4 * tan(pi / s))
  return area
def x_area_polygon__mutmut_4(s, l):
  area = s * (l * 2) / (4 * tan(pi / s))
  return area
def x_area_polygon__mutmut_5(s, l):
  area = s * (l ** 3) / (4 * tan(pi / s))
  return area
def x_area_polygon__mutmut_6(s, l):
  area = s * (l ** 2) / (4 / tan(pi / s))
  return area
def x_area_polygon__mutmut_7(s, l):
  area = s * (l ** 2) / (5 * tan(pi / s))
  return area
def x_area_polygon__mutmut_8(s, l):
  area = s * (l ** 2) / (4 * tan(None))
  return area
def x_area_polygon__mutmut_9(s, l):
  area = s * (l ** 2) / (4 * tan(pi * s))
  return area

x_area_polygon__mutmut_mutants : ClassVar[MutantDict] = {
'x_area_polygon__mutmut_1': x_area_polygon__mutmut_1, 
    'x_area_polygon__mutmut_2': x_area_polygon__mutmut_2, 
    'x_area_polygon__mutmut_3': x_area_polygon__mutmut_3, 
    'x_area_polygon__mutmut_4': x_area_polygon__mutmut_4, 
    'x_area_polygon__mutmut_5': x_area_polygon__mutmut_5, 
    'x_area_polygon__mutmut_6': x_area_polygon__mutmut_6, 
    'x_area_polygon__mutmut_7': x_area_polygon__mutmut_7, 
    'x_area_polygon__mutmut_8': x_area_polygon__mutmut_8, 
    'x_area_polygon__mutmut_9': x_area_polygon__mutmut_9
}

def area_polygon(*args, **kwargs):
  result = _mutmut_trampoline(x_area_polygon__mutmut_orig, x_area_polygon__mutmut_mutants, args, kwargs)
  return result 

area_polygon.__signature__ = _mutmut_signature(x_area_polygon__mutmut_orig)
x_area_polygon__mutmut_orig.__name__ = 'x_area_polygon'