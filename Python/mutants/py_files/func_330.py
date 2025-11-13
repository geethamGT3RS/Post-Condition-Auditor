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
def x_find_First_Missing__mutmut_orig(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_1(array,start=1,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_2(array,start=0,end=None):
    if end is not None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_3(array,start=0,end=None):
    if end is None:
      end = None   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_4(array,start=0,end=None):
    if end is None:
      end = len(array) + 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_5(array,start=0,end=None):
    if end is None:
      end = len(array) - 2   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_6(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start >= end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_7(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end - 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_8(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 2
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_9(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start == array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_10(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = None 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_11(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int(None) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_12(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) * 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_13(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start - end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_14(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 3) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_15(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] != mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_16(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(None,mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_17(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,None,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_18(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,None) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_19(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(mid+1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_20(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_21(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_22(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid - 1,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_23(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+2,end) 
    return find_First_Missing(array,start,mid) 
def x_find_First_Missing__mutmut_24(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(None,start,mid) 
def x_find_First_Missing__mutmut_25(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,None,mid) 
def x_find_First_Missing__mutmut_26(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,None) 
def x_find_First_Missing__mutmut_27(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(start,mid) 
def x_find_First_Missing__mutmut_28(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,mid) 
def x_find_First_Missing__mutmut_29(array,start=0,end=None):
    if end is None:
      end = len(array) - 1   
    if (start > end): 
        return end + 1
    if (start != array[start]): 
        return start; 
    mid = int((start + end) / 2) 
    if (array[mid] == mid): 
        return find_First_Missing(array,mid+1,end) 
    return find_First_Missing(array,start,) 

x_find_First_Missing__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_First_Missing__mutmut_1': x_find_First_Missing__mutmut_1, 
    'x_find_First_Missing__mutmut_2': x_find_First_Missing__mutmut_2, 
    'x_find_First_Missing__mutmut_3': x_find_First_Missing__mutmut_3, 
    'x_find_First_Missing__mutmut_4': x_find_First_Missing__mutmut_4, 
    'x_find_First_Missing__mutmut_5': x_find_First_Missing__mutmut_5, 
    'x_find_First_Missing__mutmut_6': x_find_First_Missing__mutmut_6, 
    'x_find_First_Missing__mutmut_7': x_find_First_Missing__mutmut_7, 
    'x_find_First_Missing__mutmut_8': x_find_First_Missing__mutmut_8, 
    'x_find_First_Missing__mutmut_9': x_find_First_Missing__mutmut_9, 
    'x_find_First_Missing__mutmut_10': x_find_First_Missing__mutmut_10, 
    'x_find_First_Missing__mutmut_11': x_find_First_Missing__mutmut_11, 
    'x_find_First_Missing__mutmut_12': x_find_First_Missing__mutmut_12, 
    'x_find_First_Missing__mutmut_13': x_find_First_Missing__mutmut_13, 
    'x_find_First_Missing__mutmut_14': x_find_First_Missing__mutmut_14, 
    'x_find_First_Missing__mutmut_15': x_find_First_Missing__mutmut_15, 
    'x_find_First_Missing__mutmut_16': x_find_First_Missing__mutmut_16, 
    'x_find_First_Missing__mutmut_17': x_find_First_Missing__mutmut_17, 
    'x_find_First_Missing__mutmut_18': x_find_First_Missing__mutmut_18, 
    'x_find_First_Missing__mutmut_19': x_find_First_Missing__mutmut_19, 
    'x_find_First_Missing__mutmut_20': x_find_First_Missing__mutmut_20, 
    'x_find_First_Missing__mutmut_21': x_find_First_Missing__mutmut_21, 
    'x_find_First_Missing__mutmut_22': x_find_First_Missing__mutmut_22, 
    'x_find_First_Missing__mutmut_23': x_find_First_Missing__mutmut_23, 
    'x_find_First_Missing__mutmut_24': x_find_First_Missing__mutmut_24, 
    'x_find_First_Missing__mutmut_25': x_find_First_Missing__mutmut_25, 
    'x_find_First_Missing__mutmut_26': x_find_First_Missing__mutmut_26, 
    'x_find_First_Missing__mutmut_27': x_find_First_Missing__mutmut_27, 
    'x_find_First_Missing__mutmut_28': x_find_First_Missing__mutmut_28, 
    'x_find_First_Missing__mutmut_29': x_find_First_Missing__mutmut_29
}

def find_First_Missing(*args, **kwargs):
    result = _mutmut_trampoline(x_find_First_Missing__mutmut_orig, x_find_First_Missing__mutmut_mutants, args, kwargs)
    return result 

find_First_Missing.__signature__ = _mutmut_signature(x_find_First_Missing__mutmut_orig)
x_find_First_Missing__mutmut_orig.__name__ = 'x_find_First_Missing'