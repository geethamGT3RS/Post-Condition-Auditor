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
def x_long_words__mutmut_orig(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_1(n, str):
    word_len = None
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_2(n, str):
    word_len = []
    txt = None
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_3(n, str):
    word_len = []
    txt = str.split(None)
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_4(n, str):
    word_len = []
    txt = str.split("XX XX")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_5(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) >= n:
            word_len.append(x)
    return word_len	
def x_long_words__mutmut_6(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(None)
    return word_len	

x_long_words__mutmut_mutants : ClassVar[MutantDict] = {
'x_long_words__mutmut_1': x_long_words__mutmut_1, 
    'x_long_words__mutmut_2': x_long_words__mutmut_2, 
    'x_long_words__mutmut_3': x_long_words__mutmut_3, 
    'x_long_words__mutmut_4': x_long_words__mutmut_4, 
    'x_long_words__mutmut_5': x_long_words__mutmut_5, 
    'x_long_words__mutmut_6': x_long_words__mutmut_6
}

def long_words(*args, **kwargs):
    result = _mutmut_trampoline(x_long_words__mutmut_orig, x_long_words__mutmut_mutants, args, kwargs)
    return result 

long_words.__signature__ = _mutmut_signature(x_long_words__mutmut_orig)
x_long_words__mutmut_orig.__name__ = 'x_long_words'