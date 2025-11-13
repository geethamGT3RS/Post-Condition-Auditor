import bisect
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
def x_right_insertion__mutmut_orig(a, x):
    return bisect.bisect_right(a, x)
def x_right_insertion__mutmut_1(a, x):
    return bisect.bisect_right(None, x)
def x_right_insertion__mutmut_2(a, x):
    return bisect.bisect_right(a, None)
def x_right_insertion__mutmut_3(a, x):
    return bisect.bisect_right(x)
def x_right_insertion__mutmut_4(a, x):
    return bisect.bisect_right(a, )

x_right_insertion__mutmut_mutants : ClassVar[MutantDict] = {
'x_right_insertion__mutmut_1': x_right_insertion__mutmut_1, 
    'x_right_insertion__mutmut_2': x_right_insertion__mutmut_2, 
    'x_right_insertion__mutmut_3': x_right_insertion__mutmut_3, 
    'x_right_insertion__mutmut_4': x_right_insertion__mutmut_4
}

def right_insertion(*args, **kwargs):
    result = _mutmut_trampoline(x_right_insertion__mutmut_orig, x_right_insertion__mutmut_mutants, args, kwargs)
    return result 

right_insertion.__signature__ = _mutmut_signature(x_right_insertion__mutmut_orig)
x_right_insertion__mutmut_orig.__name__ = 'x_right_insertion'