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
def x_is_sublist__mutmut_orig(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_1(l, s):
	sub_set = None
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_2(l, s):
	sub_set = True
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_3(l, s):
	sub_set = False
	if s != []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_4(l, s):
	sub_set = False
	if s == []:
		sub_set = None
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_5(l, s):
	sub_set = False
	if s == []:
		sub_set = False
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_6(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s != l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_7(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = None
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_8(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = False
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_9(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) >= len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_10(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = None
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_11(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = True
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_12(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(None):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_13(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] != s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_14(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[1]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_15(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = None
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_16(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 2
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_17(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) or (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_18(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n <= len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_19(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i - n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_20(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] != s[n]):
					n += 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_21(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n = 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_22(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n -= 1				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_23(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 2				
				if n == len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_24(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n != len(s):
					sub_set = True
	return sub_set
def x_is_sublist__mutmut_25(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = None
	return sub_set
def x_is_sublist__mutmut_26(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False
	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1				
				if n == len(s):
					sub_set = False
	return sub_set

x_is_sublist__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_sublist__mutmut_1': x_is_sublist__mutmut_1, 
    'x_is_sublist__mutmut_2': x_is_sublist__mutmut_2, 
    'x_is_sublist__mutmut_3': x_is_sublist__mutmut_3, 
    'x_is_sublist__mutmut_4': x_is_sublist__mutmut_4, 
    'x_is_sublist__mutmut_5': x_is_sublist__mutmut_5, 
    'x_is_sublist__mutmut_6': x_is_sublist__mutmut_6, 
    'x_is_sublist__mutmut_7': x_is_sublist__mutmut_7, 
    'x_is_sublist__mutmut_8': x_is_sublist__mutmut_8, 
    'x_is_sublist__mutmut_9': x_is_sublist__mutmut_9, 
    'x_is_sublist__mutmut_10': x_is_sublist__mutmut_10, 
    'x_is_sublist__mutmut_11': x_is_sublist__mutmut_11, 
    'x_is_sublist__mutmut_12': x_is_sublist__mutmut_12, 
    'x_is_sublist__mutmut_13': x_is_sublist__mutmut_13, 
    'x_is_sublist__mutmut_14': x_is_sublist__mutmut_14, 
    'x_is_sublist__mutmut_15': x_is_sublist__mutmut_15, 
    'x_is_sublist__mutmut_16': x_is_sublist__mutmut_16, 
    'x_is_sublist__mutmut_17': x_is_sublist__mutmut_17, 
    'x_is_sublist__mutmut_18': x_is_sublist__mutmut_18, 
    'x_is_sublist__mutmut_19': x_is_sublist__mutmut_19, 
    'x_is_sublist__mutmut_20': x_is_sublist__mutmut_20, 
    'x_is_sublist__mutmut_21': x_is_sublist__mutmut_21, 
    'x_is_sublist__mutmut_22': x_is_sublist__mutmut_22, 
    'x_is_sublist__mutmut_23': x_is_sublist__mutmut_23, 
    'x_is_sublist__mutmut_24': x_is_sublist__mutmut_24, 
    'x_is_sublist__mutmut_25': x_is_sublist__mutmut_25, 
    'x_is_sublist__mutmut_26': x_is_sublist__mutmut_26
}

def is_sublist(*args, **kwargs):
	result = _mutmut_trampoline(x_is_sublist__mutmut_orig, x_is_sublist__mutmut_mutants, args, kwargs)
	return result 

is_sublist.__signature__ = _mutmut_signature(x_is_sublist__mutmut_orig)
x_is_sublist__mutmut_orig.__name__ = 'x_is_sublist'