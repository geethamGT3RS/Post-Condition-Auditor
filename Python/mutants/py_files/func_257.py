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
def x_check_Consecutive__mutmut_orig(l): 
    return sorted(l) == list(range(min(l),max(l)+1)) 
def x_check_Consecutive__mutmut_1(l): 
    return sorted(None) == list(range(min(l),max(l)+1)) 
def x_check_Consecutive__mutmut_2(l): 
    return sorted(l) != list(range(min(l),max(l)+1)) 
def x_check_Consecutive__mutmut_3(l): 
    return sorted(l) == list(None) 
def x_check_Consecutive__mutmut_4(l): 
    return sorted(l) == list(range(None,max(l)+1)) 
def x_check_Consecutive__mutmut_5(l): 
    return sorted(l) == list(range(min(l),None)) 
def x_check_Consecutive__mutmut_6(l): 
    return sorted(l) == list(range(max(l)+1)) 
def x_check_Consecutive__mutmut_7(l): 
    return sorted(l) == list(range(min(l),)) 
def x_check_Consecutive__mutmut_8(l): 
    return sorted(l) == list(range(min(None),max(l)+1)) 
def x_check_Consecutive__mutmut_9(l): 
    return sorted(l) == list(range(min(l),max(l) - 1)) 
def x_check_Consecutive__mutmut_10(l): 
    return sorted(l) == list(range(min(l),max(None)+1)) 
def x_check_Consecutive__mutmut_11(l): 
    return sorted(l) == list(range(min(l),max(l)+2)) 

x_check_Consecutive__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_Consecutive__mutmut_1': x_check_Consecutive__mutmut_1, 
    'x_check_Consecutive__mutmut_2': x_check_Consecutive__mutmut_2, 
    'x_check_Consecutive__mutmut_3': x_check_Consecutive__mutmut_3, 
    'x_check_Consecutive__mutmut_4': x_check_Consecutive__mutmut_4, 
    'x_check_Consecutive__mutmut_5': x_check_Consecutive__mutmut_5, 
    'x_check_Consecutive__mutmut_6': x_check_Consecutive__mutmut_6, 
    'x_check_Consecutive__mutmut_7': x_check_Consecutive__mutmut_7, 
    'x_check_Consecutive__mutmut_8': x_check_Consecutive__mutmut_8, 
    'x_check_Consecutive__mutmut_9': x_check_Consecutive__mutmut_9, 
    'x_check_Consecutive__mutmut_10': x_check_Consecutive__mutmut_10, 
    'x_check_Consecutive__mutmut_11': x_check_Consecutive__mutmut_11
}

def check_Consecutive(*args, **kwargs):
    result = _mutmut_trampoline(x_check_Consecutive__mutmut_orig, x_check_Consecutive__mutmut_mutants, args, kwargs)
    return result 

check_Consecutive.__signature__ = _mutmut_signature(x_check_Consecutive__mutmut_orig)
x_check_Consecutive__mutmut_orig.__name__ = 'x_check_Consecutive'