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
def x_sample_nam__mutmut_orig(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_1(sample_names):
  sample_names=None
  return len(''.join(sample_names))
def x_sample_nam__mutmut_2(sample_names):
  sample_names=list(None)
  return len(''.join(sample_names))
def x_sample_nam__mutmut_3(sample_names):
  sample_names=list(filter(None,sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_4(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),None))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_5(sample_names):
  sample_names=list(filter(sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_6(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_7(sample_names):
  sample_names=list(filter(lambda el:None,sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_8(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() or el[1:].islower(),sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_9(sample_names):
  sample_names=list(filter(lambda el:el[1].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))
def x_sample_nam__mutmut_10(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[2:].islower(),sample_names))
  return len(''.join(sample_names))

x_sample_nam__mutmut_mutants : ClassVar[MutantDict] = {
'x_sample_nam__mutmut_1': x_sample_nam__mutmut_1, 
    'x_sample_nam__mutmut_2': x_sample_nam__mutmut_2, 
    'x_sample_nam__mutmut_3': x_sample_nam__mutmut_3, 
    'x_sample_nam__mutmut_4': x_sample_nam__mutmut_4, 
    'x_sample_nam__mutmut_5': x_sample_nam__mutmut_5, 
    'x_sample_nam__mutmut_6': x_sample_nam__mutmut_6, 
    'x_sample_nam__mutmut_7': x_sample_nam__mutmut_7, 
    'x_sample_nam__mutmut_8': x_sample_nam__mutmut_8, 
    'x_sample_nam__mutmut_9': x_sample_nam__mutmut_9, 
    'x_sample_nam__mutmut_10': x_sample_nam__mutmut_10
}

def sample_nam(*args, **kwargs):
  result = _mutmut_trampoline(x_sample_nam__mutmut_orig, x_sample_nam__mutmut_mutants, args, kwargs)
  return result 

sample_nam.__signature__ = _mutmut_signature(x_sample_nam__mutmut_orig)
x_sample_nam__mutmut_orig.__name__ = 'x_sample_nam'