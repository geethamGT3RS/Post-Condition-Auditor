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
def x_find_adverbs__mutmut_orig(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_1(text):
  for m in re.finditer(None, text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_2(text):
  for m in re.finditer(r"\w+ly", None):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_3(text):
  for m in re.finditer(text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_4(text):
  for m in re.finditer(r"\w+ly", ):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_5(text):
  for m in re.finditer(r"XX\w+lyXX", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_6(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_7(text):
  for m in re.finditer(r"\w+LY", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_8(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' / (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_9(text):
  for m in re.finditer(r"\w+ly", text):
    return ('XX%d-%d: %sXX' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_10(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%D-%D: %S' % (m.start(), m.end(), m.group(0)))
def x_find_adverbs__mutmut_11(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(None)))
def x_find_adverbs__mutmut_12(text):
  for m in re.finditer(r"\w+ly", text):
    return ('%d-%d: %s' % (m.start(), m.end(), m.group(1)))

x_find_adverbs__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_adverbs__mutmut_1': x_find_adverbs__mutmut_1, 
    'x_find_adverbs__mutmut_2': x_find_adverbs__mutmut_2, 
    'x_find_adverbs__mutmut_3': x_find_adverbs__mutmut_3, 
    'x_find_adverbs__mutmut_4': x_find_adverbs__mutmut_4, 
    'x_find_adverbs__mutmut_5': x_find_adverbs__mutmut_5, 
    'x_find_adverbs__mutmut_6': x_find_adverbs__mutmut_6, 
    'x_find_adverbs__mutmut_7': x_find_adverbs__mutmut_7, 
    'x_find_adverbs__mutmut_8': x_find_adverbs__mutmut_8, 
    'x_find_adverbs__mutmut_9': x_find_adverbs__mutmut_9, 
    'x_find_adverbs__mutmut_10': x_find_adverbs__mutmut_10, 
    'x_find_adverbs__mutmut_11': x_find_adverbs__mutmut_11, 
    'x_find_adverbs__mutmut_12': x_find_adverbs__mutmut_12
}

def find_adverbs(*args, **kwargs):
  result = _mutmut_trampoline(x_find_adverbs__mutmut_orig, x_find_adverbs__mutmut_mutants, args, kwargs)
  return result 

find_adverbs.__signature__ = _mutmut_signature(x_find_adverbs__mutmut_orig)
x_find_adverbs__mutmut_orig.__name__ = 'x_find_adverbs'