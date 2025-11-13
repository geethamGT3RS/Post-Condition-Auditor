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
def x_check_integer__mutmut_orig(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_1(text):
 text = None
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_2(text):
 text = text.strip()
 if len(text) <= 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_3(text):
 text = text.strip()
 if len(text) < 2:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_4(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(None):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_5(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] not in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_6(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "XX0123456789XX" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_7(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(None)):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_8(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return False
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_9(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") or all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_10(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[1] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_11(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] not in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_12(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "XX+-XX") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_13(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(None):
         return True
     else:
        return False
def x_check_integer__mutmut_14(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] not in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_15(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "XX0123456789XX" for i in range(1,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_16(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(None,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_17(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,None)):
         return True
     else:
        return False
def x_check_integer__mutmut_18(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_19(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,)):
         return True
     else:
        return False
def x_check_integer__mutmut_20(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(2,len(text))):
         return True
     else:
        return False
def x_check_integer__mutmut_21(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return False
     else:
        return False
def x_check_integer__mutmut_22(text):
 text = text.strip()
 if len(text) < 1:
    return None
 else:
     if all(text[i] in "0123456789" for i in range(len(text))):
          return True
     elif (text[0] in "+-") and \
         all(text[i] in "0123456789" for i in range(1,len(text))):
         return True
     else:
        return True

x_check_integer__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_integer__mutmut_1': x_check_integer__mutmut_1, 
    'x_check_integer__mutmut_2': x_check_integer__mutmut_2, 
    'x_check_integer__mutmut_3': x_check_integer__mutmut_3, 
    'x_check_integer__mutmut_4': x_check_integer__mutmut_4, 
    'x_check_integer__mutmut_5': x_check_integer__mutmut_5, 
    'x_check_integer__mutmut_6': x_check_integer__mutmut_6, 
    'x_check_integer__mutmut_7': x_check_integer__mutmut_7, 
    'x_check_integer__mutmut_8': x_check_integer__mutmut_8, 
    'x_check_integer__mutmut_9': x_check_integer__mutmut_9, 
    'x_check_integer__mutmut_10': x_check_integer__mutmut_10, 
    'x_check_integer__mutmut_11': x_check_integer__mutmut_11, 
    'x_check_integer__mutmut_12': x_check_integer__mutmut_12, 
    'x_check_integer__mutmut_13': x_check_integer__mutmut_13, 
    'x_check_integer__mutmut_14': x_check_integer__mutmut_14, 
    'x_check_integer__mutmut_15': x_check_integer__mutmut_15, 
    'x_check_integer__mutmut_16': x_check_integer__mutmut_16, 
    'x_check_integer__mutmut_17': x_check_integer__mutmut_17, 
    'x_check_integer__mutmut_18': x_check_integer__mutmut_18, 
    'x_check_integer__mutmut_19': x_check_integer__mutmut_19, 
    'x_check_integer__mutmut_20': x_check_integer__mutmut_20, 
    'x_check_integer__mutmut_21': x_check_integer__mutmut_21, 
    'x_check_integer__mutmut_22': x_check_integer__mutmut_22
}

def check_integer(*args, **kwargs):
 result = _mutmut_trampoline(x_check_integer__mutmut_orig, x_check_integer__mutmut_mutants, args, kwargs)
 return result 

check_integer.__signature__ = _mutmut_signature(x_check_integer__mutmut_orig)
x_check_integer__mutmut_orig.__name__ = 'x_check_integer'