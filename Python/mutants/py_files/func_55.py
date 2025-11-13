import sys
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
def x_next_smallest_palindrome__mutmut_orig(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_1(num):
    numstr = None
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_2(num):
    numstr = str(None)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_3(num):
    numstr = str(num)
    for i in range(None,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_4(num):
    numstr = str(num)
    for i in range(num+1,None):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_5(num):
    numstr = str(num)
    for i in range(sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_6(num):
    numstr = str(num)
    for i in range(num+1,):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_7(num):
    numstr = str(num)
    for i in range(num - 1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_8(num):
    numstr = str(num)
    for i in range(num+2,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_9(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(None) == str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_10(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) != str(i)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_11(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(None)[::-1]:
            return i
def x_next_smallest_palindrome__mutmut_12(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::+1]:
            return i
def x_next_smallest_palindrome__mutmut_13(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-2]:
            return i

x_next_smallest_palindrome__mutmut_mutants : ClassVar[MutantDict] = {
'x_next_smallest_palindrome__mutmut_1': x_next_smallest_palindrome__mutmut_1, 
    'x_next_smallest_palindrome__mutmut_2': x_next_smallest_palindrome__mutmut_2, 
    'x_next_smallest_palindrome__mutmut_3': x_next_smallest_palindrome__mutmut_3, 
    'x_next_smallest_palindrome__mutmut_4': x_next_smallest_palindrome__mutmut_4, 
    'x_next_smallest_palindrome__mutmut_5': x_next_smallest_palindrome__mutmut_5, 
    'x_next_smallest_palindrome__mutmut_6': x_next_smallest_palindrome__mutmut_6, 
    'x_next_smallest_palindrome__mutmut_7': x_next_smallest_palindrome__mutmut_7, 
    'x_next_smallest_palindrome__mutmut_8': x_next_smallest_palindrome__mutmut_8, 
    'x_next_smallest_palindrome__mutmut_9': x_next_smallest_palindrome__mutmut_9, 
    'x_next_smallest_palindrome__mutmut_10': x_next_smallest_palindrome__mutmut_10, 
    'x_next_smallest_palindrome__mutmut_11': x_next_smallest_palindrome__mutmut_11, 
    'x_next_smallest_palindrome__mutmut_12': x_next_smallest_palindrome__mutmut_12, 
    'x_next_smallest_palindrome__mutmut_13': x_next_smallest_palindrome__mutmut_13
}

def next_smallest_palindrome(*args, **kwargs):
    result = _mutmut_trampoline(x_next_smallest_palindrome__mutmut_orig, x_next_smallest_palindrome__mutmut_mutants, args, kwargs)
    return result 

next_smallest_palindrome.__signature__ = _mutmut_signature(x_next_smallest_palindrome__mutmut_orig)
x_next_smallest_palindrome__mutmut_orig.__name__ = 'x_next_smallest_palindrome'