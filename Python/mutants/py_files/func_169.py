from collections import defaultdict
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
def x_max_aggregate__mutmut_orig(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
def x_max_aggregate__mutmut_1(stdata):
    temp = None
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
def x_max_aggregate__mutmut_2(stdata):
    temp = defaultdict(None)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[1])
def x_max_aggregate__mutmut_3(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] = marks
    return max(temp.items(), key=lambda x: x[1])
def x_max_aggregate__mutmut_4(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] -= marks
    return max(temp.items(), key=lambda x: x[1])
def x_max_aggregate__mutmut_5(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(None, key=lambda x: x[1])
def x_max_aggregate__mutmut_6(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=None)
def x_max_aggregate__mutmut_7(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(key=lambda x: x[1])
def x_max_aggregate__mutmut_8(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), )
def x_max_aggregate__mutmut_9(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: None)
def x_max_aggregate__mutmut_10(stdata):
    temp = defaultdict(int)
    for name, marks in stdata:
        temp[name] += marks
    return max(temp.items(), key=lambda x: x[2])

x_max_aggregate__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_aggregate__mutmut_1': x_max_aggregate__mutmut_1, 
    'x_max_aggregate__mutmut_2': x_max_aggregate__mutmut_2, 
    'x_max_aggregate__mutmut_3': x_max_aggregate__mutmut_3, 
    'x_max_aggregate__mutmut_4': x_max_aggregate__mutmut_4, 
    'x_max_aggregate__mutmut_5': x_max_aggregate__mutmut_5, 
    'x_max_aggregate__mutmut_6': x_max_aggregate__mutmut_6, 
    'x_max_aggregate__mutmut_7': x_max_aggregate__mutmut_7, 
    'x_max_aggregate__mutmut_8': x_max_aggregate__mutmut_8, 
    'x_max_aggregate__mutmut_9': x_max_aggregate__mutmut_9, 
    'x_max_aggregate__mutmut_10': x_max_aggregate__mutmut_10
}

def max_aggregate(*args, **kwargs):
    result = _mutmut_trampoline(x_max_aggregate__mutmut_orig, x_max_aggregate__mutmut_mutants, args, kwargs)
    return result 

max_aggregate.__signature__ = _mutmut_signature(x_max_aggregate__mutmut_orig)
x_max_aggregate__mutmut_orig.__name__ = 'x_max_aggregate'