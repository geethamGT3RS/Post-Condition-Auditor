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
def x_capital_words_spaces__mutmut_orig(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
def x_capital_words_spaces__mutmut_1(str1):
  return re.sub(None, r"\1 \2", str1)
def x_capital_words_spaces__mutmut_2(str1):
  return re.sub(r"(\w)([A-Z])", None, str1)
def x_capital_words_spaces__mutmut_3(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", None)
def x_capital_words_spaces__mutmut_4(str1):
  return re.sub(r"\1 \2", str1)
def x_capital_words_spaces__mutmut_5(str1):
  return re.sub(r"(\w)([A-Z])", str1)
def x_capital_words_spaces__mutmut_6(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", )
def x_capital_words_spaces__mutmut_7(str1):
  return re.sub(r"XX(\w)([A-Z])XX", r"\1 \2", str1)
def x_capital_words_spaces__mutmut_8(str1):
  return re.sub(r"(\w)([a-z])", r"\1 \2", str1)
def x_capital_words_spaces__mutmut_9(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
def x_capital_words_spaces__mutmut_10(str1):
  return re.sub(r"(\w)([A-Z])", r"XX\1 \2XX", str1)
def x_capital_words_spaces__mutmut_11(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
def x_capital_words_spaces__mutmut_12(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

x_capital_words_spaces__mutmut_mutants : ClassVar[MutantDict] = {
'x_capital_words_spaces__mutmut_1': x_capital_words_spaces__mutmut_1, 
    'x_capital_words_spaces__mutmut_2': x_capital_words_spaces__mutmut_2, 
    'x_capital_words_spaces__mutmut_3': x_capital_words_spaces__mutmut_3, 
    'x_capital_words_spaces__mutmut_4': x_capital_words_spaces__mutmut_4, 
    'x_capital_words_spaces__mutmut_5': x_capital_words_spaces__mutmut_5, 
    'x_capital_words_spaces__mutmut_6': x_capital_words_spaces__mutmut_6, 
    'x_capital_words_spaces__mutmut_7': x_capital_words_spaces__mutmut_7, 
    'x_capital_words_spaces__mutmut_8': x_capital_words_spaces__mutmut_8, 
    'x_capital_words_spaces__mutmut_9': x_capital_words_spaces__mutmut_9, 
    'x_capital_words_spaces__mutmut_10': x_capital_words_spaces__mutmut_10, 
    'x_capital_words_spaces__mutmut_11': x_capital_words_spaces__mutmut_11, 
    'x_capital_words_spaces__mutmut_12': x_capital_words_spaces__mutmut_12
}

def capital_words_spaces(*args, **kwargs):
  result = _mutmut_trampoline(x_capital_words_spaces__mutmut_orig, x_capital_words_spaces__mutmut_mutants, args, kwargs)
  return result 

capital_words_spaces.__signature__ = _mutmut_signature(x_capital_words_spaces__mutmut_orig)
x_capital_words_spaces__mutmut_orig.__name__ = 'x_capital_words_spaces'