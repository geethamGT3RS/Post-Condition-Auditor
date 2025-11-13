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
def x_find_Rotations__mutmut_orig(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_1(str): 
    tmp = None
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_2(str): 
    tmp = str - str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_3(str): 
    tmp = str + str
    n = None 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_4(str): 
    tmp = str + str
    n = len(str) 
    for i in range(None,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_5(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,None): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_6(str): 
    tmp = str + str
    n = len(str) 
    for i in range(n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_7(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_8(str): 
    tmp = str + str
    n = len(str) 
    for i in range(2,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_9(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n - 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_10(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 2): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_11(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = None 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_12(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i - n] 
        if (str == substring): 
            return i 
    return n 
def x_find_Rotations__mutmut_13(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str != substring): 
            return i 
    return n 

x_find_Rotations__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_Rotations__mutmut_1': x_find_Rotations__mutmut_1, 
    'x_find_Rotations__mutmut_2': x_find_Rotations__mutmut_2, 
    'x_find_Rotations__mutmut_3': x_find_Rotations__mutmut_3, 
    'x_find_Rotations__mutmut_4': x_find_Rotations__mutmut_4, 
    'x_find_Rotations__mutmut_5': x_find_Rotations__mutmut_5, 
    'x_find_Rotations__mutmut_6': x_find_Rotations__mutmut_6, 
    'x_find_Rotations__mutmut_7': x_find_Rotations__mutmut_7, 
    'x_find_Rotations__mutmut_8': x_find_Rotations__mutmut_8, 
    'x_find_Rotations__mutmut_9': x_find_Rotations__mutmut_9, 
    'x_find_Rotations__mutmut_10': x_find_Rotations__mutmut_10, 
    'x_find_Rotations__mutmut_11': x_find_Rotations__mutmut_11, 
    'x_find_Rotations__mutmut_12': x_find_Rotations__mutmut_12, 
    'x_find_Rotations__mutmut_13': x_find_Rotations__mutmut_13
}

def find_Rotations(*args, **kwargs):
    result = _mutmut_trampoline(x_find_Rotations__mutmut_orig, x_find_Rotations__mutmut_mutants, args, kwargs)
    return result 

find_Rotations.__signature__ = _mutmut_signature(x_find_Rotations__mutmut_orig)
x_find_Rotations__mutmut_orig.__name__ = 'x_find_Rotations'