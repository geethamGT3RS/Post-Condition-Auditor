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
def x_div_list__mutmut_orig(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(result)
def x_div_list__mutmut_1(nums1,nums2):
  result = None
  return list(result)
def x_div_list__mutmut_2(nums1,nums2):
  result = map(None, nums1, nums2)
  return list(result)
def x_div_list__mutmut_3(nums1,nums2):
  result = map(lambda x, y: x / y, None, nums2)
  return list(result)
def x_div_list__mutmut_4(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, None)
  return list(result)
def x_div_list__mutmut_5(nums1,nums2):
  result = map(nums1, nums2)
  return list(result)
def x_div_list__mutmut_6(nums1,nums2):
  result = map(lambda x, y: x / y, nums2)
  return list(result)
def x_div_list__mutmut_7(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, )
  return list(result)
def x_div_list__mutmut_8(nums1,nums2):
  result = map(lambda x, y: None, nums1, nums2)
  return list(result)
def x_div_list__mutmut_9(nums1,nums2):
  result = map(lambda x, y: x * y, nums1, nums2)
  return list(result)
def x_div_list__mutmut_10(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(None)

x_div_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_div_list__mutmut_1': x_div_list__mutmut_1, 
    'x_div_list__mutmut_2': x_div_list__mutmut_2, 
    'x_div_list__mutmut_3': x_div_list__mutmut_3, 
    'x_div_list__mutmut_4': x_div_list__mutmut_4, 
    'x_div_list__mutmut_5': x_div_list__mutmut_5, 
    'x_div_list__mutmut_6': x_div_list__mutmut_6, 
    'x_div_list__mutmut_7': x_div_list__mutmut_7, 
    'x_div_list__mutmut_8': x_div_list__mutmut_8, 
    'x_div_list__mutmut_9': x_div_list__mutmut_9, 
    'x_div_list__mutmut_10': x_div_list__mutmut_10
}

def div_list(*args, **kwargs):
  result = _mutmut_trampoline(x_div_list__mutmut_orig, x_div_list__mutmut_mutants, args, kwargs)
  return result 

div_list.__signature__ = _mutmut_signature(x_div_list__mutmut_orig)
x_div_list__mutmut_orig.__name__ = 'x_div_list'