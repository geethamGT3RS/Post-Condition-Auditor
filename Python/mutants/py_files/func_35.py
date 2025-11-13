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
def x_word_len__mutmut_orig(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_1(s): 
    s = None   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_2(s): 
    s = s.split(None)   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_3(s): 
    s = s.split('XX XX')   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_4(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word) / 2!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_5(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%3!=0: 
            return True  
        else:
          return False
def x_word_len__mutmut_6(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2 == 0: 
            return True  
        else:
          return False
def x_word_len__mutmut_7(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2!=1: 
            return True  
        else:
          return False
def x_word_len__mutmut_8(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2!=0: 
            return False  
        else:
          return False
def x_word_len__mutmut_9(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2!=0: 
            return True  
        else:
          return True

x_word_len__mutmut_mutants : ClassVar[MutantDict] = {
'x_word_len__mutmut_1': x_word_len__mutmut_1, 
    'x_word_len__mutmut_2': x_word_len__mutmut_2, 
    'x_word_len__mutmut_3': x_word_len__mutmut_3, 
    'x_word_len__mutmut_4': x_word_len__mutmut_4, 
    'x_word_len__mutmut_5': x_word_len__mutmut_5, 
    'x_word_len__mutmut_6': x_word_len__mutmut_6, 
    'x_word_len__mutmut_7': x_word_len__mutmut_7, 
    'x_word_len__mutmut_8': x_word_len__mutmut_8, 
    'x_word_len__mutmut_9': x_word_len__mutmut_9
}

def word_len(*args, **kwargs):
    result = _mutmut_trampoline(x_word_len__mutmut_orig, x_word_len__mutmut_mutants, args, kwargs)
    return result 

word_len.__signature__ = _mutmut_signature(x_word_len__mutmut_orig)
x_word_len__mutmut_orig.__name__ = 'x_word_len'