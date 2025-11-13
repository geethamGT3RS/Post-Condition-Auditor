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
def x_remove_odd__mutmut_orig(l):
    for i in l:
        if i % 2 != 0:
            l.remove(i)
    return l
def x_remove_odd__mutmut_1(l):
    for i in l:
        if i / 2 != 0:
            l.remove(i)
    return l
def x_remove_odd__mutmut_2(l):
    for i in l:
        if i % 3 != 0:
            l.remove(i)
    return l
def x_remove_odd__mutmut_3(l):
    for i in l:
        if i % 2 == 0:
            l.remove(i)
    return l
def x_remove_odd__mutmut_4(l):
    for i in l:
        if i % 2 != 1:
            l.remove(i)
    return l
def x_remove_odd__mutmut_5(l):
    for i in l:
        if i % 2 != 0:
            l.remove(None)
    return l

x_remove_odd__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_odd__mutmut_1': x_remove_odd__mutmut_1, 
    'x_remove_odd__mutmut_2': x_remove_odd__mutmut_2, 
    'x_remove_odd__mutmut_3': x_remove_odd__mutmut_3, 
    'x_remove_odd__mutmut_4': x_remove_odd__mutmut_4, 
    'x_remove_odd__mutmut_5': x_remove_odd__mutmut_5
}

def remove_odd(*args, **kwargs):
    result = _mutmut_trampoline(x_remove_odd__mutmut_orig, x_remove_odd__mutmut_mutants, args, kwargs)
    return result 

remove_odd.__signature__ = _mutmut_signature(x_remove_odd__mutmut_orig)
x_remove_odd__mutmut_orig.__name__ = 'x_remove_odd'