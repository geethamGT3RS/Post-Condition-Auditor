import heapq
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
def x_merge_sorted_list__mutmut_orig(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_1(num1,num2,num3):
  num1=None
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_2(num1,num2,num3):
  num1=sorted(None)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_3(num1,num2,num3):
  num1=sorted(num1)
  num2=None
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_4(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(None)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_5(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=None
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_6(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(None)
  result = heapq.merge(num1,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_7(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = None
  return list(result)
def x_merge_sorted_list__mutmut_8(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(None,num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_9(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,None,num3)
  return list(result)
def x_merge_sorted_list__mutmut_10(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,None)
  return list(result)
def x_merge_sorted_list__mutmut_11(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num2,num3)
  return list(result)
def x_merge_sorted_list__mutmut_12(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num3)
  return list(result)
def x_merge_sorted_list__mutmut_13(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,)
  return list(result)
def x_merge_sorted_list__mutmut_14(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(None)

x_merge_sorted_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_merge_sorted_list__mutmut_1': x_merge_sorted_list__mutmut_1, 
    'x_merge_sorted_list__mutmut_2': x_merge_sorted_list__mutmut_2, 
    'x_merge_sorted_list__mutmut_3': x_merge_sorted_list__mutmut_3, 
    'x_merge_sorted_list__mutmut_4': x_merge_sorted_list__mutmut_4, 
    'x_merge_sorted_list__mutmut_5': x_merge_sorted_list__mutmut_5, 
    'x_merge_sorted_list__mutmut_6': x_merge_sorted_list__mutmut_6, 
    'x_merge_sorted_list__mutmut_7': x_merge_sorted_list__mutmut_7, 
    'x_merge_sorted_list__mutmut_8': x_merge_sorted_list__mutmut_8, 
    'x_merge_sorted_list__mutmut_9': x_merge_sorted_list__mutmut_9, 
    'x_merge_sorted_list__mutmut_10': x_merge_sorted_list__mutmut_10, 
    'x_merge_sorted_list__mutmut_11': x_merge_sorted_list__mutmut_11, 
    'x_merge_sorted_list__mutmut_12': x_merge_sorted_list__mutmut_12, 
    'x_merge_sorted_list__mutmut_13': x_merge_sorted_list__mutmut_13, 
    'x_merge_sorted_list__mutmut_14': x_merge_sorted_list__mutmut_14
}

def merge_sorted_list(*args, **kwargs):
  result = _mutmut_trampoline(x_merge_sorted_list__mutmut_orig, x_merge_sorted_list__mutmut_mutants, args, kwargs)
  return result 

merge_sorted_list.__signature__ = _mutmut_signature(x_merge_sorted_list__mutmut_orig)
x_merge_sorted_list__mutmut_orig.__name__ = 'x_merge_sorted_list'