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
def x_prime_num__mutmut_orig(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_1(num):
  if num > 1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_2(num):
  if num >=2:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_3(num):
  if num >=1:
   for i in range(None, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_4(num):
  if num >=1:
   for i in range(2, None):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_5(num):
  if num >=1:
   for i in range(num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_6(num):
  if num >=1:
   for i in range(2, ):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_7(num):
  if num >=1:
   for i in range(3, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_8(num):
  if num >=1:
   for i in range(2, num / 2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_9(num):
  if num >=1:
   for i in range(2, num//3):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_10(num):
  if num >=1:
   for i in range(2, num//2):
     if (num / i) == 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_11(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) != 0:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_12(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 1:
                return False
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_13(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return True
     else:
                return True
  else:
          return False
def x_prime_num__mutmut_14(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return False
  else:
          return False
def x_prime_num__mutmut_15(num):
  if num >=1:
   for i in range(2, num//2):
     if (num % i) == 0:
                return False
     else:
                return True
  else:
          return True

x_prime_num__mutmut_mutants : ClassVar[MutantDict] = {
'x_prime_num__mutmut_1': x_prime_num__mutmut_1, 
    'x_prime_num__mutmut_2': x_prime_num__mutmut_2, 
    'x_prime_num__mutmut_3': x_prime_num__mutmut_3, 
    'x_prime_num__mutmut_4': x_prime_num__mutmut_4, 
    'x_prime_num__mutmut_5': x_prime_num__mutmut_5, 
    'x_prime_num__mutmut_6': x_prime_num__mutmut_6, 
    'x_prime_num__mutmut_7': x_prime_num__mutmut_7, 
    'x_prime_num__mutmut_8': x_prime_num__mutmut_8, 
    'x_prime_num__mutmut_9': x_prime_num__mutmut_9, 
    'x_prime_num__mutmut_10': x_prime_num__mutmut_10, 
    'x_prime_num__mutmut_11': x_prime_num__mutmut_11, 
    'x_prime_num__mutmut_12': x_prime_num__mutmut_12, 
    'x_prime_num__mutmut_13': x_prime_num__mutmut_13, 
    'x_prime_num__mutmut_14': x_prime_num__mutmut_14, 
    'x_prime_num__mutmut_15': x_prime_num__mutmut_15
}

def prime_num(*args, **kwargs):
  result = _mutmut_trampoline(x_prime_num__mutmut_orig, x_prime_num__mutmut_mutants, args, kwargs)
  return result 

prime_num.__signature__ = _mutmut_signature(x_prime_num__mutmut_orig)
x_prime_num__mutmut_orig.__name__ = 'x_prime_num'