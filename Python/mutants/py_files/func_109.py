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
def x_all_Bits_Set_In_The_Given_Range__mutmut_orig(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_1(n,l,r):  
    num = None 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_2(n,l,r):  
    num = (((1 << r) - 1) & ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_3(n,l,r):  
    num = (((1 << r) + 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_4(n,l,r):  
    num = (((1 >> r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_5(n,l,r):  
    num = (((2 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_6(n,l,r):  
    num = (((1 << r) - 2) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_7(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) + 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_8(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 >> (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_9(n,l,r):  
    num = (((1 << r) - 1) ^ ((2 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_10(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l + 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_11(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 2)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_12(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 2)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_13(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = None
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_14(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n | num
    if (new_num == 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_15(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num != 0): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_16(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 1): 
        return True
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_17(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return False
    return False
def x_all_Bits_Set_In_The_Given_Range__mutmut_18(n,l,r):  
    num = (((1 << r) - 1) ^ ((1 << (l - 1)) - 1)) 
    new_num = n & num
    if (new_num == 0): 
        return True
    return True

x_all_Bits_Set_In_The_Given_Range__mutmut_mutants : ClassVar[MutantDict] = {
'x_all_Bits_Set_In_The_Given_Range__mutmut_1': x_all_Bits_Set_In_The_Given_Range__mutmut_1, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_2': x_all_Bits_Set_In_The_Given_Range__mutmut_2, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_3': x_all_Bits_Set_In_The_Given_Range__mutmut_3, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_4': x_all_Bits_Set_In_The_Given_Range__mutmut_4, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_5': x_all_Bits_Set_In_The_Given_Range__mutmut_5, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_6': x_all_Bits_Set_In_The_Given_Range__mutmut_6, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_7': x_all_Bits_Set_In_The_Given_Range__mutmut_7, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_8': x_all_Bits_Set_In_The_Given_Range__mutmut_8, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_9': x_all_Bits_Set_In_The_Given_Range__mutmut_9, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_10': x_all_Bits_Set_In_The_Given_Range__mutmut_10, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_11': x_all_Bits_Set_In_The_Given_Range__mutmut_11, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_12': x_all_Bits_Set_In_The_Given_Range__mutmut_12, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_13': x_all_Bits_Set_In_The_Given_Range__mutmut_13, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_14': x_all_Bits_Set_In_The_Given_Range__mutmut_14, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_15': x_all_Bits_Set_In_The_Given_Range__mutmut_15, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_16': x_all_Bits_Set_In_The_Given_Range__mutmut_16, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_17': x_all_Bits_Set_In_The_Given_Range__mutmut_17, 
    'x_all_Bits_Set_In_The_Given_Range__mutmut_18': x_all_Bits_Set_In_The_Given_Range__mutmut_18
}

def all_Bits_Set_In_The_Given_Range(*args, **kwargs):
    result = _mutmut_trampoline(x_all_Bits_Set_In_The_Given_Range__mutmut_orig, x_all_Bits_Set_In_The_Given_Range__mutmut_mutants, args, kwargs)
    return result 

all_Bits_Set_In_The_Given_Range.__signature__ = _mutmut_signature(x_all_Bits_Set_In_The_Given_Range__mutmut_orig)
x_all_Bits_Set_In_The_Given_Range__mutmut_orig.__name__ = 'x_all_Bits_Set_In_The_Given_Range'