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
def x_drop_empty__mutmut_orig(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1
def x_drop_empty__mutmut_1(dict1):
  dict1 = None
  return dict1
def x_drop_empty__mutmut_2(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is None}
  return dict1

x_drop_empty__mutmut_mutants : ClassVar[MutantDict] = {
'x_drop_empty__mutmut_1': x_drop_empty__mutmut_1, 
    'x_drop_empty__mutmut_2': x_drop_empty__mutmut_2
}

def drop_empty(*args, **kwargs):
  result = _mutmut_trampoline(x_drop_empty__mutmut_orig, x_drop_empty__mutmut_mutants, args, kwargs)
  return result 

drop_empty.__signature__ = _mutmut_signature(x_drop_empty__mutmut_orig)
x_drop_empty__mutmut_orig.__name__ = 'x_drop_empty'