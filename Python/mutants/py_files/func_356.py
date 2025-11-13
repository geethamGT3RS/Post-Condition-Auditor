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
def x_find_first_occurrence__mutmut_orig(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_1(A, x):
    (left, right) = None
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_2(A, x):
    (left, right) = (1, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_3(A, x):
    (left, right) = (0, len(A) + 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_4(A, x):
    (left, right) = (0, len(A) - 2)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_5(A, x):
    (left, right) = (0, len(A) - 1)
    result = None
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_6(A, x):
    (left, right) = (0, len(A) - 1)
    result = +1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_7(A, x):
    (left, right) = (0, len(A) - 1)
    result = -2
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_8(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left < right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_9(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = None
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_10(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) / 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_11(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left - right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_12(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 3
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_13(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x != A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_14(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = None
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_15(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = None
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_16(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid + 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_17(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 2
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_18(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x <= A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_19(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = None
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_20(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid + 1
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_21(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 2
        else:
            left = mid + 1
    return result
def x_find_first_occurrence__mutmut_22(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = None
    return result
def x_find_first_occurrence__mutmut_23(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid - 1
    return result
def x_find_first_occurrence__mutmut_24(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 2
    return result

x_find_first_occurrence__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_first_occurrence__mutmut_1': x_find_first_occurrence__mutmut_1, 
    'x_find_first_occurrence__mutmut_2': x_find_first_occurrence__mutmut_2, 
    'x_find_first_occurrence__mutmut_3': x_find_first_occurrence__mutmut_3, 
    'x_find_first_occurrence__mutmut_4': x_find_first_occurrence__mutmut_4, 
    'x_find_first_occurrence__mutmut_5': x_find_first_occurrence__mutmut_5, 
    'x_find_first_occurrence__mutmut_6': x_find_first_occurrence__mutmut_6, 
    'x_find_first_occurrence__mutmut_7': x_find_first_occurrence__mutmut_7, 
    'x_find_first_occurrence__mutmut_8': x_find_first_occurrence__mutmut_8, 
    'x_find_first_occurrence__mutmut_9': x_find_first_occurrence__mutmut_9, 
    'x_find_first_occurrence__mutmut_10': x_find_first_occurrence__mutmut_10, 
    'x_find_first_occurrence__mutmut_11': x_find_first_occurrence__mutmut_11, 
    'x_find_first_occurrence__mutmut_12': x_find_first_occurrence__mutmut_12, 
    'x_find_first_occurrence__mutmut_13': x_find_first_occurrence__mutmut_13, 
    'x_find_first_occurrence__mutmut_14': x_find_first_occurrence__mutmut_14, 
    'x_find_first_occurrence__mutmut_15': x_find_first_occurrence__mutmut_15, 
    'x_find_first_occurrence__mutmut_16': x_find_first_occurrence__mutmut_16, 
    'x_find_first_occurrence__mutmut_17': x_find_first_occurrence__mutmut_17, 
    'x_find_first_occurrence__mutmut_18': x_find_first_occurrence__mutmut_18, 
    'x_find_first_occurrence__mutmut_19': x_find_first_occurrence__mutmut_19, 
    'x_find_first_occurrence__mutmut_20': x_find_first_occurrence__mutmut_20, 
    'x_find_first_occurrence__mutmut_21': x_find_first_occurrence__mutmut_21, 
    'x_find_first_occurrence__mutmut_22': x_find_first_occurrence__mutmut_22, 
    'x_find_first_occurrence__mutmut_23': x_find_first_occurrence__mutmut_23, 
    'x_find_first_occurrence__mutmut_24': x_find_first_occurrence__mutmut_24
}

def find_first_occurrence(*args, **kwargs):
    result = _mutmut_trampoline(x_find_first_occurrence__mutmut_orig, x_find_first_occurrence__mutmut_mutants, args, kwargs)
    return result 

find_first_occurrence.__signature__ = _mutmut_signature(x_find_first_occurrence__mutmut_orig)
x_find_first_occurrence__mutmut_orig.__name__ = 'x_find_first_occurrence'