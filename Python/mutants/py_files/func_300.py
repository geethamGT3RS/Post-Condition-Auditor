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
def x_removezero_ip__mutmut_orig(ip):
 string = re.sub('\.[0]*', '.', ip)
 return string
def x_removezero_ip__mutmut_1(ip):
 string = None
 return string
def x_removezero_ip__mutmut_2(ip):
 string = re.sub(None, '.', ip)
 return string
def x_removezero_ip__mutmut_3(ip):
 string = re.sub('\.[0]*', None, ip)
 return string
def x_removezero_ip__mutmut_4(ip):
 string = re.sub('\.[0]*', '.', None)
 return string
def x_removezero_ip__mutmut_5(ip):
 string = re.sub('.', ip)
 return string
def x_removezero_ip__mutmut_6(ip):
 string = re.sub('\.[0]*', ip)
 return string
def x_removezero_ip__mutmut_7(ip):
 string = re.sub('\.[0]*', '.', )
 return string
def x_removezero_ip__mutmut_8(ip):
 string = re.sub('XX\.[0]*XX', '.', ip)
 return string
def x_removezero_ip__mutmut_9(ip):
 string = re.sub('\.[0]*', 'XX.XX', ip)
 return string

x_removezero_ip__mutmut_mutants : ClassVar[MutantDict] = {
'x_removezero_ip__mutmut_1': x_removezero_ip__mutmut_1, 
    'x_removezero_ip__mutmut_2': x_removezero_ip__mutmut_2, 
    'x_removezero_ip__mutmut_3': x_removezero_ip__mutmut_3, 
    'x_removezero_ip__mutmut_4': x_removezero_ip__mutmut_4, 
    'x_removezero_ip__mutmut_5': x_removezero_ip__mutmut_5, 
    'x_removezero_ip__mutmut_6': x_removezero_ip__mutmut_6, 
    'x_removezero_ip__mutmut_7': x_removezero_ip__mutmut_7, 
    'x_removezero_ip__mutmut_8': x_removezero_ip__mutmut_8, 
    'x_removezero_ip__mutmut_9': x_removezero_ip__mutmut_9
}

def removezero_ip(*args, **kwargs):
 result = _mutmut_trampoline(x_removezero_ip__mutmut_orig, x_removezero_ip__mutmut_mutants, args, kwargs)
 return result 

removezero_ip.__signature__ = _mutmut_signature(x_removezero_ip__mutmut_orig)
x_removezero_ip__mutmut_orig.__name__ = 'x_removezero_ip'
