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
def x_eulerian_num__mutmut_orig(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_1(n, m): 
	if (m >= n and n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_2(n, m): 
	if (m > n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_3(n, m): 
	if (m >= n or n != 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_4(n, m): 
	if (m >= n or n == 1): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_5(n, m): 
	if (m >= n or n == 0): 
		return 1 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_6(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m != 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_7(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 1): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_8(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 2 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_9(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) - (m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_10(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) / eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_11(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n + m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_12(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(None, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_13(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, None) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_14(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_15(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, ) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_16(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n + 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_17(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 2, m - 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_18(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m + 1) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_19(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 2) +(m + 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_20(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) / eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_21(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m - 1) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_22(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 2) * eulerian_num(n - 1, m))
def x_eulerian_num__mutmut_23(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(None, m))
def x_eulerian_num__mutmut_24(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, None))
def x_eulerian_num__mutmut_25(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(m))
def x_eulerian_num__mutmut_26(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, ))
def x_eulerian_num__mutmut_27(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n + 1, m))
def x_eulerian_num__mutmut_28(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 2, m))

x_eulerian_num__mutmut_mutants : ClassVar[MutantDict] = {
'x_eulerian_num__mutmut_1': x_eulerian_num__mutmut_1, 
    'x_eulerian_num__mutmut_2': x_eulerian_num__mutmut_2, 
    'x_eulerian_num__mutmut_3': x_eulerian_num__mutmut_3, 
    'x_eulerian_num__mutmut_4': x_eulerian_num__mutmut_4, 
    'x_eulerian_num__mutmut_5': x_eulerian_num__mutmut_5, 
    'x_eulerian_num__mutmut_6': x_eulerian_num__mutmut_6, 
    'x_eulerian_num__mutmut_7': x_eulerian_num__mutmut_7, 
    'x_eulerian_num__mutmut_8': x_eulerian_num__mutmut_8, 
    'x_eulerian_num__mutmut_9': x_eulerian_num__mutmut_9, 
    'x_eulerian_num__mutmut_10': x_eulerian_num__mutmut_10, 
    'x_eulerian_num__mutmut_11': x_eulerian_num__mutmut_11, 
    'x_eulerian_num__mutmut_12': x_eulerian_num__mutmut_12, 
    'x_eulerian_num__mutmut_13': x_eulerian_num__mutmut_13, 
    'x_eulerian_num__mutmut_14': x_eulerian_num__mutmut_14, 
    'x_eulerian_num__mutmut_15': x_eulerian_num__mutmut_15, 
    'x_eulerian_num__mutmut_16': x_eulerian_num__mutmut_16, 
    'x_eulerian_num__mutmut_17': x_eulerian_num__mutmut_17, 
    'x_eulerian_num__mutmut_18': x_eulerian_num__mutmut_18, 
    'x_eulerian_num__mutmut_19': x_eulerian_num__mutmut_19, 
    'x_eulerian_num__mutmut_20': x_eulerian_num__mutmut_20, 
    'x_eulerian_num__mutmut_21': x_eulerian_num__mutmut_21, 
    'x_eulerian_num__mutmut_22': x_eulerian_num__mutmut_22, 
    'x_eulerian_num__mutmut_23': x_eulerian_num__mutmut_23, 
    'x_eulerian_num__mutmut_24': x_eulerian_num__mutmut_24, 
    'x_eulerian_num__mutmut_25': x_eulerian_num__mutmut_25, 
    'x_eulerian_num__mutmut_26': x_eulerian_num__mutmut_26, 
    'x_eulerian_num__mutmut_27': x_eulerian_num__mutmut_27, 
    'x_eulerian_num__mutmut_28': x_eulerian_num__mutmut_28
}

def eulerian_num(*args, **kwargs):
	result = _mutmut_trampoline(x_eulerian_num__mutmut_orig, x_eulerian_num__mutmut_mutants, args, kwargs)
	return result 

eulerian_num.__signature__ = _mutmut_signature(x_eulerian_num__mutmut_orig)
x_eulerian_num__mutmut_orig.__name__ = 'x_eulerian_num'