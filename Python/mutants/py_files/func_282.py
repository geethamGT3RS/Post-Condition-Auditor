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
def x_surfacearea_cylinder__mutmut_orig(r,h):
  surfacearea=((2*3.1415*r*r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_1(r,h):
  surfacearea=None
  return surfacearea
def x_surfacearea_cylinder__mutmut_2(r,h):
  surfacearea=((2*3.1415*r*r) - (2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_3(r,h):
  surfacearea=((2*3.1415*r / r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_4(r,h):
  surfacearea=((2*3.1415 / r*r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_5(r,h):
  surfacearea=((2 / 3.1415*r*r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_6(r,h):
  surfacearea=((3*3.1415*r*r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_7(r,h):
  surfacearea=((2*4.141500000000001*r*r) +(2*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_8(r,h):
  surfacearea=((2*3.1415*r*r) +(2*3.1415*r / h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_9(r,h):
  surfacearea=((2*3.1415*r*r) +(2*3.1415 / r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_10(r,h):
  surfacearea=((2*3.1415*r*r) +(2 / 3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_11(r,h):
  surfacearea=((2*3.1415*r*r) +(3*3.1415*r*h))
  return surfacearea
def x_surfacearea_cylinder__mutmut_12(r,h):
  surfacearea=((2*3.1415*r*r) +(2*4.141500000000001*r*h))
  return surfacearea

x_surfacearea_cylinder__mutmut_mutants : ClassVar[MutantDict] = {
'x_surfacearea_cylinder__mutmut_1': x_surfacearea_cylinder__mutmut_1, 
    'x_surfacearea_cylinder__mutmut_2': x_surfacearea_cylinder__mutmut_2, 
    'x_surfacearea_cylinder__mutmut_3': x_surfacearea_cylinder__mutmut_3, 
    'x_surfacearea_cylinder__mutmut_4': x_surfacearea_cylinder__mutmut_4, 
    'x_surfacearea_cylinder__mutmut_5': x_surfacearea_cylinder__mutmut_5, 
    'x_surfacearea_cylinder__mutmut_6': x_surfacearea_cylinder__mutmut_6, 
    'x_surfacearea_cylinder__mutmut_7': x_surfacearea_cylinder__mutmut_7, 
    'x_surfacearea_cylinder__mutmut_8': x_surfacearea_cylinder__mutmut_8, 
    'x_surfacearea_cylinder__mutmut_9': x_surfacearea_cylinder__mutmut_9, 
    'x_surfacearea_cylinder__mutmut_10': x_surfacearea_cylinder__mutmut_10, 
    'x_surfacearea_cylinder__mutmut_11': x_surfacearea_cylinder__mutmut_11, 
    'x_surfacearea_cylinder__mutmut_12': x_surfacearea_cylinder__mutmut_12
}

def surfacearea_cylinder(*args, **kwargs):
  result = _mutmut_trampoline(x_surfacearea_cylinder__mutmut_orig, x_surfacearea_cylinder__mutmut_mutants, args, kwargs)
  return result 

surfacearea_cylinder.__signature__ = _mutmut_signature(x_surfacearea_cylinder__mutmut_orig)
x_surfacearea_cylinder__mutmut_orig.__name__ = 'x_surfacearea_cylinder'