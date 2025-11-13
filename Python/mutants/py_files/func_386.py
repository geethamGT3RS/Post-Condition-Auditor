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
def x_number_ctr__mutmut_orig(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_1(str):
      number_ctr= None
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_2(str):
      number_ctr= 1
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_3(str):
      number_ctr= 0
      for i in range(None):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_4(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' or str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_5(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] > '0' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_6(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= 'XX0XX' and str[i] <= '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_7(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] < '9': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_8(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= 'XX9XX': number_ctr += 1     
      return  number_ctr
def x_number_ctr__mutmut_9(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr = 1     
      return  number_ctr
def x_number_ctr__mutmut_10(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr -= 1     
      return  number_ctr
def x_number_ctr__mutmut_11(str):
      number_ctr= 0
      for i in range(len(str)):
          if str[i] >= '0' and str[i] <= '9': number_ctr += 2     
      return  number_ctr

x_number_ctr__mutmut_mutants : ClassVar[MutantDict] = {
'x_number_ctr__mutmut_1': x_number_ctr__mutmut_1, 
    'x_number_ctr__mutmut_2': x_number_ctr__mutmut_2, 
    'x_number_ctr__mutmut_3': x_number_ctr__mutmut_3, 
    'x_number_ctr__mutmut_4': x_number_ctr__mutmut_4, 
    'x_number_ctr__mutmut_5': x_number_ctr__mutmut_5, 
    'x_number_ctr__mutmut_6': x_number_ctr__mutmut_6, 
    'x_number_ctr__mutmut_7': x_number_ctr__mutmut_7, 
    'x_number_ctr__mutmut_8': x_number_ctr__mutmut_8, 
    'x_number_ctr__mutmut_9': x_number_ctr__mutmut_9, 
    'x_number_ctr__mutmut_10': x_number_ctr__mutmut_10, 
    'x_number_ctr__mutmut_11': x_number_ctr__mutmut_11
}

def number_ctr(*args, **kwargs):
      result = _mutmut_trampoline(x_number_ctr__mutmut_orig, x_number_ctr__mutmut_mutants, args, kwargs)
      return result 

number_ctr.__signature__ = _mutmut_signature(x_number_ctr__mutmut_orig)
x_number_ctr__mutmut_orig.__name__ = 'x_number_ctr'