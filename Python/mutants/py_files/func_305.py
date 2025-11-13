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
def x_armstrong_number__mutmut_orig(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_1(number):
 sum = None
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_2(number):
 sum = 1
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_3(number):
 sum = 0
 times = None
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_4(number):
 sum = 0
 times = 1
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_5(number):
 sum = 0
 times = 0
 temp = None
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_6(number):
 sum = 0
 times = 0
 temp = number
 while temp >= 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_7(number):
 sum = 0
 times = 0
 temp = number
 while temp > 1:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_8(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = None
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_9(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times - 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_10(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 2
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_11(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = None
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_12(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp / 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_13(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 11
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_14(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = None
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_15(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp >= 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_16(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 1:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_17(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = None
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_18(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp / 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_19(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 11
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_20(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = None
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_21(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum - (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_22(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder * times)
           temp //= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_23(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp = 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_24(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp /= 10
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_25(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 11
 if number == sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_26(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number != sum:
           return True
 else:
           return False
def x_armstrong_number__mutmut_27(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return False
 else:
           return False
def x_armstrong_number__mutmut_28(number):
 sum = 0
 times = 0
 temp = number
 while temp > 0:
           times = times + 1
           temp = temp // 10
 temp = number
 while temp > 0:
           reminder = temp % 10
           sum = sum + (reminder ** times)
           temp //= 10
 if number == sum:
           return True
 else:
           return True

x_armstrong_number__mutmut_mutants : ClassVar[MutantDict] = {
'x_armstrong_number__mutmut_1': x_armstrong_number__mutmut_1, 
    'x_armstrong_number__mutmut_2': x_armstrong_number__mutmut_2, 
    'x_armstrong_number__mutmut_3': x_armstrong_number__mutmut_3, 
    'x_armstrong_number__mutmut_4': x_armstrong_number__mutmut_4, 
    'x_armstrong_number__mutmut_5': x_armstrong_number__mutmut_5, 
    'x_armstrong_number__mutmut_6': x_armstrong_number__mutmut_6, 
    'x_armstrong_number__mutmut_7': x_armstrong_number__mutmut_7, 
    'x_armstrong_number__mutmut_8': x_armstrong_number__mutmut_8, 
    'x_armstrong_number__mutmut_9': x_armstrong_number__mutmut_9, 
    'x_armstrong_number__mutmut_10': x_armstrong_number__mutmut_10, 
    'x_armstrong_number__mutmut_11': x_armstrong_number__mutmut_11, 
    'x_armstrong_number__mutmut_12': x_armstrong_number__mutmut_12, 
    'x_armstrong_number__mutmut_13': x_armstrong_number__mutmut_13, 
    'x_armstrong_number__mutmut_14': x_armstrong_number__mutmut_14, 
    'x_armstrong_number__mutmut_15': x_armstrong_number__mutmut_15, 
    'x_armstrong_number__mutmut_16': x_armstrong_number__mutmut_16, 
    'x_armstrong_number__mutmut_17': x_armstrong_number__mutmut_17, 
    'x_armstrong_number__mutmut_18': x_armstrong_number__mutmut_18, 
    'x_armstrong_number__mutmut_19': x_armstrong_number__mutmut_19, 
    'x_armstrong_number__mutmut_20': x_armstrong_number__mutmut_20, 
    'x_armstrong_number__mutmut_21': x_armstrong_number__mutmut_21, 
    'x_armstrong_number__mutmut_22': x_armstrong_number__mutmut_22, 
    'x_armstrong_number__mutmut_23': x_armstrong_number__mutmut_23, 
    'x_armstrong_number__mutmut_24': x_armstrong_number__mutmut_24, 
    'x_armstrong_number__mutmut_25': x_armstrong_number__mutmut_25, 
    'x_armstrong_number__mutmut_26': x_armstrong_number__mutmut_26, 
    'x_armstrong_number__mutmut_27': x_armstrong_number__mutmut_27, 
    'x_armstrong_number__mutmut_28': x_armstrong_number__mutmut_28
}

def armstrong_number(*args, **kwargs):
 result = _mutmut_trampoline(x_armstrong_number__mutmut_orig, x_armstrong_number__mutmut_mutants, args, kwargs)
 return result 

armstrong_number.__signature__ = _mutmut_signature(x_armstrong_number__mutmut_orig)
x_armstrong_number__mutmut_orig.__name__ = 'x_armstrong_number'