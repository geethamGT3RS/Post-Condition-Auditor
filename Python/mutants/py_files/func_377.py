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
def x_extract_index_list__mutmut_orig(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_1(l1, l2, l3):
    result = None
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_2(l1, l2, l3):
    result = []
    for m, n, o in zip(None, l2, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_3(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, None, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_4(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, None):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_5(l1, l2, l3):
    result = []
    for m, n, o in zip(l2, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_6(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l3):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_7(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, ):
        if (m == n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_8(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m != n == o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_9(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n != o):
            result.append(m)
    return result
def x_extract_index_list__mutmut_10(l1, l2, l3):
    result = []
    for m, n, o in zip(l1, l2, l3):
        if (m == n == o):
            result.append(None)
    return result

x_extract_index_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_extract_index_list__mutmut_1': x_extract_index_list__mutmut_1, 
    'x_extract_index_list__mutmut_2': x_extract_index_list__mutmut_2, 
    'x_extract_index_list__mutmut_3': x_extract_index_list__mutmut_3, 
    'x_extract_index_list__mutmut_4': x_extract_index_list__mutmut_4, 
    'x_extract_index_list__mutmut_5': x_extract_index_list__mutmut_5, 
    'x_extract_index_list__mutmut_6': x_extract_index_list__mutmut_6, 
    'x_extract_index_list__mutmut_7': x_extract_index_list__mutmut_7, 
    'x_extract_index_list__mutmut_8': x_extract_index_list__mutmut_8, 
    'x_extract_index_list__mutmut_9': x_extract_index_list__mutmut_9, 
    'x_extract_index_list__mutmut_10': x_extract_index_list__mutmut_10
}

def extract_index_list(*args, **kwargs):
    result = _mutmut_trampoline(x_extract_index_list__mutmut_orig, x_extract_index_list__mutmut_mutants, args, kwargs)
    return result 

extract_index_list.__signature__ = _mutmut_signature(x_extract_index_list__mutmut_orig)
x_extract_index_list__mutmut_orig.__name__ = 'x_extract_index_list'