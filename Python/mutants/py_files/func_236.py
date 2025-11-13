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
def x_cube_nums__mutmut_orig(nums):
 cube_nums = list(map(lambda x: x ** 3, nums))
 return cube_nums
def x_cube_nums__mutmut_1(nums):
 cube_nums = None
 return cube_nums
def x_cube_nums__mutmut_2(nums):
 cube_nums = list(None)
 return cube_nums
def x_cube_nums__mutmut_3(nums):
 cube_nums = list(map(None, nums))
 return cube_nums
def x_cube_nums__mutmut_4(nums):
 cube_nums = list(map(lambda x: x ** 3, None))
 return cube_nums
def x_cube_nums__mutmut_5(nums):
 cube_nums = list(map(nums))
 return cube_nums
def x_cube_nums__mutmut_6(nums):
 cube_nums = list(map(lambda x: x ** 3, ))
 return cube_nums
def x_cube_nums__mutmut_7(nums):
 cube_nums = list(map(lambda x: None, nums))
 return cube_nums
def x_cube_nums__mutmut_8(nums):
 cube_nums = list(map(lambda x: x * 3, nums))
 return cube_nums
def x_cube_nums__mutmut_9(nums):
 cube_nums = list(map(lambda x: x ** 4, nums))
 return cube_nums

x_cube_nums__mutmut_mutants : ClassVar[MutantDict] = {
'x_cube_nums__mutmut_1': x_cube_nums__mutmut_1, 
    'x_cube_nums__mutmut_2': x_cube_nums__mutmut_2, 
    'x_cube_nums__mutmut_3': x_cube_nums__mutmut_3, 
    'x_cube_nums__mutmut_4': x_cube_nums__mutmut_4, 
    'x_cube_nums__mutmut_5': x_cube_nums__mutmut_5, 
    'x_cube_nums__mutmut_6': x_cube_nums__mutmut_6, 
    'x_cube_nums__mutmut_7': x_cube_nums__mutmut_7, 
    'x_cube_nums__mutmut_8': x_cube_nums__mutmut_8, 
    'x_cube_nums__mutmut_9': x_cube_nums__mutmut_9
}

def cube_nums(*args, **kwargs):
 result = _mutmut_trampoline(x_cube_nums__mutmut_orig, x_cube_nums__mutmut_mutants, args, kwargs)
 return result 

cube_nums.__signature__ = _mutmut_signature(x_cube_nums__mutmut_orig)
x_cube_nums__mutmut_orig.__name__ = 'x_cube_nums'