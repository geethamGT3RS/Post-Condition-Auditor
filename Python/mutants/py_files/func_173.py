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
def x_start_withp__mutmut_orig(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()
def x_start_withp__mutmut_1(words):
 for w in words:
        m = None
        if m:
            return m.groups()
def x_start_withp__mutmut_2(words):
 for w in words:
        m = re.match(None, w)
        if m:
            return m.groups()
def x_start_withp__mutmut_3(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", None)
        if m:
            return m.groups()
def x_start_withp__mutmut_4(words):
 for w in words:
        m = re.match(w)
        if m:
            return m.groups()
def x_start_withp__mutmut_5(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", )
        if m:
            return m.groups()
def x_start_withp__mutmut_6(words):
 for w in words:
        m = re.match("XX(P\w+)\W(P\w+)XX", w)
        if m:
            return m.groups()
def x_start_withp__mutmut_7(words):
 for w in words:
        m = re.match("(p\w+)\W(p\w+)", w)
        if m:
            return m.groups()

x_start_withp__mutmut_mutants : ClassVar[MutantDict] = {
'x_start_withp__mutmut_1': x_start_withp__mutmut_1, 
    'x_start_withp__mutmut_2': x_start_withp__mutmut_2, 
    'x_start_withp__mutmut_3': x_start_withp__mutmut_3, 
    'x_start_withp__mutmut_4': x_start_withp__mutmut_4, 
    'x_start_withp__mutmut_5': x_start_withp__mutmut_5, 
    'x_start_withp__mutmut_6': x_start_withp__mutmut_6, 
    'x_start_withp__mutmut_7': x_start_withp__mutmut_7
}

def start_withp(*args, **kwargs):
 result = _mutmut_trampoline(x_start_withp__mutmut_orig, x_start_withp__mutmut_mutants, args, kwargs)
 return result 

start_withp.__signature__ = _mutmut_signature(x_start_withp__mutmut_orig)
x_start_withp__mutmut_orig.__name__ = 'x_start_withp'