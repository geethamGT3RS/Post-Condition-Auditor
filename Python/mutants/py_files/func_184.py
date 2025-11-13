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
def x_convert_list_dictionary__mutmut_orig(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
def x_convert_list_dictionary__mutmut_1(l1, l2, l3):
     result = None
     return result
def x_convert_list_dictionary__mutmut_2(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(None, l2, l3)]
     return result
def x_convert_list_dictionary__mutmut_3(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, None, l3)]
     return result
def x_convert_list_dictionary__mutmut_4(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, None)]
     return result
def x_convert_list_dictionary__mutmut_5(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l2, l3)]
     return result
def x_convert_list_dictionary__mutmut_6(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l3)]
     return result
def x_convert_list_dictionary__mutmut_7(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, )]
     return result

x_convert_list_dictionary__mutmut_mutants : ClassVar[MutantDict] = {
'x_convert_list_dictionary__mutmut_1': x_convert_list_dictionary__mutmut_1, 
    'x_convert_list_dictionary__mutmut_2': x_convert_list_dictionary__mutmut_2, 
    'x_convert_list_dictionary__mutmut_3': x_convert_list_dictionary__mutmut_3, 
    'x_convert_list_dictionary__mutmut_4': x_convert_list_dictionary__mutmut_4, 
    'x_convert_list_dictionary__mutmut_5': x_convert_list_dictionary__mutmut_5, 
    'x_convert_list_dictionary__mutmut_6': x_convert_list_dictionary__mutmut_6, 
    'x_convert_list_dictionary__mutmut_7': x_convert_list_dictionary__mutmut_7
}

def convert_list_dictionary(*args, **kwargs):
     result = _mutmut_trampoline(x_convert_list_dictionary__mutmut_orig, x_convert_list_dictionary__mutmut_mutants, args, kwargs)
     return result 

convert_list_dictionary.__signature__ = _mutmut_signature(x_convert_list_dictionary__mutmut_orig)
x_convert_list_dictionary__mutmut_orig.__name__ = 'x_convert_list_dictionary'