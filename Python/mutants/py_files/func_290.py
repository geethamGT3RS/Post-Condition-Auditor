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
def x_catalan_number__mutmut_orig(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_1(num):
    if num < 1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_2(num):
    if num <=2:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_3(num):
    if num <=1:
         return 2   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_4(num):
    if num <=1:
         return 1   
    res_num = None
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_5(num):
    if num <=1:
         return 1   
    res_num = 1
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_6(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(None):
        res_num += catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_7(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num = catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_8(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num -= catalan_number(i) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_9(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) / catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_10(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(None) * catalan_number(num-i-1)
    return res_num
def x_catalan_number__mutmut_11(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(None)
    return res_num
def x_catalan_number__mutmut_12(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i + 1)
    return res_num
def x_catalan_number__mutmut_13(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num + i-1)
    return res_num
def x_catalan_number__mutmut_14(num):
    if num <=1:
         return 1   
    res_num = 0
    for i in range(num):
        res_num += catalan_number(i) * catalan_number(num-i-2)
    return res_num

x_catalan_number__mutmut_mutants : ClassVar[MutantDict] = {
'x_catalan_number__mutmut_1': x_catalan_number__mutmut_1, 
    'x_catalan_number__mutmut_2': x_catalan_number__mutmut_2, 
    'x_catalan_number__mutmut_3': x_catalan_number__mutmut_3, 
    'x_catalan_number__mutmut_4': x_catalan_number__mutmut_4, 
    'x_catalan_number__mutmut_5': x_catalan_number__mutmut_5, 
    'x_catalan_number__mutmut_6': x_catalan_number__mutmut_6, 
    'x_catalan_number__mutmut_7': x_catalan_number__mutmut_7, 
    'x_catalan_number__mutmut_8': x_catalan_number__mutmut_8, 
    'x_catalan_number__mutmut_9': x_catalan_number__mutmut_9, 
    'x_catalan_number__mutmut_10': x_catalan_number__mutmut_10, 
    'x_catalan_number__mutmut_11': x_catalan_number__mutmut_11, 
    'x_catalan_number__mutmut_12': x_catalan_number__mutmut_12, 
    'x_catalan_number__mutmut_13': x_catalan_number__mutmut_13, 
    'x_catalan_number__mutmut_14': x_catalan_number__mutmut_14
}

def catalan_number(*args, **kwargs):
    result = _mutmut_trampoline(x_catalan_number__mutmut_orig, x_catalan_number__mutmut_mutants, args, kwargs)
    return result 

catalan_number.__signature__ = _mutmut_signature(x_catalan_number__mutmut_orig)
x_catalan_number__mutmut_orig.__name__ = 'x_catalan_number'