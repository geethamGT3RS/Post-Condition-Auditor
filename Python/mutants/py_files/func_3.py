import heapq as hq
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
def x_heap_queue_largest__mutmut_orig(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums
def x_heap_queue_largest__mutmut_1(nums,n):
  largest_nums = None
  return largest_nums
def x_heap_queue_largest__mutmut_2(nums,n):
  largest_nums = hq.nlargest(None, nums)
  return largest_nums
def x_heap_queue_largest__mutmut_3(nums,n):
  largest_nums = hq.nlargest(n, None)
  return largest_nums
def x_heap_queue_largest__mutmut_4(nums,n):
  largest_nums = hq.nlargest(nums)
  return largest_nums
def x_heap_queue_largest__mutmut_5(nums,n):
  largest_nums = hq.nlargest(n, )
  return largest_nums

x_heap_queue_largest__mutmut_mutants : ClassVar[MutantDict] = {
'x_heap_queue_largest__mutmut_1': x_heap_queue_largest__mutmut_1, 
    'x_heap_queue_largest__mutmut_2': x_heap_queue_largest__mutmut_2, 
    'x_heap_queue_largest__mutmut_3': x_heap_queue_largest__mutmut_3, 
    'x_heap_queue_largest__mutmut_4': x_heap_queue_largest__mutmut_4, 
    'x_heap_queue_largest__mutmut_5': x_heap_queue_largest__mutmut_5
}

def heap_queue_largest(*args, **kwargs):
  result = _mutmut_trampoline(x_heap_queue_largest__mutmut_orig, x_heap_queue_largest__mutmut_mutants, args, kwargs)
  return result 

heap_queue_largest.__signature__ = _mutmut_signature(x_heap_queue_largest__mutmut_orig)
x_heap_queue_largest__mutmut_orig.__name__ = 'x_heap_queue_largest'