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
def x_count_binary_seq__mutmut_orig(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_1(n): 
	nCr = None
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_2(n): 
	nCr = 2
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_3(n): 
	nCr = 1
	res = None
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_4(n): 
	nCr = 1
	res = 2
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_5(n): 
	nCr = 1
	res = 1
	for r in range(None, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_6(n): 
	nCr = 1
	res = 1
	for r in range(1, None): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_7(n): 
	nCr = 1
	res = 1
	for r in range(n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_8(n): 
	nCr = 1
	res = 1
	for r in range(1, ): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_9(n): 
	nCr = 1
	res = 1
	for r in range(2, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_10(n): 
	nCr = 1
	res = 1
	for r in range(1, n - 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_11(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 2): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_12(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = None 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_13(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) * r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_14(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr / (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_15(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 + r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_16(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n - 1 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_17(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 2 - r)) / r 
		res += nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_18(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res = nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_19(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res -= nCr * nCr 
	return res 
def x_count_binary_seq__mutmut_20(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr / nCr 
	return res 

x_count_binary_seq__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_binary_seq__mutmut_1': x_count_binary_seq__mutmut_1, 
    'x_count_binary_seq__mutmut_2': x_count_binary_seq__mutmut_2, 
    'x_count_binary_seq__mutmut_3': x_count_binary_seq__mutmut_3, 
    'x_count_binary_seq__mutmut_4': x_count_binary_seq__mutmut_4, 
    'x_count_binary_seq__mutmut_5': x_count_binary_seq__mutmut_5, 
    'x_count_binary_seq__mutmut_6': x_count_binary_seq__mutmut_6, 
    'x_count_binary_seq__mutmut_7': x_count_binary_seq__mutmut_7, 
    'x_count_binary_seq__mutmut_8': x_count_binary_seq__mutmut_8, 
    'x_count_binary_seq__mutmut_9': x_count_binary_seq__mutmut_9, 
    'x_count_binary_seq__mutmut_10': x_count_binary_seq__mutmut_10, 
    'x_count_binary_seq__mutmut_11': x_count_binary_seq__mutmut_11, 
    'x_count_binary_seq__mutmut_12': x_count_binary_seq__mutmut_12, 
    'x_count_binary_seq__mutmut_13': x_count_binary_seq__mutmut_13, 
    'x_count_binary_seq__mutmut_14': x_count_binary_seq__mutmut_14, 
    'x_count_binary_seq__mutmut_15': x_count_binary_seq__mutmut_15, 
    'x_count_binary_seq__mutmut_16': x_count_binary_seq__mutmut_16, 
    'x_count_binary_seq__mutmut_17': x_count_binary_seq__mutmut_17, 
    'x_count_binary_seq__mutmut_18': x_count_binary_seq__mutmut_18, 
    'x_count_binary_seq__mutmut_19': x_count_binary_seq__mutmut_19, 
    'x_count_binary_seq__mutmut_20': x_count_binary_seq__mutmut_20
}

def count_binary_seq(*args, **kwargs):
	result = _mutmut_trampoline(x_count_binary_seq__mutmut_orig, x_count_binary_seq__mutmut_mutants, args, kwargs)
	return result 

count_binary_seq.__signature__ = _mutmut_signature(x_count_binary_seq__mutmut_orig)
x_count_binary_seq__mutmut_orig.__name__ = 'x_count_binary_seq'