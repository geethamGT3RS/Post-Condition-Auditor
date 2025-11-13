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
def x_reverse_Array_Upto_K__mutmut_orig(input, k): 
  return (input[k-1::-1] + input[k:]) 
def x_reverse_Array_Upto_K__mutmut_1(input, k): 
  return (input[k-1::-1] - input[k:]) 
def x_reverse_Array_Upto_K__mutmut_2(input, k): 
  return (input[k + 1::-1] + input[k:]) 
def x_reverse_Array_Upto_K__mutmut_3(input, k): 
  return (input[k-2::-1] + input[k:]) 
def x_reverse_Array_Upto_K__mutmut_4(input, k): 
  return (input[k-1::+1] + input[k:]) 
def x_reverse_Array_Upto_K__mutmut_5(input, k): 
  return (input[k-1::-2] + input[k:]) 

x_reverse_Array_Upto_K__mutmut_mutants : ClassVar[MutantDict] = {
'x_reverse_Array_Upto_K__mutmut_1': x_reverse_Array_Upto_K__mutmut_1, 
    'x_reverse_Array_Upto_K__mutmut_2': x_reverse_Array_Upto_K__mutmut_2, 
    'x_reverse_Array_Upto_K__mutmut_3': x_reverse_Array_Upto_K__mutmut_3, 
    'x_reverse_Array_Upto_K__mutmut_4': x_reverse_Array_Upto_K__mutmut_4, 
    'x_reverse_Array_Upto_K__mutmut_5': x_reverse_Array_Upto_K__mutmut_5
}

def reverse_Array_Upto_K(*args, **kwargs):
  result = _mutmut_trampoline(x_reverse_Array_Upto_K__mutmut_orig, x_reverse_Array_Upto_K__mutmut_mutants, args, kwargs)
  return result 

reverse_Array_Upto_K.__signature__ = _mutmut_signature(x_reverse_Array_Upto_K__mutmut_orig)
x_reverse_Array_Upto_K__mutmut_orig.__name__ = 'x_reverse_Array_Upto_K'