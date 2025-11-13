import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
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
def x_check_char__mutmut_orig(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_1(string): 
	if(re.search(None, string)): 
		return "Valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_2(string): 
	if(re.search(regex, None)): 
		return "Valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_3(string): 
	if(re.search(string)): 
		return "Valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_4(string): 
	if(re.search(regex, )): 
		return "Valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_5(string): 
	if(re.search(regex, string)): 
		return "XXValidXX" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_6(string): 
	if(re.search(regex, string)): 
		return "valid" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_7(string): 
	if(re.search(regex, string)): 
		return "VALID" 
	else: 
		return "Invalid" 
def x_check_char__mutmut_8(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "XXInvalidXX" 
def x_check_char__mutmut_9(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "invalid" 
def x_check_char__mutmut_10(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "INVALID" 

x_check_char__mutmut_mutants : ClassVar[MutantDict] = {
'x_check_char__mutmut_1': x_check_char__mutmut_1, 
    'x_check_char__mutmut_2': x_check_char__mutmut_2, 
    'x_check_char__mutmut_3': x_check_char__mutmut_3, 
    'x_check_char__mutmut_4': x_check_char__mutmut_4, 
    'x_check_char__mutmut_5': x_check_char__mutmut_5, 
    'x_check_char__mutmut_6': x_check_char__mutmut_6, 
    'x_check_char__mutmut_7': x_check_char__mutmut_7, 
    'x_check_char__mutmut_8': x_check_char__mutmut_8, 
    'x_check_char__mutmut_9': x_check_char__mutmut_9, 
    'x_check_char__mutmut_10': x_check_char__mutmut_10
}

def check_char(*args, **kwargs):
	result = _mutmut_trampoline(x_check_char__mutmut_orig, x_check_char__mutmut_mutants, args, kwargs)
	return result 

check_char.__signature__ = _mutmut_signature(x_check_char__mutmut_orig)
x_check_char__mutmut_orig.__name__ = 'x_check_char'