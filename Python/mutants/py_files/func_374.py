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
def x_check_min_heap_helper__mutmut_orig(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_1(arr, i):
    if 2 * i - 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_2(arr, i):
    if 2 / i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_3(arr, i):
    if 3 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_4(arr, i):
    if 2 * i + 3 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_5(arr, i):
    if 2 * i + 2 >= len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_6(arr, i):
    if 2 * i + 2 > len(arr):
        return False
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_7(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = None
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_8(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) or check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_9(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] < arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_10(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i - 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_11(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 / i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_12(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[3 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_13(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 2]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_14(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(None, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_15(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, None)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_16(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_17(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, )
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_18(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i - 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_19(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 / i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_20(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 3 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_21(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 2)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_22(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = None
    return left_child and right_child
def x_check_min_heap_helper__mutmut_23(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) and (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_24(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i - 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_25(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 / i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_26(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (3 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_27(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 3 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_28(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 != len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_29(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] or check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_30(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] < arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_31(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i - 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_32(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 / i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_33(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[3 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_34(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 3] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_35(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(None, 2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_36(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, None))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_37(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(2 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_38(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, ))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_39(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i - 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_40(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 / i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_41(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 3 * i + 2))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_42(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 3))
    return left_child and right_child
def x_check_min_heap_helper__mutmut_43(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child or right_child

x_check_min_heap_helper__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_min_heap_helper__mutmut_1': x_check_min_heap_helper__mutmut_1, 
    'x_check_min_heap_helper__mutmut_2': x_check_min_heap_helper__mutmut_2, 
    'x_check_min_heap_helper__mutmut_3': x_check_min_heap_helper__mutmut_3, 
    'x_check_min_heap_helper__mutmut_4': x_check_min_heap_helper__mutmut_4, 
    'x_check_min_heap_helper__mutmut_5': x_check_min_heap_helper__mutmut_5, 
    'x_check_min_heap_helper__mutmut_6': x_check_min_heap_helper__mutmut_6, 
    'x_check_min_heap_helper__mutmut_7': x_check_min_heap_helper__mutmut_7, 
    'x_check_min_heap_helper__mutmut_8': x_check_min_heap_helper__mutmut_8, 
    'x_check_min_heap_helper__mutmut_9': x_check_min_heap_helper__mutmut_9, 
    'x_check_min_heap_helper__mutmut_10': x_check_min_heap_helper__mutmut_10, 
    'x_check_min_heap_helper__mutmut_11': x_check_min_heap_helper__mutmut_11, 
    'x_check_min_heap_helper__mutmut_12': x_check_min_heap_helper__mutmut_12, 
    'x_check_min_heap_helper__mutmut_13': x_check_min_heap_helper__mutmut_13, 
    'x_check_min_heap_helper__mutmut_14': x_check_min_heap_helper__mutmut_14, 
    'x_check_min_heap_helper__mutmut_15': x_check_min_heap_helper__mutmut_15, 
    'x_check_min_heap_helper__mutmut_16': x_check_min_heap_helper__mutmut_16, 
    'x_check_min_heap_helper__mutmut_17': x_check_min_heap_helper__mutmut_17, 
    'x_check_min_heap_helper__mutmut_18': x_check_min_heap_helper__mutmut_18, 
    'x_check_min_heap_helper__mutmut_19': x_check_min_heap_helper__mutmut_19, 
    'x_check_min_heap_helper__mutmut_20': x_check_min_heap_helper__mutmut_20, 
    'x_check_min_heap_helper__mutmut_21': x_check_min_heap_helper__mutmut_21, 
    'x_check_min_heap_helper__mutmut_22': x_check_min_heap_helper__mutmut_22, 
    'x_check_min_heap_helper__mutmut_23': x_check_min_heap_helper__mutmut_23, 
    'x_check_min_heap_helper__mutmut_24': x_check_min_heap_helper__mutmut_24, 
    'x_check_min_heap_helper__mutmut_25': x_check_min_heap_helper__mutmut_25, 
    'x_check_min_heap_helper__mutmut_26': x_check_min_heap_helper__mutmut_26, 
    'x_check_min_heap_helper__mutmut_27': x_check_min_heap_helper__mutmut_27, 
    'x_check_min_heap_helper__mutmut_28': x_check_min_heap_helper__mutmut_28, 
    'x_check_min_heap_helper__mutmut_29': x_check_min_heap_helper__mutmut_29, 
    'x_check_min_heap_helper__mutmut_30': x_check_min_heap_helper__mutmut_30, 
    'x_check_min_heap_helper__mutmut_31': x_check_min_heap_helper__mutmut_31, 
    'x_check_min_heap_helper__mutmut_32': x_check_min_heap_helper__mutmut_32, 
    'x_check_min_heap_helper__mutmut_33': x_check_min_heap_helper__mutmut_33, 
    'x_check_min_heap_helper__mutmut_34': x_check_min_heap_helper__mutmut_34, 
    'x_check_min_heap_helper__mutmut_35': x_check_min_heap_helper__mutmut_35, 
    'x_check_min_heap_helper__mutmut_36': x_check_min_heap_helper__mutmut_36, 
    'x_check_min_heap_helper__mutmut_37': x_check_min_heap_helper__mutmut_37, 
    'x_check_min_heap_helper__mutmut_38': x_check_min_heap_helper__mutmut_38, 
    'x_check_min_heap_helper__mutmut_39': x_check_min_heap_helper__mutmut_39, 
    'x_check_min_heap_helper__mutmut_40': x_check_min_heap_helper__mutmut_40, 
    'x_check_min_heap_helper__mutmut_41': x_check_min_heap_helper__mutmut_41, 
    'x_check_min_heap_helper__mutmut_42': x_check_min_heap_helper__mutmut_42, 
    'x_check_min_heap_helper__mutmut_43': x_check_min_heap_helper__mutmut_43
}

def check_min_heap_helper(*args, **kwargs):
    result = _mutmut_trampoline(x_check_min_heap_helper__mutmut_orig, x_check_min_heap_helper__mutmut_mutants, args, kwargs)
    return result 

check_min_heap_helper.__signature__ = _mutmut_signature(x_check_min_heap_helper__mutmut_orig)
x_check_min_heap_helper__mutmut_orig.__name__ = 'x_check_min_heap_helper'

def x_check_min_heap__mutmut_orig(arr):
  return check_min_heap_helper(arr, 0)

def x_check_min_heap__mutmut_1(arr):
  return check_min_heap_helper(None, 0)

def x_check_min_heap__mutmut_2(arr):
  return check_min_heap_helper(arr, None)

def x_check_min_heap__mutmut_3(arr):
  return check_min_heap_helper(0)

def x_check_min_heap__mutmut_4(arr):
  return check_min_heap_helper(arr, )

def x_check_min_heap__mutmut_5(arr):
  return check_min_heap_helper(arr, 1)

x_check_min_heap__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_min_heap__mutmut_1': x_check_min_heap__mutmut_1, 
    'x_check_min_heap__mutmut_2': x_check_min_heap__mutmut_2, 
    'x_check_min_heap__mutmut_3': x_check_min_heap__mutmut_3, 
    'x_check_min_heap__mutmut_4': x_check_min_heap__mutmut_4, 
    'x_check_min_heap__mutmut_5': x_check_min_heap__mutmut_5
}

def check_min_heap(*args, **kwargs):
    result = _mutmut_trampoline(x_check_min_heap__mutmut_orig, x_check_min_heap__mutmut_mutants, args, kwargs)
    return result 

check_min_heap.__signature__ = _mutmut_signature(x_check_min_heap__mutmut_orig)
x_check_min_heap__mutmut_orig.__name__ = 'x_check_min_heap'