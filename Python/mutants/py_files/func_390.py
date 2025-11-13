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
def x_Diff__mutmut_orig(li1,li2):
    return list(set(li1)-set(li2)) + list(set(li2)-set(li1))
def x_Diff__mutmut_1(li1,li2):
    return list(set(li1)-set(li2)) - list(set(li2)-set(li1))
def x_Diff__mutmut_2(li1,li2):
    return list(None) + list(set(li2)-set(li1))
def x_Diff__mutmut_3(li1,li2):
    return list(set(li1) + set(li2)) + list(set(li2)-set(li1))
def x_Diff__mutmut_4(li1,li2):
    return list(set(None)-set(li2)) + list(set(li2)-set(li1))
def x_Diff__mutmut_5(li1,li2):
    return list(set(li1)-set(None)) + list(set(li2)-set(li1))
def x_Diff__mutmut_6(li1,li2):
    return list(set(li1)-set(li2)) + list(None)
def x_Diff__mutmut_7(li1,li2):
    return list(set(li1)-set(li2)) + list(set(li2) + set(li1))
def x_Diff__mutmut_8(li1,li2):
    return list(set(li1)-set(li2)) + list(set(None)-set(li1))
def x_Diff__mutmut_9(li1,li2):
    return list(set(li1)-set(li2)) + list(set(li2)-set(None))

x_Diff__mutmut_mutants : ClassVar[MutantDict] = {
'x_Diff__mutmut_1': x_Diff__mutmut_1, 
    'x_Diff__mutmut_2': x_Diff__mutmut_2, 
    'x_Diff__mutmut_3': x_Diff__mutmut_3, 
    'x_Diff__mutmut_4': x_Diff__mutmut_4, 
    'x_Diff__mutmut_5': x_Diff__mutmut_5, 
    'x_Diff__mutmut_6': x_Diff__mutmut_6, 
    'x_Diff__mutmut_7': x_Diff__mutmut_7, 
    'x_Diff__mutmut_8': x_Diff__mutmut_8, 
    'x_Diff__mutmut_9': x_Diff__mutmut_9
}

def Diff(*args, **kwargs):
    result = _mutmut_trampoline(x_Diff__mutmut_orig, x_Diff__mutmut_mutants, args, kwargs)
    return result 

Diff.__signature__ = _mutmut_signature(x_Diff__mutmut_orig)
x_Diff__mutmut_orig.__name__ = 'x_Diff'
 