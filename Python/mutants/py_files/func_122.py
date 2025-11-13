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
def x_max_sum__mutmut_orig(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_1(arr): 
	MSIBS = None 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_2(arr): 
	MSIBS = arr[:] 
	for i in range(None): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_3(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(None, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_4(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, None): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_5(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_6(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, ): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_7(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(1, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_8(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] or MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_9(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] >= arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_10(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] <= MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_11(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] - arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_12(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = None 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_13(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] - arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_14(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = None 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_15(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(None, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_16(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, None): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_17(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_18(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, ): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_19(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(2, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_20(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) - 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_21(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 2): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_22(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(None, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_23(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, None): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_24(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_25(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, ): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_26(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(2, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_27(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] or MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_28(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[+i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_29(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] >= arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_30(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[+j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_31(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[+i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_32(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] <= MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_33(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] - arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_34(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[+j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_35(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[+i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_36(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = None 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_37(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[+i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_38(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] - arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_39(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[+j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_40(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[+i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_41(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = None 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_42(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float(None) 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_43(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("XX-InfXX") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_44(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_45(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-INF") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_46(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(None, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_47(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, None, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_48(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, None): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_49(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_50(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_51(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, ): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum
def x_max_sum__mutmut_52(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = None 
	return max_sum
def x_max_sum__mutmut_53(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(None, i + j - k) 
	return max_sum
def x_max_sum__mutmut_54(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, None) 
	return max_sum
def x_max_sum__mutmut_55(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(i + j - k) 
	return max_sum
def x_max_sum__mutmut_56(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, ) 
	return max_sum
def x_max_sum__mutmut_57(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j + k) 
	return max_sum
def x_max_sum__mutmut_58(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i - j - k) 
	return max_sum

x_max_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_max_sum__mutmut_1': x_max_sum__mutmut_1, 
    'x_max_sum__mutmut_2': x_max_sum__mutmut_2, 
    'x_max_sum__mutmut_3': x_max_sum__mutmut_3, 
    'x_max_sum__mutmut_4': x_max_sum__mutmut_4, 
    'x_max_sum__mutmut_5': x_max_sum__mutmut_5, 
    'x_max_sum__mutmut_6': x_max_sum__mutmut_6, 
    'x_max_sum__mutmut_7': x_max_sum__mutmut_7, 
    'x_max_sum__mutmut_8': x_max_sum__mutmut_8, 
    'x_max_sum__mutmut_9': x_max_sum__mutmut_9, 
    'x_max_sum__mutmut_10': x_max_sum__mutmut_10, 
    'x_max_sum__mutmut_11': x_max_sum__mutmut_11, 
    'x_max_sum__mutmut_12': x_max_sum__mutmut_12, 
    'x_max_sum__mutmut_13': x_max_sum__mutmut_13, 
    'x_max_sum__mutmut_14': x_max_sum__mutmut_14, 
    'x_max_sum__mutmut_15': x_max_sum__mutmut_15, 
    'x_max_sum__mutmut_16': x_max_sum__mutmut_16, 
    'x_max_sum__mutmut_17': x_max_sum__mutmut_17, 
    'x_max_sum__mutmut_18': x_max_sum__mutmut_18, 
    'x_max_sum__mutmut_19': x_max_sum__mutmut_19, 
    'x_max_sum__mutmut_20': x_max_sum__mutmut_20, 
    'x_max_sum__mutmut_21': x_max_sum__mutmut_21, 
    'x_max_sum__mutmut_22': x_max_sum__mutmut_22, 
    'x_max_sum__mutmut_23': x_max_sum__mutmut_23, 
    'x_max_sum__mutmut_24': x_max_sum__mutmut_24, 
    'x_max_sum__mutmut_25': x_max_sum__mutmut_25, 
    'x_max_sum__mutmut_26': x_max_sum__mutmut_26, 
    'x_max_sum__mutmut_27': x_max_sum__mutmut_27, 
    'x_max_sum__mutmut_28': x_max_sum__mutmut_28, 
    'x_max_sum__mutmut_29': x_max_sum__mutmut_29, 
    'x_max_sum__mutmut_30': x_max_sum__mutmut_30, 
    'x_max_sum__mutmut_31': x_max_sum__mutmut_31, 
    'x_max_sum__mutmut_32': x_max_sum__mutmut_32, 
    'x_max_sum__mutmut_33': x_max_sum__mutmut_33, 
    'x_max_sum__mutmut_34': x_max_sum__mutmut_34, 
    'x_max_sum__mutmut_35': x_max_sum__mutmut_35, 
    'x_max_sum__mutmut_36': x_max_sum__mutmut_36, 
    'x_max_sum__mutmut_37': x_max_sum__mutmut_37, 
    'x_max_sum__mutmut_38': x_max_sum__mutmut_38, 
    'x_max_sum__mutmut_39': x_max_sum__mutmut_39, 
    'x_max_sum__mutmut_40': x_max_sum__mutmut_40, 
    'x_max_sum__mutmut_41': x_max_sum__mutmut_41, 
    'x_max_sum__mutmut_42': x_max_sum__mutmut_42, 
    'x_max_sum__mutmut_43': x_max_sum__mutmut_43, 
    'x_max_sum__mutmut_44': x_max_sum__mutmut_44, 
    'x_max_sum__mutmut_45': x_max_sum__mutmut_45, 
    'x_max_sum__mutmut_46': x_max_sum__mutmut_46, 
    'x_max_sum__mutmut_47': x_max_sum__mutmut_47, 
    'x_max_sum__mutmut_48': x_max_sum__mutmut_48, 
    'x_max_sum__mutmut_49': x_max_sum__mutmut_49, 
    'x_max_sum__mutmut_50': x_max_sum__mutmut_50, 
    'x_max_sum__mutmut_51': x_max_sum__mutmut_51, 
    'x_max_sum__mutmut_52': x_max_sum__mutmut_52, 
    'x_max_sum__mutmut_53': x_max_sum__mutmut_53, 
    'x_max_sum__mutmut_54': x_max_sum__mutmut_54, 
    'x_max_sum__mutmut_55': x_max_sum__mutmut_55, 
    'x_max_sum__mutmut_56': x_max_sum__mutmut_56, 
    'x_max_sum__mutmut_57': x_max_sum__mutmut_57, 
    'x_max_sum__mutmut_58': x_max_sum__mutmut_58
}

def max_sum(*args, **kwargs):
	result = _mutmut_trampoline(x_max_sum__mutmut_orig, x_max_sum__mutmut_mutants, args, kwargs)
	return result 

max_sum.__signature__ = _mutmut_signature(x_max_sum__mutmut_orig)
x_max_sum__mutmut_orig.__name__ = 'x_max_sum'