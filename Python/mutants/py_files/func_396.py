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
def x_count_vowels__mutmut_orig(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_1(test_str):
  res = None
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_2(test_str):
  res = 1
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_3(test_str):
  res = 0
  vow_list = None
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_4(test_str):
  res = 0
  vow_list = ['XXaXX', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_5(test_str):
  res = 0
  vow_list = ['A', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_6(test_str):
  res = 0
  vow_list = ['a', 'XXeXX', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_7(test_str):
  res = 0
  vow_list = ['a', 'E', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_8(test_str):
  res = 0
  vow_list = ['a', 'e', 'XXiXX', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_9(test_str):
  res = 0
  vow_list = ['a', 'e', 'I', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_10(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'XXoXX', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_11(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'O', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_12(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'XXuXX']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_13(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'U']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_14(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(None, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_15(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, None):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_16(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_17(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, ):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_18(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(2, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_19(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) + 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_20(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 2):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_21(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list or (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_22(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_23(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list and test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_24(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx + 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_25(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 2] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_26(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] not in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_27(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx - 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_28(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 2] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_29(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] not in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_30(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res = 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_31(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res -= 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_32(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 2
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_33(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list or test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_34(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[1] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_35(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_36(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[2] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_37(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] not in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_38(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res = 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_39(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res -= 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_40(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 2
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_41(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list or test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_42(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[+1] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_43(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-2] not in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_44(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] in vow_list and test_str[-2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_45(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[+2] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_46(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-3] in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_47(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] not in vow_list:
    res += 1
  return (res) 
def x_count_vowels__mutmut_48(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res = 1
  return (res) 
def x_count_vowels__mutmut_49(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res -= 1
  return (res) 
def x_count_vowels__mutmut_50(test_str):
  res = 0
  vow_list = ['a', 'e', 'i', 'o', 'u']
  for idx in range(1, len(test_str) - 1):
    if test_str[idx] not in vow_list and (test_str[idx - 1] in vow_list or test_str[idx + 1] in vow_list):
      res += 1
  if test_str[0] not in vow_list and test_str[1] in vow_list:
    res += 1
  if test_str[-1] not in vow_list and test_str[-2] in vow_list:
    res += 2
  return (res) 

x_count_vowels__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_vowels__mutmut_1': x_count_vowels__mutmut_1, 
    'x_count_vowels__mutmut_2': x_count_vowels__mutmut_2, 
    'x_count_vowels__mutmut_3': x_count_vowels__mutmut_3, 
    'x_count_vowels__mutmut_4': x_count_vowels__mutmut_4, 
    'x_count_vowels__mutmut_5': x_count_vowels__mutmut_5, 
    'x_count_vowels__mutmut_6': x_count_vowels__mutmut_6, 
    'x_count_vowels__mutmut_7': x_count_vowels__mutmut_7, 
    'x_count_vowels__mutmut_8': x_count_vowels__mutmut_8, 
    'x_count_vowels__mutmut_9': x_count_vowels__mutmut_9, 
    'x_count_vowels__mutmut_10': x_count_vowels__mutmut_10, 
    'x_count_vowels__mutmut_11': x_count_vowels__mutmut_11, 
    'x_count_vowels__mutmut_12': x_count_vowels__mutmut_12, 
    'x_count_vowels__mutmut_13': x_count_vowels__mutmut_13, 
    'x_count_vowels__mutmut_14': x_count_vowels__mutmut_14, 
    'x_count_vowels__mutmut_15': x_count_vowels__mutmut_15, 
    'x_count_vowels__mutmut_16': x_count_vowels__mutmut_16, 
    'x_count_vowels__mutmut_17': x_count_vowels__mutmut_17, 
    'x_count_vowels__mutmut_18': x_count_vowels__mutmut_18, 
    'x_count_vowels__mutmut_19': x_count_vowels__mutmut_19, 
    'x_count_vowels__mutmut_20': x_count_vowels__mutmut_20, 
    'x_count_vowels__mutmut_21': x_count_vowels__mutmut_21, 
    'x_count_vowels__mutmut_22': x_count_vowels__mutmut_22, 
    'x_count_vowels__mutmut_23': x_count_vowels__mutmut_23, 
    'x_count_vowels__mutmut_24': x_count_vowels__mutmut_24, 
    'x_count_vowels__mutmut_25': x_count_vowels__mutmut_25, 
    'x_count_vowels__mutmut_26': x_count_vowels__mutmut_26, 
    'x_count_vowels__mutmut_27': x_count_vowels__mutmut_27, 
    'x_count_vowels__mutmut_28': x_count_vowels__mutmut_28, 
    'x_count_vowels__mutmut_29': x_count_vowels__mutmut_29, 
    'x_count_vowels__mutmut_30': x_count_vowels__mutmut_30, 
    'x_count_vowels__mutmut_31': x_count_vowels__mutmut_31, 
    'x_count_vowels__mutmut_32': x_count_vowels__mutmut_32, 
    'x_count_vowels__mutmut_33': x_count_vowels__mutmut_33, 
    'x_count_vowels__mutmut_34': x_count_vowels__mutmut_34, 
    'x_count_vowels__mutmut_35': x_count_vowels__mutmut_35, 
    'x_count_vowels__mutmut_36': x_count_vowels__mutmut_36, 
    'x_count_vowels__mutmut_37': x_count_vowels__mutmut_37, 
    'x_count_vowels__mutmut_38': x_count_vowels__mutmut_38, 
    'x_count_vowels__mutmut_39': x_count_vowels__mutmut_39, 
    'x_count_vowels__mutmut_40': x_count_vowels__mutmut_40, 
    'x_count_vowels__mutmut_41': x_count_vowels__mutmut_41, 
    'x_count_vowels__mutmut_42': x_count_vowels__mutmut_42, 
    'x_count_vowels__mutmut_43': x_count_vowels__mutmut_43, 
    'x_count_vowels__mutmut_44': x_count_vowels__mutmut_44, 
    'x_count_vowels__mutmut_45': x_count_vowels__mutmut_45, 
    'x_count_vowels__mutmut_46': x_count_vowels__mutmut_46, 
    'x_count_vowels__mutmut_47': x_count_vowels__mutmut_47, 
    'x_count_vowels__mutmut_48': x_count_vowels__mutmut_48, 
    'x_count_vowels__mutmut_49': x_count_vowels__mutmut_49, 
    'x_count_vowels__mutmut_50': x_count_vowels__mutmut_50
}

def count_vowels(*args, **kwargs):
  result = _mutmut_trampoline(x_count_vowels__mutmut_orig, x_count_vowels__mutmut_mutants, args, kwargs)
  return result 

count_vowels.__signature__ = _mutmut_signature(x_count_vowels__mutmut_orig)
x_count_vowels__mutmut_orig.__name__ = 'x_count_vowels'