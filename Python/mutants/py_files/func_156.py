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
def x_validate__mutmut_orig(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_1(n): 
    for i in range(None): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_2(n): 
    for i in range(11): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_3(n): 
    for i in range(10): 
        temp = None;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_4(n): 
    for i in range(10): 
        temp = n;  
        count = None; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_5(n): 
    for i in range(10): 
        temp = n;  
        count = 1; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_6(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp / 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_7(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 11 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_8(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 != i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_9(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count = 1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_10(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count -= 1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_11(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=2;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_12(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count >= i): 
                return False
            temp //= 10; 
    return True
def x_validate__mutmut_13(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return True
            temp //= 10; 
    return True
def x_validate__mutmut_14(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp = 10; 
    return True
def x_validate__mutmut_15(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp /= 10; 
    return True
def x_validate__mutmut_16(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 11; 
    return True
def x_validate__mutmut_17(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return False

x_validate__mutmut_mutants : ClassVar[MutantDict] = {
'x_validate__mutmut_1': x_validate__mutmut_1, 
    'x_validate__mutmut_2': x_validate__mutmut_2, 
    'x_validate__mutmut_3': x_validate__mutmut_3, 
    'x_validate__mutmut_4': x_validate__mutmut_4, 
    'x_validate__mutmut_5': x_validate__mutmut_5, 
    'x_validate__mutmut_6': x_validate__mutmut_6, 
    'x_validate__mutmut_7': x_validate__mutmut_7, 
    'x_validate__mutmut_8': x_validate__mutmut_8, 
    'x_validate__mutmut_9': x_validate__mutmut_9, 
    'x_validate__mutmut_10': x_validate__mutmut_10, 
    'x_validate__mutmut_11': x_validate__mutmut_11, 
    'x_validate__mutmut_12': x_validate__mutmut_12, 
    'x_validate__mutmut_13': x_validate__mutmut_13, 
    'x_validate__mutmut_14': x_validate__mutmut_14, 
    'x_validate__mutmut_15': x_validate__mutmut_15, 
    'x_validate__mutmut_16': x_validate__mutmut_16, 
    'x_validate__mutmut_17': x_validate__mutmut_17
}

def validate(*args, **kwargs):
    result = _mutmut_trampoline(x_validate__mutmut_orig, x_validate__mutmut_mutants, args, kwargs)
    return result 

validate.__signature__ = _mutmut_signature(x_validate__mutmut_orig)
x_validate__mutmut_orig.__name__ = 'x_validate'