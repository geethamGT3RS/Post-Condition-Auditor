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
def x_flatten_list__mutmut_orig(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_1(list1):
    result_list = None
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_2(list1):
    result_list = []
    if list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_3(list1):
    result_list = []
    if not list1: return result_list
    stack = None
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_4(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(None)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_5(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = None
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_6(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = None
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_7(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(None)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_8(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(None)
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_9(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(None))
        else: result_list.append(next)
    result_list.reverse()
    return result_list 
def x_flatten_list__mutmut_10(list1):
    result_list = []
    if not list1: return result_list
    stack = [list(list1)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(None)
    result_list.reverse()
    return result_list 

x_flatten_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_flatten_list__mutmut_1': x_flatten_list__mutmut_1, 
    'x_flatten_list__mutmut_2': x_flatten_list__mutmut_2, 
    'x_flatten_list__mutmut_3': x_flatten_list__mutmut_3, 
    'x_flatten_list__mutmut_4': x_flatten_list__mutmut_4, 
    'x_flatten_list__mutmut_5': x_flatten_list__mutmut_5, 
    'x_flatten_list__mutmut_6': x_flatten_list__mutmut_6, 
    'x_flatten_list__mutmut_7': x_flatten_list__mutmut_7, 
    'x_flatten_list__mutmut_8': x_flatten_list__mutmut_8, 
    'x_flatten_list__mutmut_9': x_flatten_list__mutmut_9, 
    'x_flatten_list__mutmut_10': x_flatten_list__mutmut_10
}

def flatten_list(*args, **kwargs):
    result = _mutmut_trampoline(x_flatten_list__mutmut_orig, x_flatten_list__mutmut_mutants, args, kwargs)
    return result 

flatten_list.__signature__ = _mutmut_signature(x_flatten_list__mutmut_orig)
x_flatten_list__mutmut_orig.__name__ = 'x_flatten_list'