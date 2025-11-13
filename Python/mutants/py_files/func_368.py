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
def x_divisible_by_digits__mutmut_orig(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_1(startnum, endnum):
    return [n for n in range(None, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_2(startnum, endnum):
    return [n for n in range(startnum, None) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_3(startnum, endnum):
    return [n for n in range(endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_4(startnum, endnum):
    return [n for n in range(startnum, ) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_5(startnum, endnum):
    return [n for n in range(startnum, endnum - 1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_6(startnum, endnum):
    return [n for n in range(startnum, endnum+2) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_7(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_8(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(None)]
def x_divisible_by_digits__mutmut_9(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(None, str(n)))]
def x_divisible_by_digits__mutmut_10(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, None))]
def x_divisible_by_digits__mutmut_11(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(str(n)))]
def x_divisible_by_digits__mutmut_12(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, ))]
def x_divisible_by_digits__mutmut_13(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: None, str(n)))]
def x_divisible_by_digits__mutmut_14(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 and n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_15(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(None) == 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_16(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) != 0 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_17(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 1 or n%int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_18(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n / int(x) != 0, str(n)))]
def x_divisible_by_digits__mutmut_19(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(None) != 0, str(n)))]
def x_divisible_by_digits__mutmut_20(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) == 0, str(n)))]
def x_divisible_by_digits__mutmut_21(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 1, str(n)))]
def x_divisible_by_digits__mutmut_22(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(None)))]

x_divisible_by_digits__mutmut_mutants : ClassVar[MutantDict] = {
'x_divisible_by_digits__mutmut_1': x_divisible_by_digits__mutmut_1, 
    'x_divisible_by_digits__mutmut_2': x_divisible_by_digits__mutmut_2, 
    'x_divisible_by_digits__mutmut_3': x_divisible_by_digits__mutmut_3, 
    'x_divisible_by_digits__mutmut_4': x_divisible_by_digits__mutmut_4, 
    'x_divisible_by_digits__mutmut_5': x_divisible_by_digits__mutmut_5, 
    'x_divisible_by_digits__mutmut_6': x_divisible_by_digits__mutmut_6, 
    'x_divisible_by_digits__mutmut_7': x_divisible_by_digits__mutmut_7, 
    'x_divisible_by_digits__mutmut_8': x_divisible_by_digits__mutmut_8, 
    'x_divisible_by_digits__mutmut_9': x_divisible_by_digits__mutmut_9, 
    'x_divisible_by_digits__mutmut_10': x_divisible_by_digits__mutmut_10, 
    'x_divisible_by_digits__mutmut_11': x_divisible_by_digits__mutmut_11, 
    'x_divisible_by_digits__mutmut_12': x_divisible_by_digits__mutmut_12, 
    'x_divisible_by_digits__mutmut_13': x_divisible_by_digits__mutmut_13, 
    'x_divisible_by_digits__mutmut_14': x_divisible_by_digits__mutmut_14, 
    'x_divisible_by_digits__mutmut_15': x_divisible_by_digits__mutmut_15, 
    'x_divisible_by_digits__mutmut_16': x_divisible_by_digits__mutmut_16, 
    'x_divisible_by_digits__mutmut_17': x_divisible_by_digits__mutmut_17, 
    'x_divisible_by_digits__mutmut_18': x_divisible_by_digits__mutmut_18, 
    'x_divisible_by_digits__mutmut_19': x_divisible_by_digits__mutmut_19, 
    'x_divisible_by_digits__mutmut_20': x_divisible_by_digits__mutmut_20, 
    'x_divisible_by_digits__mutmut_21': x_divisible_by_digits__mutmut_21, 
    'x_divisible_by_digits__mutmut_22': x_divisible_by_digits__mutmut_22
}

def divisible_by_digits(*args, **kwargs):
    result = _mutmut_trampoline(x_divisible_by_digits__mutmut_orig, x_divisible_by_digits__mutmut_mutants, args, kwargs)
    return result 

divisible_by_digits.__signature__ = _mutmut_signature(x_divisible_by_digits__mutmut_orig)
x_divisible_by_digits__mutmut_orig.__name__ = 'x_divisible_by_digits'