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
def x_recursive_list_sum__mutmut_orig(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_1(data_list):
	total = None
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_2(data_list):
	total = 1
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_3(data_list):
	total = 0
	for element in data_list:
		if type(None) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_4(data_list):
	total = 0
	for element in data_list:
		if type(element) != type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_5(data_list):
	total = 0
	for element in data_list:
		if type(element) == type(None):
			total = total + recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_6(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = None
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_7(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total - recursive_list_sum(element)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_8(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(None)
		else:
			total = total + element
	return total
def x_recursive_list_sum__mutmut_9(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = None
	return total
def x_recursive_list_sum__mutmut_10(data_list):
	total = 0
	for element in data_list:
		if type(element) == type([]):
			total = total + recursive_list_sum(element)
		else:
			total = total - element
	return total

x_recursive_list_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_recursive_list_sum__mutmut_1': x_recursive_list_sum__mutmut_1, 
    'x_recursive_list_sum__mutmut_2': x_recursive_list_sum__mutmut_2, 
    'x_recursive_list_sum__mutmut_3': x_recursive_list_sum__mutmut_3, 
    'x_recursive_list_sum__mutmut_4': x_recursive_list_sum__mutmut_4, 
    'x_recursive_list_sum__mutmut_5': x_recursive_list_sum__mutmut_5, 
    'x_recursive_list_sum__mutmut_6': x_recursive_list_sum__mutmut_6, 
    'x_recursive_list_sum__mutmut_7': x_recursive_list_sum__mutmut_7, 
    'x_recursive_list_sum__mutmut_8': x_recursive_list_sum__mutmut_8, 
    'x_recursive_list_sum__mutmut_9': x_recursive_list_sum__mutmut_9, 
    'x_recursive_list_sum__mutmut_10': x_recursive_list_sum__mutmut_10
}

def recursive_list_sum(*args, **kwargs):
	result = _mutmut_trampoline(x_recursive_list_sum__mutmut_orig, x_recursive_list_sum__mutmut_mutants, args, kwargs)
	return result 

recursive_list_sum.__signature__ = _mutmut_signature(x_recursive_list_sum__mutmut_orig)
x_recursive_list_sum__mutmut_orig.__name__ = 'x_recursive_list_sum'