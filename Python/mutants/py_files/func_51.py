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
def x_divisor__mutmut_orig(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
def x_divisor__mutmut_1(n):
  for i in range(None):
    x = len([i for i in range(1,n+1) if not n % i])
  return x
def x_divisor__mutmut_2(n):
  for i in range(n):
    x = None
  return x

x_divisor__mutmut_mutants : ClassVar[MutantDict] = {
'x_divisor__mutmut_1': x_divisor__mutmut_1, 
    'x_divisor__mutmut_2': x_divisor__mutmut_2
}

def divisor(*args, **kwargs):
  result = _mutmut_trampoline(x_divisor__mutmut_orig, x_divisor__mutmut_mutants, args, kwargs)
  return result 

divisor.__signature__ = _mutmut_signature(x_divisor__mutmut_orig)
x_divisor__mutmut_orig.__name__ = 'x_divisor'