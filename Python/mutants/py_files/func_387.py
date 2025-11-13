import math 
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
def x_is_polite__mutmut_orig(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 
def x_is_polite__mutmut_1(n): 
	n = None
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 
def x_is_polite__mutmut_2(n): 
	n = n - 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 
def x_is_polite__mutmut_3(n): 
	n = n + 2
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 
def x_is_polite__mutmut_4(n): 
	n = n + 1
	return (int)(None) 
def x_is_polite__mutmut_5(n): 
	n = n + 1
	return (int)(n - (math.log((n + math.log(n, 2)), 2))) 
def x_is_polite__mutmut_6(n): 
	n = n + 1
	return (int)(n+(math.log(None, 2))) 
def x_is_polite__mutmut_7(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), None))) 
def x_is_polite__mutmut_8(n): 
	n = n + 1
	return (int)(n+(math.log(2))) 
def x_is_polite__mutmut_9(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), ))) 
def x_is_polite__mutmut_10(n): 
	n = n + 1
	return (int)(n+(math.log((n - math.log(n, 2)), 2))) 
def x_is_polite__mutmut_11(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(None, 2)), 2))) 
def x_is_polite__mutmut_12(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, None)), 2))) 
def x_is_polite__mutmut_13(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(2)), 2))) 
def x_is_polite__mutmut_14(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, )), 2))) 
def x_is_polite__mutmut_15(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 3)), 2))) 
def x_is_polite__mutmut_16(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 3))) 

x_is_polite__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_polite__mutmut_1': x_is_polite__mutmut_1, 
    'x_is_polite__mutmut_2': x_is_polite__mutmut_2, 
    'x_is_polite__mutmut_3': x_is_polite__mutmut_3, 
    'x_is_polite__mutmut_4': x_is_polite__mutmut_4, 
    'x_is_polite__mutmut_5': x_is_polite__mutmut_5, 
    'x_is_polite__mutmut_6': x_is_polite__mutmut_6, 
    'x_is_polite__mutmut_7': x_is_polite__mutmut_7, 
    'x_is_polite__mutmut_8': x_is_polite__mutmut_8, 
    'x_is_polite__mutmut_9': x_is_polite__mutmut_9, 
    'x_is_polite__mutmut_10': x_is_polite__mutmut_10, 
    'x_is_polite__mutmut_11': x_is_polite__mutmut_11, 
    'x_is_polite__mutmut_12': x_is_polite__mutmut_12, 
    'x_is_polite__mutmut_13': x_is_polite__mutmut_13, 
    'x_is_polite__mutmut_14': x_is_polite__mutmut_14, 
    'x_is_polite__mutmut_15': x_is_polite__mutmut_15, 
    'x_is_polite__mutmut_16': x_is_polite__mutmut_16
}

def is_polite(*args, **kwargs):
	result = _mutmut_trampoline(x_is_polite__mutmut_orig, x_is_polite__mutmut_mutants, args, kwargs)
	return result 

is_polite.__signature__ = _mutmut_signature(x_is_polite__mutmut_orig)
x_is_polite__mutmut_orig.__name__ = 'x_is_polite'