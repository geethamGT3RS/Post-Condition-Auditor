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
def x_is_Monotonic__mutmut_orig(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_1(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) and all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_2(A): 
    return (all(None) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_3(A): 
    return (all(A[i] < A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_4(A): 
    return (all(A[i] <= A[i - 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_5(A): 
    return (all(A[i] <= A[i + 2] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_6(A): 
    return (all(A[i] <= A[i + 1] for i in range(None)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_7(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) + 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_8(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 2)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_9(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(None)) 
def x_is_Monotonic__mutmut_10(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] > A[i + 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_11(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i - 1] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_12(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 2] for i in range(len(A) - 1))) 
def x_is_Monotonic__mutmut_13(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(None))) 
def x_is_Monotonic__mutmut_14(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) + 1))) 
def x_is_Monotonic__mutmut_15(A): 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 2))) 

x_is_Monotonic__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_Monotonic__mutmut_1': x_is_Monotonic__mutmut_1, 
    'x_is_Monotonic__mutmut_2': x_is_Monotonic__mutmut_2, 
    'x_is_Monotonic__mutmut_3': x_is_Monotonic__mutmut_3, 
    'x_is_Monotonic__mutmut_4': x_is_Monotonic__mutmut_4, 
    'x_is_Monotonic__mutmut_5': x_is_Monotonic__mutmut_5, 
    'x_is_Monotonic__mutmut_6': x_is_Monotonic__mutmut_6, 
    'x_is_Monotonic__mutmut_7': x_is_Monotonic__mutmut_7, 
    'x_is_Monotonic__mutmut_8': x_is_Monotonic__mutmut_8, 
    'x_is_Monotonic__mutmut_9': x_is_Monotonic__mutmut_9, 
    'x_is_Monotonic__mutmut_10': x_is_Monotonic__mutmut_10, 
    'x_is_Monotonic__mutmut_11': x_is_Monotonic__mutmut_11, 
    'x_is_Monotonic__mutmut_12': x_is_Monotonic__mutmut_12, 
    'x_is_Monotonic__mutmut_13': x_is_Monotonic__mutmut_13, 
    'x_is_Monotonic__mutmut_14': x_is_Monotonic__mutmut_14, 
    'x_is_Monotonic__mutmut_15': x_is_Monotonic__mutmut_15
}

def is_Monotonic(*args, **kwargs):
    result = _mutmut_trampoline(x_is_Monotonic__mutmut_orig, x_is_Monotonic__mutmut_mutants, args, kwargs)
    return result 

is_Monotonic.__signature__ = _mutmut_signature(x_is_Monotonic__mutmut_orig)
x_is_Monotonic__mutmut_orig.__name__ = 'x_is_Monotonic'