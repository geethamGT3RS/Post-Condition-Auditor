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
def x_remove_odd__mutmut_orig(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_1(str1):
 str2 = None
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_2(str1):
 str2 = 'XXXX'
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_3(str1):
 str2 = ''
 for i in range(None, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_4(str1):
 str2 = ''
 for i in range(1, None):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_5(str1):
 str2 = ''
 for i in range(len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_6(str1):
 str2 = ''
 for i in range(1, ):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_7(str1):
 str2 = ''
 for i in range(2, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_8(str1):
 str2 = ''
 for i in range(1, len(str1) - 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_9(str1):
 str2 = ''
 for i in range(1, len(str1) + 2):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_10(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i / 2 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_11(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 3 == 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_12(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 != 0):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_13(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 1):
        str2 = str2 + str1[i - 1]
 return str2
def x_remove_odd__mutmut_14(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = None
 return str2
def x_remove_odd__mutmut_15(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 - str1[i - 1]
 return str2
def x_remove_odd__mutmut_16(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i + 1]
 return str2
def x_remove_odd__mutmut_17(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 == 0):
        str2 = str2 + str1[i - 2]
 return str2

x_remove_odd__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_odd__mutmut_1': x_remove_odd__mutmut_1, 
    'x_remove_odd__mutmut_2': x_remove_odd__mutmut_2, 
    'x_remove_odd__mutmut_3': x_remove_odd__mutmut_3, 
    'x_remove_odd__mutmut_4': x_remove_odd__mutmut_4, 
    'x_remove_odd__mutmut_5': x_remove_odd__mutmut_5, 
    'x_remove_odd__mutmut_6': x_remove_odd__mutmut_6, 
    'x_remove_odd__mutmut_7': x_remove_odd__mutmut_7, 
    'x_remove_odd__mutmut_8': x_remove_odd__mutmut_8, 
    'x_remove_odd__mutmut_9': x_remove_odd__mutmut_9, 
    'x_remove_odd__mutmut_10': x_remove_odd__mutmut_10, 
    'x_remove_odd__mutmut_11': x_remove_odd__mutmut_11, 
    'x_remove_odd__mutmut_12': x_remove_odd__mutmut_12, 
    'x_remove_odd__mutmut_13': x_remove_odd__mutmut_13, 
    'x_remove_odd__mutmut_14': x_remove_odd__mutmut_14, 
    'x_remove_odd__mutmut_15': x_remove_odd__mutmut_15, 
    'x_remove_odd__mutmut_16': x_remove_odd__mutmut_16, 
    'x_remove_odd__mutmut_17': x_remove_odd__mutmut_17
}

def remove_odd(*args, **kwargs):
 result = _mutmut_trampoline(x_remove_odd__mutmut_orig, x_remove_odd__mutmut_mutants, args, kwargs)
 return result 

remove_odd.__signature__ = _mutmut_signature(x_remove_odd__mutmut_orig)
x_remove_odd__mutmut_orig.__name__ = 'x_remove_odd'