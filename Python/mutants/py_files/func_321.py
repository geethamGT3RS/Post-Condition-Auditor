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
def x_min_Jumps__mutmut_orig(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_1(steps, d): 
    (a, b) = None
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_2(steps, d): 
    (a, b) = steps
    temp = None 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_3(steps, d): 
    (a, b) = steps
    temp = a 
    a = None 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_4(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(None, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_5(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, None) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_6(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_7(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, ) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_8(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = None 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_9(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(None, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_10(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, None) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_11(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_12(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, ) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_13(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d > b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_14(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) * b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_15(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b + 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_16(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d - b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_17(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 2) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_18(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d != 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_19(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 1): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_20(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 1
    if (d == a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_21(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d != a): 
        return 1
    else:
        return 2
def x_min_Jumps__mutmut_22(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 2
    else:
        return 2
def x_min_Jumps__mutmut_23(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 3

x_min_Jumps__mutmut_mutants : ClassVar[MutantDict] = {
'x_min_Jumps__mutmut_1': x_min_Jumps__mutmut_1, 
    'x_min_Jumps__mutmut_2': x_min_Jumps__mutmut_2, 
    'x_min_Jumps__mutmut_3': x_min_Jumps__mutmut_3, 
    'x_min_Jumps__mutmut_4': x_min_Jumps__mutmut_4, 
    'x_min_Jumps__mutmut_5': x_min_Jumps__mutmut_5, 
    'x_min_Jumps__mutmut_6': x_min_Jumps__mutmut_6, 
    'x_min_Jumps__mutmut_7': x_min_Jumps__mutmut_7, 
    'x_min_Jumps__mutmut_8': x_min_Jumps__mutmut_8, 
    'x_min_Jumps__mutmut_9': x_min_Jumps__mutmut_9, 
    'x_min_Jumps__mutmut_10': x_min_Jumps__mutmut_10, 
    'x_min_Jumps__mutmut_11': x_min_Jumps__mutmut_11, 
    'x_min_Jumps__mutmut_12': x_min_Jumps__mutmut_12, 
    'x_min_Jumps__mutmut_13': x_min_Jumps__mutmut_13, 
    'x_min_Jumps__mutmut_14': x_min_Jumps__mutmut_14, 
    'x_min_Jumps__mutmut_15': x_min_Jumps__mutmut_15, 
    'x_min_Jumps__mutmut_16': x_min_Jumps__mutmut_16, 
    'x_min_Jumps__mutmut_17': x_min_Jumps__mutmut_17, 
    'x_min_Jumps__mutmut_18': x_min_Jumps__mutmut_18, 
    'x_min_Jumps__mutmut_19': x_min_Jumps__mutmut_19, 
    'x_min_Jumps__mutmut_20': x_min_Jumps__mutmut_20, 
    'x_min_Jumps__mutmut_21': x_min_Jumps__mutmut_21, 
    'x_min_Jumps__mutmut_22': x_min_Jumps__mutmut_22, 
    'x_min_Jumps__mutmut_23': x_min_Jumps__mutmut_23
}

def min_Jumps(*args, **kwargs):
    result = _mutmut_trampoline(x_min_Jumps__mutmut_orig, x_min_Jumps__mutmut_mutants, args, kwargs)
    return result 

min_Jumps.__signature__ = _mutmut_signature(x_min_Jumps__mutmut_orig)
x_min_Jumps__mutmut_orig.__name__ = 'x_min_Jumps'