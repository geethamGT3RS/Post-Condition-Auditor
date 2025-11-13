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
def x_change_date_format__mutmut_orig(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_1(dt):
        return re.sub(None, '\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_2(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', None, dt)
def x_change_date_format__mutmut_3(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', None)
def x_change_date_format__mutmut_4(dt):
        return re.sub('\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_5(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', dt)
def x_change_date_format__mutmut_6(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', )
def x_change_date_format__mutmut_7(dt):
        return re.sub(r'XX(\d{4})-(\d{1,2})-(\d{1,2})XX', '\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_8(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_9(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
def x_change_date_format__mutmut_10(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', 'XX\\3-\\2-\\1XX', dt)

x_change_date_format__mutmut_mutants : ClassVar[MutantDict] = {
'x_change_date_format__mutmut_1': x_change_date_format__mutmut_1, 
    'x_change_date_format__mutmut_2': x_change_date_format__mutmut_2, 
    'x_change_date_format__mutmut_3': x_change_date_format__mutmut_3, 
    'x_change_date_format__mutmut_4': x_change_date_format__mutmut_4, 
    'x_change_date_format__mutmut_5': x_change_date_format__mutmut_5, 
    'x_change_date_format__mutmut_6': x_change_date_format__mutmut_6, 
    'x_change_date_format__mutmut_7': x_change_date_format__mutmut_7, 
    'x_change_date_format__mutmut_8': x_change_date_format__mutmut_8, 
    'x_change_date_format__mutmut_9': x_change_date_format__mutmut_9, 
    'x_change_date_format__mutmut_10': x_change_date_format__mutmut_10
}

def change_date_format(*args, **kwargs):
        result = _mutmut_trampoline(x_change_date_format__mutmut_orig, x_change_date_format__mutmut_mutants, args, kwargs)
        return result 

change_date_format.__signature__ = _mutmut_signature(x_change_date_format__mutmut_orig)
x_change_date_format__mutmut_orig.__name__ = 'x_change_date_format'