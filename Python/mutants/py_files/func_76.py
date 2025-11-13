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
def x_multiply_int__mutmut_orig(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_1(x, y):
    if y <= 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_2(x, y):
    if y < 1:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_3(x, y):
    if y < 0:
        return +multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_4(x, y):
    if y < 0:
        return -multiply_int(None, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_5(x, y):
    if y < 0:
        return -multiply_int(x, None)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_6(x, y):
    if y < 0:
        return -multiply_int(-y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_7(x, y):
    if y < 0:
        return -multiply_int(x, )
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_8(x, y):
    if y < 0:
        return -multiply_int(x, +y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_9(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y != 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_10(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 1:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_11(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_12(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y != 1:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_13(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 2:
        return x
    else:
        return x + multiply_int(x, y - 1)
def x_multiply_int__mutmut_14(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x - multiply_int(x, y - 1)
def x_multiply_int__mutmut_15(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(None, y - 1)
def x_multiply_int__mutmut_16(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, None)
def x_multiply_int__mutmut_17(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(y - 1)
def x_multiply_int__mutmut_18(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, )
def x_multiply_int__mutmut_19(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y + 1)
def x_multiply_int__mutmut_20(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 2)

x_multiply_int__mutmut_mutants : ClassVar[MutantDict] = {
'x_multiply_int__mutmut_1': x_multiply_int__mutmut_1, 
    'x_multiply_int__mutmut_2': x_multiply_int__mutmut_2, 
    'x_multiply_int__mutmut_3': x_multiply_int__mutmut_3, 
    'x_multiply_int__mutmut_4': x_multiply_int__mutmut_4, 
    'x_multiply_int__mutmut_5': x_multiply_int__mutmut_5, 
    'x_multiply_int__mutmut_6': x_multiply_int__mutmut_6, 
    'x_multiply_int__mutmut_7': x_multiply_int__mutmut_7, 
    'x_multiply_int__mutmut_8': x_multiply_int__mutmut_8, 
    'x_multiply_int__mutmut_9': x_multiply_int__mutmut_9, 
    'x_multiply_int__mutmut_10': x_multiply_int__mutmut_10, 
    'x_multiply_int__mutmut_11': x_multiply_int__mutmut_11, 
    'x_multiply_int__mutmut_12': x_multiply_int__mutmut_12, 
    'x_multiply_int__mutmut_13': x_multiply_int__mutmut_13, 
    'x_multiply_int__mutmut_14': x_multiply_int__mutmut_14, 
    'x_multiply_int__mutmut_15': x_multiply_int__mutmut_15, 
    'x_multiply_int__mutmut_16': x_multiply_int__mutmut_16, 
    'x_multiply_int__mutmut_17': x_multiply_int__mutmut_17, 
    'x_multiply_int__mutmut_18': x_multiply_int__mutmut_18, 
    'x_multiply_int__mutmut_19': x_multiply_int__mutmut_19, 
    'x_multiply_int__mutmut_20': x_multiply_int__mutmut_20
}

def multiply_int(*args, **kwargs):
    result = _mutmut_trampoline(x_multiply_int__mutmut_orig, x_multiply_int__mutmut_mutants, args, kwargs)
    return result 

multiply_int.__signature__ = _mutmut_signature(x_multiply_int__mutmut_orig)
x_multiply_int__mutmut_orig.__name__ = 'x_multiply_int'