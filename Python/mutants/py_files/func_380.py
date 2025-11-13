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
def x_count_reverse_pairs__mutmut_orig(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_1(test_list):
  res = None 
  return res
def x_count_reverse_pairs__mutmut_2(test_list):
  res = sum(None) 
  return res
def x_count_reverse_pairs__mutmut_3(test_list):
  res = sum([2 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_4(test_list):
  res = sum([1 for idx in range(None, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_5(test_list):
  res = sum([1 for idx in range(0, None) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_6(test_list):
  res = sum([1 for idx in range(len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_7(test_list):
  res = sum([1 for idx in range(0, ) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_8(test_list):
  res = sum([1 for idx in range(1, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_9(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(None, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_10(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, None) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_11(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_12(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, ) if test_list[idxn] == str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_13(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] != str(''.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_14(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(None)]) 
  return res
def x_count_reverse_pairs__mutmut_15(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(None))]) 
  return res
def x_count_reverse_pairs__mutmut_16(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str('XXXX'.join(list(reversed(test_list[idx]))))]) 
  return res
def x_count_reverse_pairs__mutmut_17(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(None)))]) 
  return res
def x_count_reverse_pairs__mutmut_18(test_list):
  res = sum([1 for idx in range(0, len(test_list)) for idxn in range(idx, len( 
	test_list)) if test_list[idxn] == str(''.join(list(reversed(None))))]) 
  return res

x_count_reverse_pairs__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_reverse_pairs__mutmut_1': x_count_reverse_pairs__mutmut_1, 
    'x_count_reverse_pairs__mutmut_2': x_count_reverse_pairs__mutmut_2, 
    'x_count_reverse_pairs__mutmut_3': x_count_reverse_pairs__mutmut_3, 
    'x_count_reverse_pairs__mutmut_4': x_count_reverse_pairs__mutmut_4, 
    'x_count_reverse_pairs__mutmut_5': x_count_reverse_pairs__mutmut_5, 
    'x_count_reverse_pairs__mutmut_6': x_count_reverse_pairs__mutmut_6, 
    'x_count_reverse_pairs__mutmut_7': x_count_reverse_pairs__mutmut_7, 
    'x_count_reverse_pairs__mutmut_8': x_count_reverse_pairs__mutmut_8, 
    'x_count_reverse_pairs__mutmut_9': x_count_reverse_pairs__mutmut_9, 
    'x_count_reverse_pairs__mutmut_10': x_count_reverse_pairs__mutmut_10, 
    'x_count_reverse_pairs__mutmut_11': x_count_reverse_pairs__mutmut_11, 
    'x_count_reverse_pairs__mutmut_12': x_count_reverse_pairs__mutmut_12, 
    'x_count_reverse_pairs__mutmut_13': x_count_reverse_pairs__mutmut_13, 
    'x_count_reverse_pairs__mutmut_14': x_count_reverse_pairs__mutmut_14, 
    'x_count_reverse_pairs__mutmut_15': x_count_reverse_pairs__mutmut_15, 
    'x_count_reverse_pairs__mutmut_16': x_count_reverse_pairs__mutmut_16, 
    'x_count_reverse_pairs__mutmut_17': x_count_reverse_pairs__mutmut_17, 
    'x_count_reverse_pairs__mutmut_18': x_count_reverse_pairs__mutmut_18
}

def count_reverse_pairs(*args, **kwargs):
  result = _mutmut_trampoline(x_count_reverse_pairs__mutmut_orig, x_count_reverse_pairs__mutmut_mutants, args, kwargs)
  return result 

count_reverse_pairs.__signature__ = _mutmut_signature(x_count_reverse_pairs__mutmut_orig)
x_count_reverse_pairs__mutmut_orig.__name__ = 'x_count_reverse_pairs'