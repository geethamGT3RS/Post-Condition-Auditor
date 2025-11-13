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
def x_text_match_wordz_middle__mutmut_orig(text):
        return bool(re.search(r'\Bz\B',  text))
def x_text_match_wordz_middle__mutmut_1(text):
        return bool(None)
def x_text_match_wordz_middle__mutmut_2(text):
        return bool(re.search(None,  text))
def x_text_match_wordz_middle__mutmut_3(text):
        return bool(re.search(r'\Bz\B',  None))
def x_text_match_wordz_middle__mutmut_4(text):
        return bool(re.search(text))
def x_text_match_wordz_middle__mutmut_5(text):
        return bool(re.search(r'\Bz\B',  ))
def x_text_match_wordz_middle__mutmut_6(text):
        return bool(re.search(r'XX\Bz\BXX',  text))
def x_text_match_wordz_middle__mutmut_7(text):
        return bool(re.search(r'\Bz\B',  text))
def x_text_match_wordz_middle__mutmut_8(text):
        return bool(re.search(r'\BZ\B',  text))

x_text_match_wordz_middle__mutmut_mutants : ClassVar[MutantDict] = {
'x_text_match_wordz_middle__mutmut_1': x_text_match_wordz_middle__mutmut_1, 
    'x_text_match_wordz_middle__mutmut_2': x_text_match_wordz_middle__mutmut_2, 
    'x_text_match_wordz_middle__mutmut_3': x_text_match_wordz_middle__mutmut_3, 
    'x_text_match_wordz_middle__mutmut_4': x_text_match_wordz_middle__mutmut_4, 
    'x_text_match_wordz_middle__mutmut_5': x_text_match_wordz_middle__mutmut_5, 
    'x_text_match_wordz_middle__mutmut_6': x_text_match_wordz_middle__mutmut_6, 
    'x_text_match_wordz_middle__mutmut_7': x_text_match_wordz_middle__mutmut_7, 
    'x_text_match_wordz_middle__mutmut_8': x_text_match_wordz_middle__mutmut_8
}

def text_match_wordz_middle(*args, **kwargs):
        result = _mutmut_trampoline(x_text_match_wordz_middle__mutmut_orig, x_text_match_wordz_middle__mutmut_mutants, args, kwargs)
        return result 

text_match_wordz_middle.__signature__ = _mutmut_signature(x_text_match_wordz_middle__mutmut_orig)
x_text_match_wordz_middle__mutmut_orig.__name__ = 'x_text_match_wordz_middle'