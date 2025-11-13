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
def x_last_Digit_Factorial__mutmut_orig(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_1(n): 
    if (n != 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_2(n): 
    if (n == 1): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_3(n): 
    if (n == 0): return 2
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_4(n): 
    if (n == 0): return 1
    elif (n < 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_5(n): 
    if (n == 0): return 1
    elif (n <= 3): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_6(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n != 3): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_7(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 4): return 6
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_8(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 7
    elif (n == 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_9(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n != 4): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_10(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 5): return 4 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_11(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 5 
    else: 
      return 0
def x_last_Digit_Factorial__mutmut_12(n): 
    if (n == 0): return 1
    elif (n <= 2): return n  
    elif (n == 3): return 6
    elif (n == 4): return 4 
    else: 
      return 1

x_last_Digit_Factorial__mutmut_mutants : ClassVar[MutantDict] = {
'x_last_Digit_Factorial__mutmut_1': x_last_Digit_Factorial__mutmut_1, 
    'x_last_Digit_Factorial__mutmut_2': x_last_Digit_Factorial__mutmut_2, 
    'x_last_Digit_Factorial__mutmut_3': x_last_Digit_Factorial__mutmut_3, 
    'x_last_Digit_Factorial__mutmut_4': x_last_Digit_Factorial__mutmut_4, 
    'x_last_Digit_Factorial__mutmut_5': x_last_Digit_Factorial__mutmut_5, 
    'x_last_Digit_Factorial__mutmut_6': x_last_Digit_Factorial__mutmut_6, 
    'x_last_Digit_Factorial__mutmut_7': x_last_Digit_Factorial__mutmut_7, 
    'x_last_Digit_Factorial__mutmut_8': x_last_Digit_Factorial__mutmut_8, 
    'x_last_Digit_Factorial__mutmut_9': x_last_Digit_Factorial__mutmut_9, 
    'x_last_Digit_Factorial__mutmut_10': x_last_Digit_Factorial__mutmut_10, 
    'x_last_Digit_Factorial__mutmut_11': x_last_Digit_Factorial__mutmut_11, 
    'x_last_Digit_Factorial__mutmut_12': x_last_Digit_Factorial__mutmut_12
}

def last_Digit_Factorial(*args, **kwargs):
    result = _mutmut_trampoline(x_last_Digit_Factorial__mutmut_orig, x_last_Digit_Factorial__mutmut_mutants, args, kwargs)
    return result 

last_Digit_Factorial.__signature__ = _mutmut_signature(x_last_Digit_Factorial__mutmut_orig)
x_last_Digit_Factorial__mutmut_orig.__name__ = 'x_last_Digit_Factorial'