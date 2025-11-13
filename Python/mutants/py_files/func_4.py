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
def x_is_Power_Of_Two__mutmut_orig (x): 
    return x and (not(x & (x - 1))) 
def x_is_Power_Of_Two__mutmut_1 (x): 
    return x or (not(x & (x - 1))) 
def x_is_Power_Of_Two__mutmut_2 (x): 
    return x and (x & (x - 1)) 
def x_is_Power_Of_Two__mutmut_3 (x): 
    return x and (not(x | (x - 1))) 
def x_is_Power_Of_Two__mutmut_4 (x): 
    return x and (not(x & (x + 1))) 
def x_is_Power_Of_Two__mutmut_5 (x): 
    return x and (not(x & (x - 2))) 

x_is_Power_Of_Two__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_Power_Of_Two__mutmut_1': x_is_Power_Of_Two__mutmut_1, 
    'x_is_Power_Of_Two__mutmut_2': x_is_Power_Of_Two__mutmut_2, 
    'x_is_Power_Of_Two__mutmut_3': x_is_Power_Of_Two__mutmut_3, 
    'x_is_Power_Of_Two__mutmut_4': x_is_Power_Of_Two__mutmut_4, 
    'x_is_Power_Of_Two__mutmut_5': x_is_Power_Of_Two__mutmut_5
}

def is_Power_Of_Two(*args, **kwargs):
    result = _mutmut_trampoline(x_is_Power_Of_Two__mutmut_orig, x_is_Power_Of_Two__mutmut_mutants, args, kwargs)
    return result 

is_Power_Of_Two.__signature__ = _mutmut_signature(x_is_Power_Of_Two__mutmut_orig)
x_is_Power_Of_Two__mutmut_orig.__name__ = 'x_is_Power_Of_Two'
def x_differ_At_One_Bit_Pos__mutmut_orig(a,b): 
    return is_Power_Of_Two(a ^ b)
def x_differ_At_One_Bit_Pos__mutmut_1(a,b): 
    return is_Power_Of_Two(None)
def x_differ_At_One_Bit_Pos__mutmut_2(a,b): 
    return is_Power_Of_Two(a & b)

x_differ_At_One_Bit_Pos__mutmut_mutants : ClassVar[MutantDict] = {
'x_differ_At_One_Bit_Pos__mutmut_1': x_differ_At_One_Bit_Pos__mutmut_1, 
    'x_differ_At_One_Bit_Pos__mutmut_2': x_differ_At_One_Bit_Pos__mutmut_2
}

def differ_At_One_Bit_Pos(*args, **kwargs):
    result = _mutmut_trampoline(x_differ_At_One_Bit_Pos__mutmut_orig, x_differ_At_One_Bit_Pos__mutmut_mutants, args, kwargs)
    return result 

differ_At_One_Bit_Pos.__signature__ = _mutmut_signature(x_differ_At_One_Bit_Pos__mutmut_orig)
x_differ_At_One_Bit_Pos__mutmut_orig.__name__ = 'x_differ_At_One_Bit_Pos'