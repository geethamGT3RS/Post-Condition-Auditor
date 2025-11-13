import heapq as hq
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
def x_heap_sort__mutmut_orig(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_1(iterable):
    h = None
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_2(iterable):
    h = []
    for value in iterable:
        hq.heappush(None, value)
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_3(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, None)
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_4(iterable):
    h = []
    for value in iterable:
        hq.heappush(value)
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_5(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, )
    return [hq.heappop(h) for i in range(len(h))]
def x_heap_sort__mutmut_6(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(None) for i in range(len(h))]
def x_heap_sort__mutmut_7(iterable):
    h = []
    for value in iterable:
        hq.heappush(h, value)
    return [hq.heappop(h) for i in range(None)]

x_heap_sort__mutmut_mutants : ClassVar[MutantDict] = {
'x_heap_sort__mutmut_1': x_heap_sort__mutmut_1, 
    'x_heap_sort__mutmut_2': x_heap_sort__mutmut_2, 
    'x_heap_sort__mutmut_3': x_heap_sort__mutmut_3, 
    'x_heap_sort__mutmut_4': x_heap_sort__mutmut_4, 
    'x_heap_sort__mutmut_5': x_heap_sort__mutmut_5, 
    'x_heap_sort__mutmut_6': x_heap_sort__mutmut_6, 
    'x_heap_sort__mutmut_7': x_heap_sort__mutmut_7
}

def heap_sort(*args, **kwargs):
    result = _mutmut_trampoline(x_heap_sort__mutmut_orig, x_heap_sort__mutmut_mutants, args, kwargs)
    return result 

heap_sort.__signature__ = _mutmut_signature(x_heap_sort__mutmut_orig)
x_heap_sort__mutmut_orig.__name__ = 'x_heap_sort'