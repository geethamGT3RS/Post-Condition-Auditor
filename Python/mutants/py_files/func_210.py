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
def x_cube_Sum__mutmut_orig(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_1(n): 
    sum = None
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_2(n): 
    sum = 1
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_3(n): 
    sum = 0
    for i in range(None,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_4(n): 
    sum = 0
    for i in range(1,None): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_5(n): 
    sum = 0
    for i in range(n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_6(n): 
    sum = 0
    for i in range(1,): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_7(n): 
    sum = 0
    for i in range(2,n + 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_8(n): 
    sum = 0
    for i in range(1,n - 1): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_9(n): 
    sum = 0
    for i in range(1,n + 2): 
        sum += (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_10(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum = (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_11(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum -= (2*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_12(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i) / (2*i) 
    return sum
def x_cube_Sum__mutmut_13(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i) / (2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_14(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2 / i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_15(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (3*i)*(2*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_16(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2 / i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_17(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(3*i)*(2*i) 
    return sum
def x_cube_Sum__mutmut_18(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(2 / i) 
    return sum
def x_cube_Sum__mutmut_19(n): 
    sum = 0
    for i in range(1,n + 1): 
        sum += (2*i)*(2*i)*(3*i) 
    return sum

x_cube_Sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_cube_Sum__mutmut_1': x_cube_Sum__mutmut_1, 
    'x_cube_Sum__mutmut_2': x_cube_Sum__mutmut_2, 
    'x_cube_Sum__mutmut_3': x_cube_Sum__mutmut_3, 
    'x_cube_Sum__mutmut_4': x_cube_Sum__mutmut_4, 
    'x_cube_Sum__mutmut_5': x_cube_Sum__mutmut_5, 
    'x_cube_Sum__mutmut_6': x_cube_Sum__mutmut_6, 
    'x_cube_Sum__mutmut_7': x_cube_Sum__mutmut_7, 
    'x_cube_Sum__mutmut_8': x_cube_Sum__mutmut_8, 
    'x_cube_Sum__mutmut_9': x_cube_Sum__mutmut_9, 
    'x_cube_Sum__mutmut_10': x_cube_Sum__mutmut_10, 
    'x_cube_Sum__mutmut_11': x_cube_Sum__mutmut_11, 
    'x_cube_Sum__mutmut_12': x_cube_Sum__mutmut_12, 
    'x_cube_Sum__mutmut_13': x_cube_Sum__mutmut_13, 
    'x_cube_Sum__mutmut_14': x_cube_Sum__mutmut_14, 
    'x_cube_Sum__mutmut_15': x_cube_Sum__mutmut_15, 
    'x_cube_Sum__mutmut_16': x_cube_Sum__mutmut_16, 
    'x_cube_Sum__mutmut_17': x_cube_Sum__mutmut_17, 
    'x_cube_Sum__mutmut_18': x_cube_Sum__mutmut_18, 
    'x_cube_Sum__mutmut_19': x_cube_Sum__mutmut_19
}

def cube_Sum(*args, **kwargs):
    result = _mutmut_trampoline(x_cube_Sum__mutmut_orig, x_cube_Sum__mutmut_mutants, args, kwargs)
    return result 

cube_Sum.__signature__ = _mutmut_signature(x_cube_Sum__mutmut_orig)
x_cube_Sum__mutmut_orig.__name__ = 'x_cube_Sum'