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
def x_sequential_search__mutmut_orig(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_1(dlist, item):
    pos = None
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_2(dlist, item):
    pos = 1
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_3(dlist, item):
    pos = 0
    found = None
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_4(dlist, item):
    pos = 0
    found = True
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_5(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) or not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_6(dlist, item):
    pos = 0
    found = False
    while pos <= len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_7(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_8(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] != item:
            found = True
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_9(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = None
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_10(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = False
        else:
            pos = pos + 1
    return found, pos
def x_sequential_search__mutmut_11(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = None
    return found, pos
def x_sequential_search__mutmut_12(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos - 1
    return found, pos
def x_sequential_search__mutmut_13(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 2
    return found, pos

x_sequential_search__mutmut_mutants : ClassVar[MutantDict] = {
'x_sequential_search__mutmut_1': x_sequential_search__mutmut_1, 
    'x_sequential_search__mutmut_2': x_sequential_search__mutmut_2, 
    'x_sequential_search__mutmut_3': x_sequential_search__mutmut_3, 
    'x_sequential_search__mutmut_4': x_sequential_search__mutmut_4, 
    'x_sequential_search__mutmut_5': x_sequential_search__mutmut_5, 
    'x_sequential_search__mutmut_6': x_sequential_search__mutmut_6, 
    'x_sequential_search__mutmut_7': x_sequential_search__mutmut_7, 
    'x_sequential_search__mutmut_8': x_sequential_search__mutmut_8, 
    'x_sequential_search__mutmut_9': x_sequential_search__mutmut_9, 
    'x_sequential_search__mutmut_10': x_sequential_search__mutmut_10, 
    'x_sequential_search__mutmut_11': x_sequential_search__mutmut_11, 
    'x_sequential_search__mutmut_12': x_sequential_search__mutmut_12, 
    'x_sequential_search__mutmut_13': x_sequential_search__mutmut_13
}

def sequential_search(*args, **kwargs):
    result = _mutmut_trampoline(x_sequential_search__mutmut_orig, x_sequential_search__mutmut_mutants, args, kwargs)
    return result 

sequential_search.__signature__ = _mutmut_signature(x_sequential_search__mutmut_orig)
x_sequential_search__mutmut_orig.__name__ = 'x_sequential_search'