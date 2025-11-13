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
def x_count_bidirectional__mutmut_orig(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_1(test_list):
  res = None
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_2(test_list):
  res = 1
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_3(test_list):
  res = 0
  for idx in range(None, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_4(test_list):
  res = 0
  for idx in range(0, None):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_5(test_list):
  res = 0
  for idx in range(len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_6(test_list):
  res = 0
  for idx in range(0, ):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_7(test_list):
  res = 0
  for idx in range(1, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_8(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(None, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_9(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, None):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_10(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_11(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, ):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_12(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx - 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_13(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 2, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_14(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] or test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_15(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][1] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_16(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] != test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_17(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][2] and test_list[idx][1] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_18(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][2] == test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_19(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] != test_list[iidx][0]:
        res += 1
  return res
def x_count_bidirectional__mutmut_20(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][1]:
        res += 1
  return res
def x_count_bidirectional__mutmut_21(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res = 1
  return res
def x_count_bidirectional__mutmut_22(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res -= 1
  return res
def x_count_bidirectional__mutmut_23(test_list):
  res = 0
  for idx in range(0, len(test_list)):
    for iidx in range(idx + 1, len(test_list)):
      if test_list[iidx][0] == test_list[idx][1] and test_list[idx][1] == test_list[iidx][0]:
        res += 2
  return res

x_count_bidirectional__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_bidirectional__mutmut_1': x_count_bidirectional__mutmut_1, 
    'x_count_bidirectional__mutmut_2': x_count_bidirectional__mutmut_2, 
    'x_count_bidirectional__mutmut_3': x_count_bidirectional__mutmut_3, 
    'x_count_bidirectional__mutmut_4': x_count_bidirectional__mutmut_4, 
    'x_count_bidirectional__mutmut_5': x_count_bidirectional__mutmut_5, 
    'x_count_bidirectional__mutmut_6': x_count_bidirectional__mutmut_6, 
    'x_count_bidirectional__mutmut_7': x_count_bidirectional__mutmut_7, 
    'x_count_bidirectional__mutmut_8': x_count_bidirectional__mutmut_8, 
    'x_count_bidirectional__mutmut_9': x_count_bidirectional__mutmut_9, 
    'x_count_bidirectional__mutmut_10': x_count_bidirectional__mutmut_10, 
    'x_count_bidirectional__mutmut_11': x_count_bidirectional__mutmut_11, 
    'x_count_bidirectional__mutmut_12': x_count_bidirectional__mutmut_12, 
    'x_count_bidirectional__mutmut_13': x_count_bidirectional__mutmut_13, 
    'x_count_bidirectional__mutmut_14': x_count_bidirectional__mutmut_14, 
    'x_count_bidirectional__mutmut_15': x_count_bidirectional__mutmut_15, 
    'x_count_bidirectional__mutmut_16': x_count_bidirectional__mutmut_16, 
    'x_count_bidirectional__mutmut_17': x_count_bidirectional__mutmut_17, 
    'x_count_bidirectional__mutmut_18': x_count_bidirectional__mutmut_18, 
    'x_count_bidirectional__mutmut_19': x_count_bidirectional__mutmut_19, 
    'x_count_bidirectional__mutmut_20': x_count_bidirectional__mutmut_20, 
    'x_count_bidirectional__mutmut_21': x_count_bidirectional__mutmut_21, 
    'x_count_bidirectional__mutmut_22': x_count_bidirectional__mutmut_22, 
    'x_count_bidirectional__mutmut_23': x_count_bidirectional__mutmut_23
}

def count_bidirectional(*args, **kwargs):
  result = _mutmut_trampoline(x_count_bidirectional__mutmut_orig, x_count_bidirectional__mutmut_mutants, args, kwargs)
  return result 

count_bidirectional.__signature__ = _mutmut_signature(x_count_bidirectional__mutmut_orig)
x_count_bidirectional__mutmut_orig.__name__ = 'x_count_bidirectional'