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
def x_find_Element__mutmut_orig(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_1(arr,ranges,rotations,index) :  
    for i in range(None,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_2(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,None,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_3(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,None ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_4(arr,ranges,rotations,index) :  
    for i in range(-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_5(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_6(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_7(arr,ranges,rotations,index) :  
    for i in range(rotations + 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_8(arr,ranges,rotations,index) :  
    for i in range(rotations - 2,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_9(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,+1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_10(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-2,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_11(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,+1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_12(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-2 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_13(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = None 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_14(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][1] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_15(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = None 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_16(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][2] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_17(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index or right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_18(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left < index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_19(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right > index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_20(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index != left) : 
                index = right 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_21(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = None 
            else : 
                index = index - 1 
    return arr[index] 
def x_find_Element__mutmut_22(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = None 
    return arr[index] 
def x_find_Element__mutmut_23(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index + 1 
    return arr[index] 
def x_find_Element__mutmut_24(arr,ranges,rotations,index) :  
    for i in range(rotations - 1,-1,-1 ) : 
        left = ranges[i][0] 
        right = ranges[i][1] 
        if (left <= index and right >= index) : 
            if (index == left) : 
                index = right 
            else : 
                index = index - 2 
    return arr[index] 

x_find_Element__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_Element__mutmut_1': x_find_Element__mutmut_1, 
    'x_find_Element__mutmut_2': x_find_Element__mutmut_2, 
    'x_find_Element__mutmut_3': x_find_Element__mutmut_3, 
    'x_find_Element__mutmut_4': x_find_Element__mutmut_4, 
    'x_find_Element__mutmut_5': x_find_Element__mutmut_5, 
    'x_find_Element__mutmut_6': x_find_Element__mutmut_6, 
    'x_find_Element__mutmut_7': x_find_Element__mutmut_7, 
    'x_find_Element__mutmut_8': x_find_Element__mutmut_8, 
    'x_find_Element__mutmut_9': x_find_Element__mutmut_9, 
    'x_find_Element__mutmut_10': x_find_Element__mutmut_10, 
    'x_find_Element__mutmut_11': x_find_Element__mutmut_11, 
    'x_find_Element__mutmut_12': x_find_Element__mutmut_12, 
    'x_find_Element__mutmut_13': x_find_Element__mutmut_13, 
    'x_find_Element__mutmut_14': x_find_Element__mutmut_14, 
    'x_find_Element__mutmut_15': x_find_Element__mutmut_15, 
    'x_find_Element__mutmut_16': x_find_Element__mutmut_16, 
    'x_find_Element__mutmut_17': x_find_Element__mutmut_17, 
    'x_find_Element__mutmut_18': x_find_Element__mutmut_18, 
    'x_find_Element__mutmut_19': x_find_Element__mutmut_19, 
    'x_find_Element__mutmut_20': x_find_Element__mutmut_20, 
    'x_find_Element__mutmut_21': x_find_Element__mutmut_21, 
    'x_find_Element__mutmut_22': x_find_Element__mutmut_22, 
    'x_find_Element__mutmut_23': x_find_Element__mutmut_23, 
    'x_find_Element__mutmut_24': x_find_Element__mutmut_24
}

def find_Element(*args, **kwargs):
    result = _mutmut_trampoline(x_find_Element__mutmut_orig, x_find_Element__mutmut_mutants, args, kwargs)
    return result 

find_Element.__signature__ = _mutmut_signature(x_find_Element__mutmut_orig)
x_find_Element__mutmut_orig.__name__ = 'x_find_Element'