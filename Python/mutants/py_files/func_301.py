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
def x_diff_even_odd__mutmut_orig(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_1(list1):
    first_even = None
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_2(list1):
    first_even = next(None,-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_3(list1):
    first_even = next((el for el in list1 if el%2==0),None)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_4(list1):
    first_even = next(-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_5(list1):
    first_even = next((el for el in list1 if el%2==0),)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_6(list1):
    first_even = next((el for el in list1 if el / 2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_7(list1):
    first_even = next((el for el in list1 if el%3==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_8(list1):
    first_even = next((el for el in list1 if el%2 != 0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_9(list1):
    first_even = next((el for el in list1 if el%2==1),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_10(list1):
    first_even = next((el for el in list1 if el%2==0),+1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_11(list1):
    first_even = next((el for el in list1 if el%2==0),-2)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_12(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = None
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_13(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next(None,-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_14(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),None)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_15(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next(-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_16(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_17(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el / 2!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_18(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%3!=0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_19(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2 == 0),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_20(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=1),-1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_21(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),+1)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_22(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-2)
    return (first_even-first_odd)
def x_diff_even_odd__mutmut_23(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even + first_odd)

x_diff_even_odd__mutmut_mutants : ClassVar[MutantDict] = {
'x_diff_even_odd__mutmut_1': x_diff_even_odd__mutmut_1, 
    'x_diff_even_odd__mutmut_2': x_diff_even_odd__mutmut_2, 
    'x_diff_even_odd__mutmut_3': x_diff_even_odd__mutmut_3, 
    'x_diff_even_odd__mutmut_4': x_diff_even_odd__mutmut_4, 
    'x_diff_even_odd__mutmut_5': x_diff_even_odd__mutmut_5, 
    'x_diff_even_odd__mutmut_6': x_diff_even_odd__mutmut_6, 
    'x_diff_even_odd__mutmut_7': x_diff_even_odd__mutmut_7, 
    'x_diff_even_odd__mutmut_8': x_diff_even_odd__mutmut_8, 
    'x_diff_even_odd__mutmut_9': x_diff_even_odd__mutmut_9, 
    'x_diff_even_odd__mutmut_10': x_diff_even_odd__mutmut_10, 
    'x_diff_even_odd__mutmut_11': x_diff_even_odd__mutmut_11, 
    'x_diff_even_odd__mutmut_12': x_diff_even_odd__mutmut_12, 
    'x_diff_even_odd__mutmut_13': x_diff_even_odd__mutmut_13, 
    'x_diff_even_odd__mutmut_14': x_diff_even_odd__mutmut_14, 
    'x_diff_even_odd__mutmut_15': x_diff_even_odd__mutmut_15, 
    'x_diff_even_odd__mutmut_16': x_diff_even_odd__mutmut_16, 
    'x_diff_even_odd__mutmut_17': x_diff_even_odd__mutmut_17, 
    'x_diff_even_odd__mutmut_18': x_diff_even_odd__mutmut_18, 
    'x_diff_even_odd__mutmut_19': x_diff_even_odd__mutmut_19, 
    'x_diff_even_odd__mutmut_20': x_diff_even_odd__mutmut_20, 
    'x_diff_even_odd__mutmut_21': x_diff_even_odd__mutmut_21, 
    'x_diff_even_odd__mutmut_22': x_diff_even_odd__mutmut_22, 
    'x_diff_even_odd__mutmut_23': x_diff_even_odd__mutmut_23
}

def diff_even_odd(*args, **kwargs):
    result = _mutmut_trampoline(x_diff_even_odd__mutmut_orig, x_diff_even_odd__mutmut_mutants, args, kwargs)
    return result 

diff_even_odd.__signature__ = _mutmut_signature(x_diff_even_odd__mutmut_orig)
x_diff_even_odd__mutmut_orig.__name__ = 'x_diff_even_odd'