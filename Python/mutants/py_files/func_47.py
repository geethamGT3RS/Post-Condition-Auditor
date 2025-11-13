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
def x_is_undulating__mutmut_orig(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_1(n): 
	n = None
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_2(n): 
	n = str(None)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_3(n): 
	n = str(n)
	if (len(n) < 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_4(n): 
	n = str(n)
	if (len(n) <= 3): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_5(n): 
	n = str(n)
	if (len(n) <= 2): 
		return True
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_6(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(None, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_7(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, None): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_8(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_9(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, ): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_10(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(3, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_11(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i + 2] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_12(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 3] != n[i]): 
			return False
	return True
def x_is_undulating__mutmut_13(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] == n[i]): 
			return False
	return True
def x_is_undulating__mutmut_14(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return True
	return True
def x_is_undulating__mutmut_15(n): 
	n = str(n)
	if (len(n) <= 2): 
		return False
	for i in range(2, len(n)): 
		if (n[i - 2] != n[i]): 
			return False
	return False

x_is_undulating__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_undulating__mutmut_1': x_is_undulating__mutmut_1, 
    'x_is_undulating__mutmut_2': x_is_undulating__mutmut_2, 
    'x_is_undulating__mutmut_3': x_is_undulating__mutmut_3, 
    'x_is_undulating__mutmut_4': x_is_undulating__mutmut_4, 
    'x_is_undulating__mutmut_5': x_is_undulating__mutmut_5, 
    'x_is_undulating__mutmut_6': x_is_undulating__mutmut_6, 
    'x_is_undulating__mutmut_7': x_is_undulating__mutmut_7, 
    'x_is_undulating__mutmut_8': x_is_undulating__mutmut_8, 
    'x_is_undulating__mutmut_9': x_is_undulating__mutmut_9, 
    'x_is_undulating__mutmut_10': x_is_undulating__mutmut_10, 
    'x_is_undulating__mutmut_11': x_is_undulating__mutmut_11, 
    'x_is_undulating__mutmut_12': x_is_undulating__mutmut_12, 
    'x_is_undulating__mutmut_13': x_is_undulating__mutmut_13, 
    'x_is_undulating__mutmut_14': x_is_undulating__mutmut_14, 
    'x_is_undulating__mutmut_15': x_is_undulating__mutmut_15
}

def is_undulating(*args, **kwargs):
	result = _mutmut_trampoline(x_is_undulating__mutmut_orig, x_is_undulating__mutmut_mutants, args, kwargs)
	return result 

is_undulating.__signature__ = _mutmut_signature(x_is_undulating__mutmut_orig)
x_is_undulating__mutmut_orig.__name__ = 'x_is_undulating'