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
def x_all_Characters_Same__mutmut_orig(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_1(s) :
    n = None
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_2(s) :
    n = len(s)
    for i in range(None,n) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_3(s) :
    n = len(s)
    for i in range(1,None) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_4(s) :
    n = len(s)
    for i in range(n) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_5(s) :
    n = len(s)
    for i in range(1,) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_6(s) :
    n = len(s)
    for i in range(2,n) :
        if s[i] != s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_7(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] == s[0] :
            return False
    return True
def x_all_Characters_Same__mutmut_8(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[1] :
            return False
    return True
def x_all_Characters_Same__mutmut_9(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return True
    return True
def x_all_Characters_Same__mutmut_10(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return False

x_all_Characters_Same__mutmut_mutants : ClassVar[MutantDict] = {
'x_all_Characters_Same__mutmut_1': x_all_Characters_Same__mutmut_1, 
    'x_all_Characters_Same__mutmut_2': x_all_Characters_Same__mutmut_2, 
    'x_all_Characters_Same__mutmut_3': x_all_Characters_Same__mutmut_3, 
    'x_all_Characters_Same__mutmut_4': x_all_Characters_Same__mutmut_4, 
    'x_all_Characters_Same__mutmut_5': x_all_Characters_Same__mutmut_5, 
    'x_all_Characters_Same__mutmut_6': x_all_Characters_Same__mutmut_6, 
    'x_all_Characters_Same__mutmut_7': x_all_Characters_Same__mutmut_7, 
    'x_all_Characters_Same__mutmut_8': x_all_Characters_Same__mutmut_8, 
    'x_all_Characters_Same__mutmut_9': x_all_Characters_Same__mutmut_9, 
    'x_all_Characters_Same__mutmut_10': x_all_Characters_Same__mutmut_10
}

def all_Characters_Same(*args, **kwargs):
    result = _mutmut_trampoline(x_all_Characters_Same__mutmut_orig, x_all_Characters_Same__mutmut_mutants, args, kwargs)
    return result 

all_Characters_Same.__signature__ = _mutmut_signature(x_all_Characters_Same__mutmut_orig)
x_all_Characters_Same__mutmut_orig.__name__ = 'x_all_Characters_Same'