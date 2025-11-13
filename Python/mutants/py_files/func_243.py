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
def x_check_monthnumb_number__mutmut_orig(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_1(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 and monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_2(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 and monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_3(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 and monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_4(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 and monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_5(monthnum2):
  if(monthnum2==1 or monthnum2==3 and monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_6(monthnum2):
  if(monthnum2==1 and monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_7(monthnum2):
  if(monthnum2 != 1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_8(monthnum2):
  if(monthnum2==2 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_9(monthnum2):
  if(monthnum2==1 or monthnum2 != 3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_10(monthnum2):
  if(monthnum2==1 or monthnum2==4 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_11(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2 != 5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_12(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==6 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_13(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2 != 7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_14(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==8 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_15(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2 != 8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_16(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==9 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_17(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2 != 10 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_18(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==11 or monthnum2==12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_19(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2 != 12):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_20(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==13):
    return True
  else:
    return False
def x_check_monthnumb_number__mutmut_21(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return False
  else:
    return False
def x_check_monthnumb_number__mutmut_22(monthnum2):
  if(monthnum2==1 or monthnum2==3 or monthnum2==5 or monthnum2==7 or monthnum2==8 or monthnum2==10 or monthnum2==12):
    return True
  else:
    return True

x_check_monthnumb_number__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_monthnumb_number__mutmut_1': x_check_monthnumb_number__mutmut_1, 
    'x_check_monthnumb_number__mutmut_2': x_check_monthnumb_number__mutmut_2, 
    'x_check_monthnumb_number__mutmut_3': x_check_monthnumb_number__mutmut_3, 
    'x_check_monthnumb_number__mutmut_4': x_check_monthnumb_number__mutmut_4, 
    'x_check_monthnumb_number__mutmut_5': x_check_monthnumb_number__mutmut_5, 
    'x_check_monthnumb_number__mutmut_6': x_check_monthnumb_number__mutmut_6, 
    'x_check_monthnumb_number__mutmut_7': x_check_monthnumb_number__mutmut_7, 
    'x_check_monthnumb_number__mutmut_8': x_check_monthnumb_number__mutmut_8, 
    'x_check_monthnumb_number__mutmut_9': x_check_monthnumb_number__mutmut_9, 
    'x_check_monthnumb_number__mutmut_10': x_check_monthnumb_number__mutmut_10, 
    'x_check_monthnumb_number__mutmut_11': x_check_monthnumb_number__mutmut_11, 
    'x_check_monthnumb_number__mutmut_12': x_check_monthnumb_number__mutmut_12, 
    'x_check_monthnumb_number__mutmut_13': x_check_monthnumb_number__mutmut_13, 
    'x_check_monthnumb_number__mutmut_14': x_check_monthnumb_number__mutmut_14, 
    'x_check_monthnumb_number__mutmut_15': x_check_monthnumb_number__mutmut_15, 
    'x_check_monthnumb_number__mutmut_16': x_check_monthnumb_number__mutmut_16, 
    'x_check_monthnumb_number__mutmut_17': x_check_monthnumb_number__mutmut_17, 
    'x_check_monthnumb_number__mutmut_18': x_check_monthnumb_number__mutmut_18, 
    'x_check_monthnumb_number__mutmut_19': x_check_monthnumb_number__mutmut_19, 
    'x_check_monthnumb_number__mutmut_20': x_check_monthnumb_number__mutmut_20, 
    'x_check_monthnumb_number__mutmut_21': x_check_monthnumb_number__mutmut_21, 
    'x_check_monthnumb_number__mutmut_22': x_check_monthnumb_number__mutmut_22
}

def check_monthnumb_number(*args, **kwargs):
  result = _mutmut_trampoline(x_check_monthnumb_number__mutmut_orig, x_check_monthnumb_number__mutmut_mutants, args, kwargs)
  return result 

check_monthnumb_number.__signature__ = _mutmut_signature(x_check_monthnumb_number__mutmut_orig)
x_check_monthnumb_number__mutmut_orig.__name__ = 'x_check_monthnumb_number'