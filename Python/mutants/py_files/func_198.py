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
def x_rearrange_bigger__mutmut_orig(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_1(n):
    nums = None
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_2(n):
    nums = list(None)
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_3(n):
    nums = list(str(None))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_4(n):
    nums = list(str(n))
    for i in range(None,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_5(n):
    nums = list(str(n))
    for i in range(len(nums)-2,None,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_6(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,None):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_7(n):
    nums = list(str(n))
    for i in range(-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_8(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_9(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_10(n):
    nums = list(str(n))
    for i in range(len(nums) + 2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_11(n):
    nums = list(str(n))
    for i in range(len(nums)-3,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_12(n):
    nums = list(str(n))
    for i in range(len(nums)-2,+1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_13(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-2,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_14(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,+1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_15(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-2):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_16(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] <= nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_17(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i - 1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_18(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+2]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_19(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = None
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_20(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = None
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_21(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(None)
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_22(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(None, z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_23(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], None))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_24(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_25(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], ))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_26(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: None, z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_27(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x >= z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_28(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[1], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_29(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(None)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_30(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = None
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_31(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] - z
            return int("".join(nums))
    return False
def x_rearrange_bigger__mutmut_32(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int(None)
    return False
def x_rearrange_bigger__mutmut_33(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(None))
    return False
def x_rearrange_bigger__mutmut_34(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("XXXX".join(nums))
    return False
def x_rearrange_bigger__mutmut_35(n):
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return True

x_rearrange_bigger__mutmut_mutants : ClassVar[MutantDict] = {
'x_rearrange_bigger__mutmut_1': x_rearrange_bigger__mutmut_1, 
    'x_rearrange_bigger__mutmut_2': x_rearrange_bigger__mutmut_2, 
    'x_rearrange_bigger__mutmut_3': x_rearrange_bigger__mutmut_3, 
    'x_rearrange_bigger__mutmut_4': x_rearrange_bigger__mutmut_4, 
    'x_rearrange_bigger__mutmut_5': x_rearrange_bigger__mutmut_5, 
    'x_rearrange_bigger__mutmut_6': x_rearrange_bigger__mutmut_6, 
    'x_rearrange_bigger__mutmut_7': x_rearrange_bigger__mutmut_7, 
    'x_rearrange_bigger__mutmut_8': x_rearrange_bigger__mutmut_8, 
    'x_rearrange_bigger__mutmut_9': x_rearrange_bigger__mutmut_9, 
    'x_rearrange_bigger__mutmut_10': x_rearrange_bigger__mutmut_10, 
    'x_rearrange_bigger__mutmut_11': x_rearrange_bigger__mutmut_11, 
    'x_rearrange_bigger__mutmut_12': x_rearrange_bigger__mutmut_12, 
    'x_rearrange_bigger__mutmut_13': x_rearrange_bigger__mutmut_13, 
    'x_rearrange_bigger__mutmut_14': x_rearrange_bigger__mutmut_14, 
    'x_rearrange_bigger__mutmut_15': x_rearrange_bigger__mutmut_15, 
    'x_rearrange_bigger__mutmut_16': x_rearrange_bigger__mutmut_16, 
    'x_rearrange_bigger__mutmut_17': x_rearrange_bigger__mutmut_17, 
    'x_rearrange_bigger__mutmut_18': x_rearrange_bigger__mutmut_18, 
    'x_rearrange_bigger__mutmut_19': x_rearrange_bigger__mutmut_19, 
    'x_rearrange_bigger__mutmut_20': x_rearrange_bigger__mutmut_20, 
    'x_rearrange_bigger__mutmut_21': x_rearrange_bigger__mutmut_21, 
    'x_rearrange_bigger__mutmut_22': x_rearrange_bigger__mutmut_22, 
    'x_rearrange_bigger__mutmut_23': x_rearrange_bigger__mutmut_23, 
    'x_rearrange_bigger__mutmut_24': x_rearrange_bigger__mutmut_24, 
    'x_rearrange_bigger__mutmut_25': x_rearrange_bigger__mutmut_25, 
    'x_rearrange_bigger__mutmut_26': x_rearrange_bigger__mutmut_26, 
    'x_rearrange_bigger__mutmut_27': x_rearrange_bigger__mutmut_27, 
    'x_rearrange_bigger__mutmut_28': x_rearrange_bigger__mutmut_28, 
    'x_rearrange_bigger__mutmut_29': x_rearrange_bigger__mutmut_29, 
    'x_rearrange_bigger__mutmut_30': x_rearrange_bigger__mutmut_30, 
    'x_rearrange_bigger__mutmut_31': x_rearrange_bigger__mutmut_31, 
    'x_rearrange_bigger__mutmut_32': x_rearrange_bigger__mutmut_32, 
    'x_rearrange_bigger__mutmut_33': x_rearrange_bigger__mutmut_33, 
    'x_rearrange_bigger__mutmut_34': x_rearrange_bigger__mutmut_34, 
    'x_rearrange_bigger__mutmut_35': x_rearrange_bigger__mutmut_35
}

def rearrange_bigger(*args, **kwargs):
    result = _mutmut_trampoline(x_rearrange_bigger__mutmut_orig, x_rearrange_bigger__mutmut_mutants, args, kwargs)
    return result 

rearrange_bigger.__signature__ = _mutmut_signature(x_rearrange_bigger__mutmut_orig)
x_rearrange_bigger__mutmut_orig.__name__ = 'x_rearrange_bigger'