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
def x_tuple_to_int__mutmut_orig(nums):
    result = int(''.join(map(str,nums)))
    return result
def x_tuple_to_int__mutmut_1(nums):
    result = None
    return result
def x_tuple_to_int__mutmut_2(nums):
    result = int(None)
    return result
def x_tuple_to_int__mutmut_3(nums):
    result = int(''.join(None))
    return result
def x_tuple_to_int__mutmut_4(nums):
    result = int('XXXX'.join(map(str,nums)))
    return result
def x_tuple_to_int__mutmut_5(nums):
    result = int(''.join(map(None,nums)))
    return result
def x_tuple_to_int__mutmut_6(nums):
    result = int(''.join(map(str,None)))
    return result
def x_tuple_to_int__mutmut_7(nums):
    result = int(''.join(map(nums)))
    return result
def x_tuple_to_int__mutmut_8(nums):
    result = int(''.join(map(str,)))
    return result

x_tuple_to_int__mutmut_mutants : ClassVar[MutantDict] = {
'x_tuple_to_int__mutmut_1': x_tuple_to_int__mutmut_1, 
    'x_tuple_to_int__mutmut_2': x_tuple_to_int__mutmut_2, 
    'x_tuple_to_int__mutmut_3': x_tuple_to_int__mutmut_3, 
    'x_tuple_to_int__mutmut_4': x_tuple_to_int__mutmut_4, 
    'x_tuple_to_int__mutmut_5': x_tuple_to_int__mutmut_5, 
    'x_tuple_to_int__mutmut_6': x_tuple_to_int__mutmut_6, 
    'x_tuple_to_int__mutmut_7': x_tuple_to_int__mutmut_7, 
    'x_tuple_to_int__mutmut_8': x_tuple_to_int__mutmut_8
}

def tuple_to_int(*args, **kwargs):
    result = _mutmut_trampoline(x_tuple_to_int__mutmut_orig, x_tuple_to_int__mutmut_mutants, args, kwargs)
    return result 

tuple_to_int.__signature__ = _mutmut_signature(x_tuple_to_int__mutmut_orig)
x_tuple_to_int__mutmut_orig.__name__ = 'x_tuple_to_int'