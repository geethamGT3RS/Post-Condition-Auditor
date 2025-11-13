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
def x_odd_Equivalent__mutmut_orig(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_1(s,n): 
    count=None
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_2(s,n): 
    count=1
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_3(s,n): 
    count=0
    for i in range(None,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_4(s,n): 
    count=0
    for i in range(0,None): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_5(s,n): 
    count=0
    for i in range(n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_6(s,n): 
    count=0
    for i in range(0,): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_7(s,n): 
    count=0
    for i in range(1,n): 
        if (s[i] == '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_8(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] != '1'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_9(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == 'XX1XX'): 
            count = count + 1
    return count 
def x_odd_Equivalent__mutmut_10(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = None
    return count 
def x_odd_Equivalent__mutmut_11(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count - 1
    return count 
def x_odd_Equivalent__mutmut_12(s,n): 
    count=0
    for i in range(0,n): 
        if (s[i] == '1'): 
            count = count + 2
    return count 

x_odd_Equivalent__mutmut_mutants : ClassVar[MutantDict] = {
'x_odd_Equivalent__mutmut_1': x_odd_Equivalent__mutmut_1, 
    'x_odd_Equivalent__mutmut_2': x_odd_Equivalent__mutmut_2, 
    'x_odd_Equivalent__mutmut_3': x_odd_Equivalent__mutmut_3, 
    'x_odd_Equivalent__mutmut_4': x_odd_Equivalent__mutmut_4, 
    'x_odd_Equivalent__mutmut_5': x_odd_Equivalent__mutmut_5, 
    'x_odd_Equivalent__mutmut_6': x_odd_Equivalent__mutmut_6, 
    'x_odd_Equivalent__mutmut_7': x_odd_Equivalent__mutmut_7, 
    'x_odd_Equivalent__mutmut_8': x_odd_Equivalent__mutmut_8, 
    'x_odd_Equivalent__mutmut_9': x_odd_Equivalent__mutmut_9, 
    'x_odd_Equivalent__mutmut_10': x_odd_Equivalent__mutmut_10, 
    'x_odd_Equivalent__mutmut_11': x_odd_Equivalent__mutmut_11, 
    'x_odd_Equivalent__mutmut_12': x_odd_Equivalent__mutmut_12
}

def odd_Equivalent(*args, **kwargs):
    result = _mutmut_trampoline(x_odd_Equivalent__mutmut_orig, x_odd_Equivalent__mutmut_mutants, args, kwargs)
    return result 

odd_Equivalent.__signature__ = _mutmut_signature(x_odd_Equivalent__mutmut_orig)
x_odd_Equivalent__mutmut_orig.__name__ = 'x_odd_Equivalent'