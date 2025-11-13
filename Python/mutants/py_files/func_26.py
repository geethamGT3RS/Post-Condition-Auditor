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
def x_bell_number__mutmut_orig(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_1(n):   
    bell = None 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_2(n):   
    bell = [[1 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_3(n):   
    bell = [[0 for i in range(None)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_4(n):   
    bell = [[0 for i in range(n - 1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_5(n):   
    bell = [[0 for i in range(n+2)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_6(n):   
    bell = [[0 for i in range(n+1)] for j in range(None)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_7(n):   
    bell = [[0 for i in range(n+1)] for j in range(n - 1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_8(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+2)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_9(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = None
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_10(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[1][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_11(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][1] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_12(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 2
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_13(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(None, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_14(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, None): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_15(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_16(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, ): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_17(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(2, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_18(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n - 1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_19(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+2): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_20(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = None  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_21(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][1] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_22(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i + 1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_23(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-2][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_24(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i + 1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_25(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-2]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_26(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(None, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_27(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, None): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_28(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_29(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, ): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_30(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(2, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_31(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i - 1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_32(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+2): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_33(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = None   
    return bell[n][0] 
def x_bell_number__mutmut_34(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] - bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_35(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i + 1][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_36(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-2][j-1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_37(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j + 1] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_38(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-2] + bell[i][j-1]   
    return bell[n][0] 
def x_bell_number__mutmut_39(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j + 1]   
    return bell[n][0] 
def x_bell_number__mutmut_40(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-2]   
    return bell[n][0] 
def x_bell_number__mutmut_41(n):   
    bell = [[0 for i in range(n+1)] for j in range(n+1)] 
    bell[0][0] = 1
    for i in range(1, n+1): 
        bell[i][0] = bell[i-1][i-1]  
        for j in range(1, i+1): 
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]   
    return bell[n][1] 

x_bell_number__mutmut_mutants : ClassVar[MutantDict] = {
'x_bell_number__mutmut_1': x_bell_number__mutmut_1, 
    'x_bell_number__mutmut_2': x_bell_number__mutmut_2, 
    'x_bell_number__mutmut_3': x_bell_number__mutmut_3, 
    'x_bell_number__mutmut_4': x_bell_number__mutmut_4, 
    'x_bell_number__mutmut_5': x_bell_number__mutmut_5, 
    'x_bell_number__mutmut_6': x_bell_number__mutmut_6, 
    'x_bell_number__mutmut_7': x_bell_number__mutmut_7, 
    'x_bell_number__mutmut_8': x_bell_number__mutmut_8, 
    'x_bell_number__mutmut_9': x_bell_number__mutmut_9, 
    'x_bell_number__mutmut_10': x_bell_number__mutmut_10, 
    'x_bell_number__mutmut_11': x_bell_number__mutmut_11, 
    'x_bell_number__mutmut_12': x_bell_number__mutmut_12, 
    'x_bell_number__mutmut_13': x_bell_number__mutmut_13, 
    'x_bell_number__mutmut_14': x_bell_number__mutmut_14, 
    'x_bell_number__mutmut_15': x_bell_number__mutmut_15, 
    'x_bell_number__mutmut_16': x_bell_number__mutmut_16, 
    'x_bell_number__mutmut_17': x_bell_number__mutmut_17, 
    'x_bell_number__mutmut_18': x_bell_number__mutmut_18, 
    'x_bell_number__mutmut_19': x_bell_number__mutmut_19, 
    'x_bell_number__mutmut_20': x_bell_number__mutmut_20, 
    'x_bell_number__mutmut_21': x_bell_number__mutmut_21, 
    'x_bell_number__mutmut_22': x_bell_number__mutmut_22, 
    'x_bell_number__mutmut_23': x_bell_number__mutmut_23, 
    'x_bell_number__mutmut_24': x_bell_number__mutmut_24, 
    'x_bell_number__mutmut_25': x_bell_number__mutmut_25, 
    'x_bell_number__mutmut_26': x_bell_number__mutmut_26, 
    'x_bell_number__mutmut_27': x_bell_number__mutmut_27, 
    'x_bell_number__mutmut_28': x_bell_number__mutmut_28, 
    'x_bell_number__mutmut_29': x_bell_number__mutmut_29, 
    'x_bell_number__mutmut_30': x_bell_number__mutmut_30, 
    'x_bell_number__mutmut_31': x_bell_number__mutmut_31, 
    'x_bell_number__mutmut_32': x_bell_number__mutmut_32, 
    'x_bell_number__mutmut_33': x_bell_number__mutmut_33, 
    'x_bell_number__mutmut_34': x_bell_number__mutmut_34, 
    'x_bell_number__mutmut_35': x_bell_number__mutmut_35, 
    'x_bell_number__mutmut_36': x_bell_number__mutmut_36, 
    'x_bell_number__mutmut_37': x_bell_number__mutmut_37, 
    'x_bell_number__mutmut_38': x_bell_number__mutmut_38, 
    'x_bell_number__mutmut_39': x_bell_number__mutmut_39, 
    'x_bell_number__mutmut_40': x_bell_number__mutmut_40, 
    'x_bell_number__mutmut_41': x_bell_number__mutmut_41
}

def bell_number(*args, **kwargs):
    result = _mutmut_trampoline(x_bell_number__mutmut_orig, x_bell_number__mutmut_mutants, args, kwargs)
    return result 

bell_number.__signature__ = _mutmut_signature(x_bell_number__mutmut_orig)
x_bell_number__mutmut_orig.__name__ = 'x_bell_number'