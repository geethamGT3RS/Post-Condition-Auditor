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
def x_pancake_sort__mutmut_orig(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_1(nums):
    arr_len = None
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_2(nums):
    arr_len = len(nums)
    while arr_len >= 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_3(nums):
    arr_len = len(nums)
    while arr_len > 2:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_4(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = None
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_5(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(None)
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_6(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.rindex(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_7(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(None))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_8(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[1:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_9(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = None
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_10(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] - nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_11(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::+1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_12(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-2] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_13(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi - 1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_14(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+2:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_15(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = None
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_16(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] - nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_17(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len + 1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_18(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-2::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_19(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::+1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_20(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-2] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums
def x_pancake_sort__mutmut_21(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len = 1
    return nums
def x_pancake_sort__mutmut_22(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len += 1
    return nums
def x_pancake_sort__mutmut_23(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 2
    return nums

x_pancake_sort__mutmut_mutants : ClassVar[MutantDict] = {
'x_pancake_sort__mutmut_1': x_pancake_sort__mutmut_1, 
    'x_pancake_sort__mutmut_2': x_pancake_sort__mutmut_2, 
    'x_pancake_sort__mutmut_3': x_pancake_sort__mutmut_3, 
    'x_pancake_sort__mutmut_4': x_pancake_sort__mutmut_4, 
    'x_pancake_sort__mutmut_5': x_pancake_sort__mutmut_5, 
    'x_pancake_sort__mutmut_6': x_pancake_sort__mutmut_6, 
    'x_pancake_sort__mutmut_7': x_pancake_sort__mutmut_7, 
    'x_pancake_sort__mutmut_8': x_pancake_sort__mutmut_8, 
    'x_pancake_sort__mutmut_9': x_pancake_sort__mutmut_9, 
    'x_pancake_sort__mutmut_10': x_pancake_sort__mutmut_10, 
    'x_pancake_sort__mutmut_11': x_pancake_sort__mutmut_11, 
    'x_pancake_sort__mutmut_12': x_pancake_sort__mutmut_12, 
    'x_pancake_sort__mutmut_13': x_pancake_sort__mutmut_13, 
    'x_pancake_sort__mutmut_14': x_pancake_sort__mutmut_14, 
    'x_pancake_sort__mutmut_15': x_pancake_sort__mutmut_15, 
    'x_pancake_sort__mutmut_16': x_pancake_sort__mutmut_16, 
    'x_pancake_sort__mutmut_17': x_pancake_sort__mutmut_17, 
    'x_pancake_sort__mutmut_18': x_pancake_sort__mutmut_18, 
    'x_pancake_sort__mutmut_19': x_pancake_sort__mutmut_19, 
    'x_pancake_sort__mutmut_20': x_pancake_sort__mutmut_20, 
    'x_pancake_sort__mutmut_21': x_pancake_sort__mutmut_21, 
    'x_pancake_sort__mutmut_22': x_pancake_sort__mutmut_22, 
    'x_pancake_sort__mutmut_23': x_pancake_sort__mutmut_23
}

def pancake_sort(*args, **kwargs):
    result = _mutmut_trampoline(x_pancake_sort__mutmut_orig, x_pancake_sort__mutmut_mutants, args, kwargs)
    return result 

pancake_sort.__signature__ = _mutmut_signature(x_pancake_sort__mutmut_orig)
x_pancake_sort__mutmut_orig.__name__ = 'x_pancake_sort'