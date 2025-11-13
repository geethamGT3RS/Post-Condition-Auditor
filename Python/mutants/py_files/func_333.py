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
def x_adjac__mutmut_orig(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_1(ele, sub = []): 
  if ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_2(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(None, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_3(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, None) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_4(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_5(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_6(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] + 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_7(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[1] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_8(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 2, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_9(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] - 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_10(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[1] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_11(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 3) 
                for idx in adjac(ele[1:], sub + [j])] 
def x_adjac__mutmut_12(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(None, sub + [j])] 
def x_adjac__mutmut_13(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], None)] 
def x_adjac__mutmut_14(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(sub + [j])] 
def x_adjac__mutmut_15(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], )] 
def x_adjac__mutmut_16(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[2:], sub + [j])] 
def x_adjac__mutmut_17(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub - [j])] 

x_adjac__mutmut_mutants : ClassVar[MutantDict] = {
'x_adjac__mutmut_1': x_adjac__mutmut_1, 
    'x_adjac__mutmut_2': x_adjac__mutmut_2, 
    'x_adjac__mutmut_3': x_adjac__mutmut_3, 
    'x_adjac__mutmut_4': x_adjac__mutmut_4, 
    'x_adjac__mutmut_5': x_adjac__mutmut_5, 
    'x_adjac__mutmut_6': x_adjac__mutmut_6, 
    'x_adjac__mutmut_7': x_adjac__mutmut_7, 
    'x_adjac__mutmut_8': x_adjac__mutmut_8, 
    'x_adjac__mutmut_9': x_adjac__mutmut_9, 
    'x_adjac__mutmut_10': x_adjac__mutmut_10, 
    'x_adjac__mutmut_11': x_adjac__mutmut_11, 
    'x_adjac__mutmut_12': x_adjac__mutmut_12, 
    'x_adjac__mutmut_13': x_adjac__mutmut_13, 
    'x_adjac__mutmut_14': x_adjac__mutmut_14, 
    'x_adjac__mutmut_15': x_adjac__mutmut_15, 
    'x_adjac__mutmut_16': x_adjac__mutmut_16, 
    'x_adjac__mutmut_17': x_adjac__mutmut_17
}

def adjac(*args, **kwargs):
  result = _mutmut_trampoline(x_adjac__mutmut_orig, x_adjac__mutmut_mutants, args, kwargs)
  return result 

adjac.__signature__ = _mutmut_signature(x_adjac__mutmut_orig)
x_adjac__mutmut_orig.__name__ = 'x_adjac'
def x_get_coordinates__mutmut_orig(test_tup):
  return list(adjac(test_tup))
def x_get_coordinates__mutmut_1(test_tup):
  return list(None)
def x_get_coordinates__mutmut_2(test_tup):
  return list(adjac(None))

x_get_coordinates__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_coordinates__mutmut_1': x_get_coordinates__mutmut_1, 
    'x_get_coordinates__mutmut_2': x_get_coordinates__mutmut_2
}

def get_coordinates(*args, **kwargs):
  result = _mutmut_trampoline(x_get_coordinates__mutmut_orig, x_get_coordinates__mutmut_mutants, args, kwargs)
  return result 

get_coordinates.__signature__ = _mutmut_signature(x_get_coordinates__mutmut_orig)
x_get_coordinates__mutmut_orig.__name__ = 'x_get_coordinates'