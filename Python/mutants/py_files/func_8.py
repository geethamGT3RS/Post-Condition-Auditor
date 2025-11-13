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
def x_remove_Occ__mutmut_orig(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_1(s,ch): 
    for i in range(None): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_2(s,ch): 
    for i in range(len(s)): 
        if (s[i] != ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_3(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = None 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_4(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] - s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_5(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[1 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_6(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i - 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_7(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 2:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_8(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            return
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_9(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(None,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_10(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,None,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_11(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,None):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_12(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_13(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_14(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_15(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) + 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_16(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 2,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_17(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,+1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_18(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-2,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_19(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,+1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_20(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-2):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_21(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] != ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_22(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = None 
            break
    return s 
def x_remove_Occ__mutmut_23(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] - s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_24(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[1 : i] + s[i + 1:] 
            break
    return s 
def x_remove_Occ__mutmut_25(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i - 1:] 
            break
    return s 
def x_remove_Occ__mutmut_26(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 2:] 
            break
    return s 
def x_remove_Occ__mutmut_27(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            return
    return s 

x_remove_Occ__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_Occ__mutmut_1': x_remove_Occ__mutmut_1, 
    'x_remove_Occ__mutmut_2': x_remove_Occ__mutmut_2, 
    'x_remove_Occ__mutmut_3': x_remove_Occ__mutmut_3, 
    'x_remove_Occ__mutmut_4': x_remove_Occ__mutmut_4, 
    'x_remove_Occ__mutmut_5': x_remove_Occ__mutmut_5, 
    'x_remove_Occ__mutmut_6': x_remove_Occ__mutmut_6, 
    'x_remove_Occ__mutmut_7': x_remove_Occ__mutmut_7, 
    'x_remove_Occ__mutmut_8': x_remove_Occ__mutmut_8, 
    'x_remove_Occ__mutmut_9': x_remove_Occ__mutmut_9, 
    'x_remove_Occ__mutmut_10': x_remove_Occ__mutmut_10, 
    'x_remove_Occ__mutmut_11': x_remove_Occ__mutmut_11, 
    'x_remove_Occ__mutmut_12': x_remove_Occ__mutmut_12, 
    'x_remove_Occ__mutmut_13': x_remove_Occ__mutmut_13, 
    'x_remove_Occ__mutmut_14': x_remove_Occ__mutmut_14, 
    'x_remove_Occ__mutmut_15': x_remove_Occ__mutmut_15, 
    'x_remove_Occ__mutmut_16': x_remove_Occ__mutmut_16, 
    'x_remove_Occ__mutmut_17': x_remove_Occ__mutmut_17, 
    'x_remove_Occ__mutmut_18': x_remove_Occ__mutmut_18, 
    'x_remove_Occ__mutmut_19': x_remove_Occ__mutmut_19, 
    'x_remove_Occ__mutmut_20': x_remove_Occ__mutmut_20, 
    'x_remove_Occ__mutmut_21': x_remove_Occ__mutmut_21, 
    'x_remove_Occ__mutmut_22': x_remove_Occ__mutmut_22, 
    'x_remove_Occ__mutmut_23': x_remove_Occ__mutmut_23, 
    'x_remove_Occ__mutmut_24': x_remove_Occ__mutmut_24, 
    'x_remove_Occ__mutmut_25': x_remove_Occ__mutmut_25, 
    'x_remove_Occ__mutmut_26': x_remove_Occ__mutmut_26, 
    'x_remove_Occ__mutmut_27': x_remove_Occ__mutmut_27
}

def remove_Occ(*args, **kwargs):
    result = _mutmut_trampoline(x_remove_Occ__mutmut_orig, x_remove_Occ__mutmut_mutants, args, kwargs)
    return result 

remove_Occ.__signature__ = _mutmut_signature(x_remove_Occ__mutmut_orig)
x_remove_Occ__mutmut_orig.__name__ = 'x_remove_Occ'