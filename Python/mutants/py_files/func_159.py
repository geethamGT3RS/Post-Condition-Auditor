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
def x_max_sub_array_sum_repeated__mutmut_orig(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_1(a, n, k): 
	max_so_far = None
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_2(a, n, k): 
	max_so_far = +2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_3(a, n, k): 
	max_so_far = -2147483649
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_4(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = None
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_5(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 1
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_6(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(None): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_7(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n / k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_8(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = None 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_9(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here - a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_10(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i / n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_11(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far <= max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_12(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = None 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_13(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here <= 0): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_14(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 1): 
			max_ending_here = 0
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_15(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = None
	return max_so_far
def x_max_sub_array_sum_repeated__mutmut_16(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 1
	return max_so_far

x_max_sub_array_sum_repeated__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_sub_array_sum_repeated__mutmut_1': x_max_sub_array_sum_repeated__mutmut_1, 
    'x_max_sub_array_sum_repeated__mutmut_2': x_max_sub_array_sum_repeated__mutmut_2, 
    'x_max_sub_array_sum_repeated__mutmut_3': x_max_sub_array_sum_repeated__mutmut_3, 
    'x_max_sub_array_sum_repeated__mutmut_4': x_max_sub_array_sum_repeated__mutmut_4, 
    'x_max_sub_array_sum_repeated__mutmut_5': x_max_sub_array_sum_repeated__mutmut_5, 
    'x_max_sub_array_sum_repeated__mutmut_6': x_max_sub_array_sum_repeated__mutmut_6, 
    'x_max_sub_array_sum_repeated__mutmut_7': x_max_sub_array_sum_repeated__mutmut_7, 
    'x_max_sub_array_sum_repeated__mutmut_8': x_max_sub_array_sum_repeated__mutmut_8, 
    'x_max_sub_array_sum_repeated__mutmut_9': x_max_sub_array_sum_repeated__mutmut_9, 
    'x_max_sub_array_sum_repeated__mutmut_10': x_max_sub_array_sum_repeated__mutmut_10, 
    'x_max_sub_array_sum_repeated__mutmut_11': x_max_sub_array_sum_repeated__mutmut_11, 
    'x_max_sub_array_sum_repeated__mutmut_12': x_max_sub_array_sum_repeated__mutmut_12, 
    'x_max_sub_array_sum_repeated__mutmut_13': x_max_sub_array_sum_repeated__mutmut_13, 
    'x_max_sub_array_sum_repeated__mutmut_14': x_max_sub_array_sum_repeated__mutmut_14, 
    'x_max_sub_array_sum_repeated__mutmut_15': x_max_sub_array_sum_repeated__mutmut_15, 
    'x_max_sub_array_sum_repeated__mutmut_16': x_max_sub_array_sum_repeated__mutmut_16
}

def max_sub_array_sum_repeated(*args, **kwargs):
	result = _mutmut_trampoline(x_max_sub_array_sum_repeated__mutmut_orig, x_max_sub_array_sum_repeated__mutmut_mutants, args, kwargs)
	return result 

max_sub_array_sum_repeated.__signature__ = _mutmut_signature(x_max_sub_array_sum_repeated__mutmut_orig)
x_max_sub_array_sum_repeated__mutmut_orig.__name__ = 'x_max_sub_array_sum_repeated'