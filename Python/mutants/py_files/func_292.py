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
def x_expensive_items__mutmut_orig(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items
def x_expensive_items__mutmut_1(items,n):
  expensive_items = None
  return expensive_items
def x_expensive_items__mutmut_2(items,n):
  expensive_items = heapq.nlargest(None, items, key=lambda s: s['price'])
  return expensive_items
def x_expensive_items__mutmut_3(items,n):
  expensive_items = heapq.nlargest(n, None, key=lambda s: s['price'])
  return expensive_items
def x_expensive_items__mutmut_4(items,n):
  expensive_items = heapq.nlargest(n, items, key=None)
  return expensive_items
def x_expensive_items__mutmut_5(items,n):
  expensive_items = heapq.nlargest(items, key=lambda s: s['price'])
  return expensive_items
def x_expensive_items__mutmut_6(items,n):
  expensive_items = heapq.nlargest(n, key=lambda s: s['price'])
  return expensive_items
def x_expensive_items__mutmut_7(items,n):
  expensive_items = heapq.nlargest(n, items, )
  return expensive_items
def x_expensive_items__mutmut_8(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: None)
  return expensive_items
def x_expensive_items__mutmut_9(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['XXpriceXX'])
  return expensive_items
def x_expensive_items__mutmut_10(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['PRICE'])
  return expensive_items

x_expensive_items__mutmut_mutants : ClassVar[MutantDict] = {
'x_expensive_items__mutmut_1': x_expensive_items__mutmut_1, 
    'x_expensive_items__mutmut_2': x_expensive_items__mutmut_2, 
    'x_expensive_items__mutmut_3': x_expensive_items__mutmut_3, 
    'x_expensive_items__mutmut_4': x_expensive_items__mutmut_4, 
    'x_expensive_items__mutmut_5': x_expensive_items__mutmut_5, 
    'x_expensive_items__mutmut_6': x_expensive_items__mutmut_6, 
    'x_expensive_items__mutmut_7': x_expensive_items__mutmut_7, 
    'x_expensive_items__mutmut_8': x_expensive_items__mutmut_8, 
    'x_expensive_items__mutmut_9': x_expensive_items__mutmut_9, 
    'x_expensive_items__mutmut_10': x_expensive_items__mutmut_10
}

def expensive_items(*args, **kwargs):
  result = _mutmut_trampoline(x_expensive_items__mutmut_orig, x_expensive_items__mutmut_mutants, args, kwargs)
  return result 

expensive_items.__signature__ = _mutmut_signature(x_expensive_items__mutmut_orig)
x_expensive_items__mutmut_orig.__name__ = 'x_expensive_items'