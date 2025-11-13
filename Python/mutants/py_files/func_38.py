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
def x_get_Char__mutmut_orig(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_1(strr):  
    summ = None
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_2(strr):  
    summ = 1
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_3(strr):  
    summ = 0
    for i in range(None): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_4(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ = (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_5(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ -= (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_6(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') - 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_7(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) + ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_8(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(None) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_9(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord(None) + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_10(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('XXaXX') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_11(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('A') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_12(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 2)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_13(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ / 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_14(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 27 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_15(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 != 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_16(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 1): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_17(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord(None) 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_18(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('XXzXX') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_19(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('Z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_20(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = None
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_21(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ / 26
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_22(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 27
        return chr(ord('a') + summ - 1)
def x_get_Char__mutmut_23(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(None)
def x_get_Char__mutmut_24(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ + 1)
def x_get_Char__mutmut_25(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') - summ - 1)
def x_get_Char__mutmut_26(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord(None) + summ - 1)
def x_get_Char__mutmut_27(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('XXaXX') + summ - 1)
def x_get_Char__mutmut_28(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('A') + summ - 1)
def x_get_Char__mutmut_29(strr):  
    summ = 0
    for i in range(len(strr)): 
        summ += (ord(strr[i]) - ord('a') + 1)  
    if (summ % 26 == 0): 
        return ord('z') 
    else: 
        summ = summ % 26
        return chr(ord('a') + summ - 2)

x_get_Char__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_Char__mutmut_1': x_get_Char__mutmut_1, 
    'x_get_Char__mutmut_2': x_get_Char__mutmut_2, 
    'x_get_Char__mutmut_3': x_get_Char__mutmut_3, 
    'x_get_Char__mutmut_4': x_get_Char__mutmut_4, 
    'x_get_Char__mutmut_5': x_get_Char__mutmut_5, 
    'x_get_Char__mutmut_6': x_get_Char__mutmut_6, 
    'x_get_Char__mutmut_7': x_get_Char__mutmut_7, 
    'x_get_Char__mutmut_8': x_get_Char__mutmut_8, 
    'x_get_Char__mutmut_9': x_get_Char__mutmut_9, 
    'x_get_Char__mutmut_10': x_get_Char__mutmut_10, 
    'x_get_Char__mutmut_11': x_get_Char__mutmut_11, 
    'x_get_Char__mutmut_12': x_get_Char__mutmut_12, 
    'x_get_Char__mutmut_13': x_get_Char__mutmut_13, 
    'x_get_Char__mutmut_14': x_get_Char__mutmut_14, 
    'x_get_Char__mutmut_15': x_get_Char__mutmut_15, 
    'x_get_Char__mutmut_16': x_get_Char__mutmut_16, 
    'x_get_Char__mutmut_17': x_get_Char__mutmut_17, 
    'x_get_Char__mutmut_18': x_get_Char__mutmut_18, 
    'x_get_Char__mutmut_19': x_get_Char__mutmut_19, 
    'x_get_Char__mutmut_20': x_get_Char__mutmut_20, 
    'x_get_Char__mutmut_21': x_get_Char__mutmut_21, 
    'x_get_Char__mutmut_22': x_get_Char__mutmut_22, 
    'x_get_Char__mutmut_23': x_get_Char__mutmut_23, 
    'x_get_Char__mutmut_24': x_get_Char__mutmut_24, 
    'x_get_Char__mutmut_25': x_get_Char__mutmut_25, 
    'x_get_Char__mutmut_26': x_get_Char__mutmut_26, 
    'x_get_Char__mutmut_27': x_get_Char__mutmut_27, 
    'x_get_Char__mutmut_28': x_get_Char__mutmut_28, 
    'x_get_Char__mutmut_29': x_get_Char__mutmut_29
}

def get_Char(*args, **kwargs):
    result = _mutmut_trampoline(x_get_Char__mutmut_orig, x_get_Char__mutmut_mutants, args, kwargs)
    return result 

get_Char.__signature__ = _mutmut_signature(x_get_Char__mutmut_orig)
x_get_Char__mutmut_orig.__name__ = 'x_get_Char'