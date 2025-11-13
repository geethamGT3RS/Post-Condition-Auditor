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
def x_group_tuples__mutmut_orig(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_1(Input): 
	out = None 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_2(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(None) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_3(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[1]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_4(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[2:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_5(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = None 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_6(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[1]] = list(elem) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_7(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(None) 
	return [tuple(values) for values in out.values()] 
def x_group_tuples__mutmut_8(Input): 
	out = {} 
	for elem in Input: 
		try: 
			out[elem[0]].extend(elem[1:]) 
		except KeyError: 
			out[elem[0]] = list(elem) 
	return [tuple(None) for values in out.values()] 

x_group_tuples__mutmut_mutants : ClassVar[MutantDict] = {
'x_group_tuples__mutmut_1': x_group_tuples__mutmut_1, 
    'x_group_tuples__mutmut_2': x_group_tuples__mutmut_2, 
    'x_group_tuples__mutmut_3': x_group_tuples__mutmut_3, 
    'x_group_tuples__mutmut_4': x_group_tuples__mutmut_4, 
    'x_group_tuples__mutmut_5': x_group_tuples__mutmut_5, 
    'x_group_tuples__mutmut_6': x_group_tuples__mutmut_6, 
    'x_group_tuples__mutmut_7': x_group_tuples__mutmut_7, 
    'x_group_tuples__mutmut_8': x_group_tuples__mutmut_8
}

def group_tuples(*args, **kwargs):
	result = _mutmut_trampoline(x_group_tuples__mutmut_orig, x_group_tuples__mutmut_mutants, args, kwargs)
	return result 

group_tuples.__signature__ = _mutmut_signature(x_group_tuples__mutmut_orig)
x_group_tuples__mutmut_orig.__name__ = 'x_group_tuples'