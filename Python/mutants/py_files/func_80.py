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
def x_reverse_vowels__mutmut_orig(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_1(str1):
	vowels = None
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_2(str1):
	vowels = "XXXX"
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_3(str1):
	vowels = ""
	for char in str1:
		if char not in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_4(str1):
	vowels = ""
	for char in str1:
		if char in "XXaeiouAEIOUXX":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_5(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouaeiou":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_6(str1):
	vowels = ""
	for char in str1:
		if char in "AEIOUAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_7(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels = char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_8(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels -= char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_9(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = None
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_10(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = "XXXX"
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_11(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char not in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_12(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "XXaeiouAEIOUXX":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_13(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouaeiou":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_14(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "AEIOUAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_15(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string = vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_16(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string -= vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_17(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[+1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_18(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-2]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_19(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = None
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_20(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:+1]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_21(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-2]
		else:
			result_string += char
	return result_string
def x_reverse_vowels__mutmut_22(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string = char
	return result_string
def x_reverse_vowels__mutmut_23(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string -= char
	return result_string

x_reverse_vowels__mutmut_mutants : ClassVar[MutantDict] = {
'x_reverse_vowels__mutmut_1': x_reverse_vowels__mutmut_1, 
    'x_reverse_vowels__mutmut_2': x_reverse_vowels__mutmut_2, 
    'x_reverse_vowels__mutmut_3': x_reverse_vowels__mutmut_3, 
    'x_reverse_vowels__mutmut_4': x_reverse_vowels__mutmut_4, 
    'x_reverse_vowels__mutmut_5': x_reverse_vowels__mutmut_5, 
    'x_reverse_vowels__mutmut_6': x_reverse_vowels__mutmut_6, 
    'x_reverse_vowels__mutmut_7': x_reverse_vowels__mutmut_7, 
    'x_reverse_vowels__mutmut_8': x_reverse_vowels__mutmut_8, 
    'x_reverse_vowels__mutmut_9': x_reverse_vowels__mutmut_9, 
    'x_reverse_vowels__mutmut_10': x_reverse_vowels__mutmut_10, 
    'x_reverse_vowels__mutmut_11': x_reverse_vowels__mutmut_11, 
    'x_reverse_vowels__mutmut_12': x_reverse_vowels__mutmut_12, 
    'x_reverse_vowels__mutmut_13': x_reverse_vowels__mutmut_13, 
    'x_reverse_vowels__mutmut_14': x_reverse_vowels__mutmut_14, 
    'x_reverse_vowels__mutmut_15': x_reverse_vowels__mutmut_15, 
    'x_reverse_vowels__mutmut_16': x_reverse_vowels__mutmut_16, 
    'x_reverse_vowels__mutmut_17': x_reverse_vowels__mutmut_17, 
    'x_reverse_vowels__mutmut_18': x_reverse_vowels__mutmut_18, 
    'x_reverse_vowels__mutmut_19': x_reverse_vowels__mutmut_19, 
    'x_reverse_vowels__mutmut_20': x_reverse_vowels__mutmut_20, 
    'x_reverse_vowels__mutmut_21': x_reverse_vowels__mutmut_21, 
    'x_reverse_vowels__mutmut_22': x_reverse_vowels__mutmut_22, 
    'x_reverse_vowels__mutmut_23': x_reverse_vowels__mutmut_23
}

def reverse_vowels(*args, **kwargs):
	result = _mutmut_trampoline(x_reverse_vowels__mutmut_orig, x_reverse_vowels__mutmut_mutants, args, kwargs)
	return result 

reverse_vowels.__signature__ = _mutmut_signature(x_reverse_vowels__mutmut_orig)
x_reverse_vowels__mutmut_orig.__name__ = 'x_reverse_vowels'