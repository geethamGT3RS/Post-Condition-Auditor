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
def x_find_length__mutmut_orig(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_1(string): 
	n = None
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_2(string): 
	n = len(string)
	current_sum = None
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_3(string): 
	n = len(string)
	current_sum = 1
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_4(string): 
	n = len(string)
	current_sum = 0
	max_sum = None
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_5(string): 
	n = len(string)
	current_sum = 0
	max_sum = 1
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_6(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(None): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_7(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum = (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_8(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum -= (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_9(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (2 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_10(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] != '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_11(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == 'XX0XX' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_12(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else +1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_13(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -2) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_14(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum <= 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_15(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 1: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_16(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = None
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_17(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 1
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_18(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = None 
	return max_sum if max_sum else 0
def x_find_length__mutmut_19(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(None, max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_20(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, None) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_21(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(max_sum) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_22(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, ) 
	return max_sum if max_sum else 0
def x_find_length__mutmut_23(string): 
	n = len(string)
	current_sum = 0
	max_sum = 0
	for i in range(n): 
		current_sum += (1 if string[i] == '0' else -1) 
		if current_sum < 0: 
			current_sum = 0
		max_sum = max(current_sum, max_sum) 
	return max_sum if max_sum else 1

x_find_length__mutmut_mutants : ClassVar[MutantDict] = {
'x_find_length__mutmut_1': x_find_length__mutmut_1, 
    'x_find_length__mutmut_2': x_find_length__mutmut_2, 
    'x_find_length__mutmut_3': x_find_length__mutmut_3, 
    'x_find_length__mutmut_4': x_find_length__mutmut_4, 
    'x_find_length__mutmut_5': x_find_length__mutmut_5, 
    'x_find_length__mutmut_6': x_find_length__mutmut_6, 
    'x_find_length__mutmut_7': x_find_length__mutmut_7, 
    'x_find_length__mutmut_8': x_find_length__mutmut_8, 
    'x_find_length__mutmut_9': x_find_length__mutmut_9, 
    'x_find_length__mutmut_10': x_find_length__mutmut_10, 
    'x_find_length__mutmut_11': x_find_length__mutmut_11, 
    'x_find_length__mutmut_12': x_find_length__mutmut_12, 
    'x_find_length__mutmut_13': x_find_length__mutmut_13, 
    'x_find_length__mutmut_14': x_find_length__mutmut_14, 
    'x_find_length__mutmut_15': x_find_length__mutmut_15, 
    'x_find_length__mutmut_16': x_find_length__mutmut_16, 
    'x_find_length__mutmut_17': x_find_length__mutmut_17, 
    'x_find_length__mutmut_18': x_find_length__mutmut_18, 
    'x_find_length__mutmut_19': x_find_length__mutmut_19, 
    'x_find_length__mutmut_20': x_find_length__mutmut_20, 
    'x_find_length__mutmut_21': x_find_length__mutmut_21, 
    'x_find_length__mutmut_22': x_find_length__mutmut_22, 
    'x_find_length__mutmut_23': x_find_length__mutmut_23
}

def find_length(*args, **kwargs):
	result = _mutmut_trampoline(x_find_length__mutmut_orig, x_find_length__mutmut_mutants, args, kwargs)
	return result 

find_length.__signature__ = _mutmut_signature(x_find_length__mutmut_orig)
x_find_length__mutmut_orig.__name__ = 'x_find_length'