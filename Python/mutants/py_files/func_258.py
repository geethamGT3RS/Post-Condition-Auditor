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
def x_tuple_intersection__mutmut_orig(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_1(test_list1, test_list2):
  res = None
  return (res)
def x_tuple_intersection__mutmut_2(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) | set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_3(test_list1, test_list2):
  res = set(None) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_4(test_list1, test_list2):
  res = set([tuple(None) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_5(test_list1, test_list2):
  res = set([tuple(sorted(None)) for ele in test_list1]) & set([tuple(sorted(ele)) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_6(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set(None)
  return (res)
def x_tuple_intersection__mutmut_7(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(None) for ele in test_list2])
  return (res)
def x_tuple_intersection__mutmut_8(test_list1, test_list2):
  res = set([tuple(sorted(ele)) for ele in test_list1]) & set([tuple(sorted(None)) for ele in test_list2])
  return (res)

x_tuple_intersection__mutmut_mutants : ClassVar[MutantDict] = {
'x_tuple_intersection__mutmut_1': x_tuple_intersection__mutmut_1, 
    'x_tuple_intersection__mutmut_2': x_tuple_intersection__mutmut_2, 
    'x_tuple_intersection__mutmut_3': x_tuple_intersection__mutmut_3, 
    'x_tuple_intersection__mutmut_4': x_tuple_intersection__mutmut_4, 
    'x_tuple_intersection__mutmut_5': x_tuple_intersection__mutmut_5, 
    'x_tuple_intersection__mutmut_6': x_tuple_intersection__mutmut_6, 
    'x_tuple_intersection__mutmut_7': x_tuple_intersection__mutmut_7, 
    'x_tuple_intersection__mutmut_8': x_tuple_intersection__mutmut_8
}

def tuple_intersection(*args, **kwargs):
  result = _mutmut_trampoline(x_tuple_intersection__mutmut_orig, x_tuple_intersection__mutmut_mutants, args, kwargs)
  return result 

tuple_intersection.__signature__ = _mutmut_signature(x_tuple_intersection__mutmut_orig)
x_tuple_intersection__mutmut_orig.__name__ = 'x_tuple_intersection'