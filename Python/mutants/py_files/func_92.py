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
def x_find_solution__mutmut_orig(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_1(a, b, n):
	i = None
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_2(a, b, n):
	i = 1
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_3(a, b, n):
	i = 0
	while i / a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_4(a, b, n):
	i = 0
	while i * a < n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_5(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) / b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_6(a, b, n):
	i = 0
	while i * a <= n:
		if (n + (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_7(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i / a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_8(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b != 0: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_9(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 1: 
			return (i, (n - (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_10(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) / b)
		i = i + 1
	return None
def x_find_solution__mutmut_11(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n + (i * a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_12(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i / a)) // b)
		i = i + 1
	return None
def x_find_solution__mutmut_13(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = None
	return None
def x_find_solution__mutmut_14(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i - 1
	return None
def x_find_solution__mutmut_15(a, b, n):
	i = 0
	while i * a <= n:
		if (n - (i * a)) % b == 0: 
			return (i, (n - (i * a)) // b)
		i = i + 2
	return None

x_find_solution__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_solution__mutmut_1': x_find_solution__mutmut_1, 
    'x_find_solution__mutmut_2': x_find_solution__mutmut_2, 
    'x_find_solution__mutmut_3': x_find_solution__mutmut_3, 
    'x_find_solution__mutmut_4': x_find_solution__mutmut_4, 
    'x_find_solution__mutmut_5': x_find_solution__mutmut_5, 
    'x_find_solution__mutmut_6': x_find_solution__mutmut_6, 
    'x_find_solution__mutmut_7': x_find_solution__mutmut_7, 
    'x_find_solution__mutmut_8': x_find_solution__mutmut_8, 
    'x_find_solution__mutmut_9': x_find_solution__mutmut_9, 
    'x_find_solution__mutmut_10': x_find_solution__mutmut_10, 
    'x_find_solution__mutmut_11': x_find_solution__mutmut_11, 
    'x_find_solution__mutmut_12': x_find_solution__mutmut_12, 
    'x_find_solution__mutmut_13': x_find_solution__mutmut_13, 
    'x_find_solution__mutmut_14': x_find_solution__mutmut_14, 
    'x_find_solution__mutmut_15': x_find_solution__mutmut_15
}

def find_solution(*args, **kwargs):
	result = _mutmut_trampoline(x_find_solution__mutmut_orig, x_find_solution__mutmut_mutants, args, kwargs)
	return result 

find_solution.__signature__ = _mutmut_signature(x_find_solution__mutmut_orig)
x_find_solution__mutmut_orig.__name__ = 'x_find_solution'