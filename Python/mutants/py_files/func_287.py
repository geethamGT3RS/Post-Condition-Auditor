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
def x_even_ele__mutmut_orig(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_1(test_tuple, even_fnc): 
	res = None 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_2(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res = (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_3(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res -= (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_4(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(None, even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_5(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, None), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_6(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(even_fnc), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_7(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, ), ) 
		elif even_fnc(ele): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_8(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(None): 
			res += (ele, ) 
	return res 
def x_even_ele__mutmut_9(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res = (ele, ) 
	return res 
def x_even_ele__mutmut_10(test_tuple, even_fnc): 
	res = tuple() 
	for ele in test_tuple: 
		if isinstance(ele, tuple): 
			res += (even_ele(ele, even_fnc), ) 
		elif even_fnc(ele): 
			res -= (ele, ) 
	return res 

x_even_ele__mutmut_mutants : ClassVar[MutantDict] = {
'x_even_ele__mutmut_1': x_even_ele__mutmut_1, 
    'x_even_ele__mutmut_2': x_even_ele__mutmut_2, 
    'x_even_ele__mutmut_3': x_even_ele__mutmut_3, 
    'x_even_ele__mutmut_4': x_even_ele__mutmut_4, 
    'x_even_ele__mutmut_5': x_even_ele__mutmut_5, 
    'x_even_ele__mutmut_6': x_even_ele__mutmut_6, 
    'x_even_ele__mutmut_7': x_even_ele__mutmut_7, 
    'x_even_ele__mutmut_8': x_even_ele__mutmut_8, 
    'x_even_ele__mutmut_9': x_even_ele__mutmut_9, 
    'x_even_ele__mutmut_10': x_even_ele__mutmut_10
}

def even_ele(*args, **kwargs):
	result = _mutmut_trampoline(x_even_ele__mutmut_orig, x_even_ele__mutmut_mutants, args, kwargs)
	return result 

even_ele.__signature__ = _mutmut_signature(x_even_ele__mutmut_orig)
x_even_ele__mutmut_orig.__name__ = 'x_even_ele'
def x_extract_even__mutmut_orig(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 == 0)
  return (res) 
def x_extract_even__mutmut_1(test_tuple):
  res = None
  return (res) 
def x_extract_even__mutmut_2(test_tuple):
  res = even_ele(None, lambda x: x % 2 == 0)
  return (res) 
def x_extract_even__mutmut_3(test_tuple):
  res = even_ele(test_tuple, None)
  return (res) 
def x_extract_even__mutmut_4(test_tuple):
  res = even_ele(lambda x: x % 2 == 0)
  return (res) 
def x_extract_even__mutmut_5(test_tuple):
  res = even_ele(test_tuple, )
  return (res) 
def x_extract_even__mutmut_6(test_tuple):
  res = even_ele(test_tuple, lambda x: None)
  return (res) 
def x_extract_even__mutmut_7(test_tuple):
  res = even_ele(test_tuple, lambda x: x / 2 == 0)
  return (res) 
def x_extract_even__mutmut_8(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 3 == 0)
  return (res) 
def x_extract_even__mutmut_9(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 != 0)
  return (res) 
def x_extract_even__mutmut_10(test_tuple):
  res = even_ele(test_tuple, lambda x: x % 2 == 1)
  return (res) 

x_extract_even__mutmut_mutants : ClassVar[MutantDict] = {
'x_extract_even__mutmut_1': x_extract_even__mutmut_1, 
    'x_extract_even__mutmut_2': x_extract_even__mutmut_2, 
    'x_extract_even__mutmut_3': x_extract_even__mutmut_3, 
    'x_extract_even__mutmut_4': x_extract_even__mutmut_4, 
    'x_extract_even__mutmut_5': x_extract_even__mutmut_5, 
    'x_extract_even__mutmut_6': x_extract_even__mutmut_6, 
    'x_extract_even__mutmut_7': x_extract_even__mutmut_7, 
    'x_extract_even__mutmut_8': x_extract_even__mutmut_8, 
    'x_extract_even__mutmut_9': x_extract_even__mutmut_9, 
    'x_extract_even__mutmut_10': x_extract_even__mutmut_10
}

def extract_even(*args, **kwargs):
	result = _mutmut_trampoline(x_extract_even__mutmut_orig, x_extract_even__mutmut_mutants, args, kwargs)
	return result 

extract_even.__signature__ = _mutmut_signature(x_extract_even__mutmut_orig)
x_extract_even__mutmut_orig.__name__ = 'x_extract_even'