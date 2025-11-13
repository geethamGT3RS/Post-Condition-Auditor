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
def x_replace_spaces__mutmut_orig(text):
  return "".join(" " if c == "_" else ("_" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_1(text):
  return "".join(None)
def x_replace_spaces__mutmut_2(text):
  return "XXXX".join(" " if c == "_" else ("_" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_3(text):
  return "".join("XX XX" if c == "_" else ("_" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_4(text):
  return "".join(" " if c != "_" else ("_" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_5(text):
  return "".join(" " if c == "XX_XX" else ("_" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_6(text):
  return "".join(" " if c == "_" else ("XX_XX" if c == " " else c) for c in text)
def x_replace_spaces__mutmut_7(text):
  return "".join(" " if c == "_" else ("_" if c != " " else c) for c in text)
def x_replace_spaces__mutmut_8(text):
  return "".join(" " if c == "_" else ("_" if c == "XX XX" else c) for c in text)

x_replace_spaces__mutmut_mutants : ClassVar[MutantDict] = {
'x_replace_spaces__mutmut_1': x_replace_spaces__mutmut_1, 
    'x_replace_spaces__mutmut_2': x_replace_spaces__mutmut_2, 
    'x_replace_spaces__mutmut_3': x_replace_spaces__mutmut_3, 
    'x_replace_spaces__mutmut_4': x_replace_spaces__mutmut_4, 
    'x_replace_spaces__mutmut_5': x_replace_spaces__mutmut_5, 
    'x_replace_spaces__mutmut_6': x_replace_spaces__mutmut_6, 
    'x_replace_spaces__mutmut_7': x_replace_spaces__mutmut_7, 
    'x_replace_spaces__mutmut_8': x_replace_spaces__mutmut_8
}

def replace_spaces(*args, **kwargs):
  result = _mutmut_trampoline(x_replace_spaces__mutmut_orig, x_replace_spaces__mutmut_mutants, args, kwargs)
  return result 

replace_spaces.__signature__ = _mutmut_signature(x_replace_spaces__mutmut_orig)
x_replace_spaces__mutmut_orig.__name__ = 'x_replace_spaces'