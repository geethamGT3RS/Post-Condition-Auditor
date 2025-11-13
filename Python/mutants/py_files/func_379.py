import re
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
def x_text_match_zero_one__mutmut_orig(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_1(text):
        patterns = None
        if re.search(patterns,  text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_2(text):
        patterns = 'XXab+?XX'
        if re.search(patterns,  text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_3(text):
        patterns = 'AB+?'
        if re.search(patterns,  text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_4(text):
        patterns = 'ab+?'
        if re.search(None,  text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_5(text):
        patterns = 'ab+?'
        if re.search(patterns,  None):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_6(text):
        patterns = 'ab+?'
        if re.search(text):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_7(text):
        patterns = 'ab+?'
        if re.search(patterns,  ):
                return True
        else:
                return False
def x_text_match_zero_one__mutmut_8(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return False
        else:
                return False
def x_text_match_zero_one__mutmut_9(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return True
        else:
                return True

x_text_match_zero_one__mutmut_mutants : ClassVar[MutantDict] = {
'x_text_match_zero_one__mutmut_1': x_text_match_zero_one__mutmut_1, 
    'x_text_match_zero_one__mutmut_2': x_text_match_zero_one__mutmut_2, 
    'x_text_match_zero_one__mutmut_3': x_text_match_zero_one__mutmut_3, 
    'x_text_match_zero_one__mutmut_4': x_text_match_zero_one__mutmut_4, 
    'x_text_match_zero_one__mutmut_5': x_text_match_zero_one__mutmut_5, 
    'x_text_match_zero_one__mutmut_6': x_text_match_zero_one__mutmut_6, 
    'x_text_match_zero_one__mutmut_7': x_text_match_zero_one__mutmut_7, 
    'x_text_match_zero_one__mutmut_8': x_text_match_zero_one__mutmut_8, 
    'x_text_match_zero_one__mutmut_9': x_text_match_zero_one__mutmut_9
}

def text_match_zero_one(*args, **kwargs):
        result = _mutmut_trampoline(x_text_match_zero_one__mutmut_orig, x_text_match_zero_one__mutmut_mutants, args, kwargs)
        return result 

text_match_zero_one.__signature__ = _mutmut_signature(x_text_match_zero_one__mutmut_orig)
x_text_match_zero_one__mutmut_orig.__name__ = 'x_text_match_zero_one'