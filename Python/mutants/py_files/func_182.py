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
def x_find_lucas__mutmut_orig(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_1(n): 
	if (n != 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_2(n): 
	if (n == 1): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_3(n): 
	if (n == 0): 
		return 3
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_4(n): 
	if (n == 0): 
		return 2
	if (n != 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_5(n): 
	if (n == 0): 
		return 2
	if (n == 2): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_6(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 2
	return find_lucas(n - 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_7(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) - find_lucas(n - 2) 
def x_find_lucas__mutmut_8(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(None) + find_lucas(n - 2) 
def x_find_lucas__mutmut_9(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n + 1) + find_lucas(n - 2) 
def x_find_lucas__mutmut_10(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 2) + find_lucas(n - 2) 
def x_find_lucas__mutmut_11(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(None) 
def x_find_lucas__mutmut_12(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n + 2) 
def x_find_lucas__mutmut_13(n): 
	if (n == 0): 
		return 2
	if (n == 1): 
		return 1
	return find_lucas(n - 1) + find_lucas(n - 3) 

x_find_lucas__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_lucas__mutmut_1': x_find_lucas__mutmut_1, 
    'x_find_lucas__mutmut_2': x_find_lucas__mutmut_2, 
    'x_find_lucas__mutmut_3': x_find_lucas__mutmut_3, 
    'x_find_lucas__mutmut_4': x_find_lucas__mutmut_4, 
    'x_find_lucas__mutmut_5': x_find_lucas__mutmut_5, 
    'x_find_lucas__mutmut_6': x_find_lucas__mutmut_6, 
    'x_find_lucas__mutmut_7': x_find_lucas__mutmut_7, 
    'x_find_lucas__mutmut_8': x_find_lucas__mutmut_8, 
    'x_find_lucas__mutmut_9': x_find_lucas__mutmut_9, 
    'x_find_lucas__mutmut_10': x_find_lucas__mutmut_10, 
    'x_find_lucas__mutmut_11': x_find_lucas__mutmut_11, 
    'x_find_lucas__mutmut_12': x_find_lucas__mutmut_12, 
    'x_find_lucas__mutmut_13': x_find_lucas__mutmut_13
}

def find_lucas(*args, **kwargs):
	result = _mutmut_trampoline(x_find_lucas__mutmut_orig, x_find_lucas__mutmut_mutants, args, kwargs)
	return result 

find_lucas.__signature__ = _mutmut_signature(x_find_lucas__mutmut_orig)
x_find_lucas__mutmut_orig.__name__ = 'x_find_lucas'