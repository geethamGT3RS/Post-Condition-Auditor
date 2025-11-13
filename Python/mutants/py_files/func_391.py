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
def x_odd_num_sum__mutmut_orig(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_1(n) : 
    j = None
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_2(n) : 
    j = 1
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_3(n) : 
    j = 0
    sm = None
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_4(n) : 
    j = 0
    sm = 1
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_5(n) : 
    j = 0
    sm = 0
    for i in range(None,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_6(n) : 
    j = 0
    sm = 0
    for i in range(1,None) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_7(n) : 
    j = 0
    sm = 0
    for i in range(n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_8(n) : 
    j = 0
    sm = 0
    for i in range(1,) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_9(n) : 
    j = 0
    sm = 0
    for i in range(2,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_10(n) : 
    j = 0
    sm = 0
    for i in range(1,n - 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_11(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 2) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_12(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = None 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_13(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i + 1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_14(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2 / i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_15(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (3*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_16(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-2) 
        sm = sm + (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_17(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = None   
    return sm 
def x_odd_num_sum__mutmut_18(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm - (j*j*j*j)   
    return sm 
def x_odd_num_sum__mutmut_19(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j / j)   
    return sm 
def x_odd_num_sum__mutmut_20(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j / j*j)   
    return sm 
def x_odd_num_sum__mutmut_21(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j / j*j*j)   
    return sm 

x_odd_num_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_odd_num_sum__mutmut_1': x_odd_num_sum__mutmut_1, 
    'x_odd_num_sum__mutmut_2': x_odd_num_sum__mutmut_2, 
    'x_odd_num_sum__mutmut_3': x_odd_num_sum__mutmut_3, 
    'x_odd_num_sum__mutmut_4': x_odd_num_sum__mutmut_4, 
    'x_odd_num_sum__mutmut_5': x_odd_num_sum__mutmut_5, 
    'x_odd_num_sum__mutmut_6': x_odd_num_sum__mutmut_6, 
    'x_odd_num_sum__mutmut_7': x_odd_num_sum__mutmut_7, 
    'x_odd_num_sum__mutmut_8': x_odd_num_sum__mutmut_8, 
    'x_odd_num_sum__mutmut_9': x_odd_num_sum__mutmut_9, 
    'x_odd_num_sum__mutmut_10': x_odd_num_sum__mutmut_10, 
    'x_odd_num_sum__mutmut_11': x_odd_num_sum__mutmut_11, 
    'x_odd_num_sum__mutmut_12': x_odd_num_sum__mutmut_12, 
    'x_odd_num_sum__mutmut_13': x_odd_num_sum__mutmut_13, 
    'x_odd_num_sum__mutmut_14': x_odd_num_sum__mutmut_14, 
    'x_odd_num_sum__mutmut_15': x_odd_num_sum__mutmut_15, 
    'x_odd_num_sum__mutmut_16': x_odd_num_sum__mutmut_16, 
    'x_odd_num_sum__mutmut_17': x_odd_num_sum__mutmut_17, 
    'x_odd_num_sum__mutmut_18': x_odd_num_sum__mutmut_18, 
    'x_odd_num_sum__mutmut_19': x_odd_num_sum__mutmut_19, 
    'x_odd_num_sum__mutmut_20': x_odd_num_sum__mutmut_20, 
    'x_odd_num_sum__mutmut_21': x_odd_num_sum__mutmut_21
}

def odd_num_sum(*args, **kwargs):
    result = _mutmut_trampoline(x_odd_num_sum__mutmut_orig, x_odd_num_sum__mutmut_mutants, args, kwargs)
    return result 

odd_num_sum.__signature__ = _mutmut_signature(x_odd_num_sum__mutmut_orig)
x_odd_num_sum__mutmut_orig.__name__ = 'x_odd_num_sum'