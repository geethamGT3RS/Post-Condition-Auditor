import cmath
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
def x_angle_complex__mutmut_orig(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_1(a,b):
  cn=None
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_2(a,b):
  cn=complex(None,b)
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_3(a,b):
  cn=complex(a,None)
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_4(a,b):
  cn=complex(b)
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_5(a,b):
  cn=complex(a,)
  angle=cmath.phase(a+b)
  return angle
def x_angle_complex__mutmut_6(a,b):
  cn=complex(a,b)
  angle=None
  return angle
def x_angle_complex__mutmut_7(a,b):
  cn=complex(a,b)
  angle=cmath.phase(None)
  return angle
def x_angle_complex__mutmut_8(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a - b)
  return angle

x_angle_complex__mutmut_mutants : ClassVar[MutantDict] = {
'x_angle_complex__mutmut_1': x_angle_complex__mutmut_1, 
    'x_angle_complex__mutmut_2': x_angle_complex__mutmut_2, 
    'x_angle_complex__mutmut_3': x_angle_complex__mutmut_3, 
    'x_angle_complex__mutmut_4': x_angle_complex__mutmut_4, 
    'x_angle_complex__mutmut_5': x_angle_complex__mutmut_5, 
    'x_angle_complex__mutmut_6': x_angle_complex__mutmut_6, 
    'x_angle_complex__mutmut_7': x_angle_complex__mutmut_7, 
    'x_angle_complex__mutmut_8': x_angle_complex__mutmut_8
}

def angle_complex(*args, **kwargs):
  result = _mutmut_trampoline(x_angle_complex__mutmut_orig, x_angle_complex__mutmut_mutants, args, kwargs)
  return result 

angle_complex.__signature__ = _mutmut_signature(x_angle_complex__mutmut_orig)
x_angle_complex__mutmut_orig.__name__ = 'x_angle_complex'