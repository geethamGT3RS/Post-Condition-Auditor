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
def x_is_woodall__mutmut_orig(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_1(x): 
	if (x / 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_2(x): 
	if (x % 3 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_3(x): 
	if (x % 2 != 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_4(x): 
	if (x % 2 == 1): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_5(x): 
	if (x % 2 == 0): 
		return True
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_6(x): 
	if (x % 2 == 0): 
		return False
	if (x != 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_7(x): 
	if (x % 2 == 0): 
		return False
	if (x == 2): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_8(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return False
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_9(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = None 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_10(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x - 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_11(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 2 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_12(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = None
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_13(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 1
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_14(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x / 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_15(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 3 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_16(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 != 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_17(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 1): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_18(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = None
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_19(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x * 2
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_20(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/3
		p = p + 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_21(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = None
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_22(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p - 1
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_23(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 2
		if (p == x): 
			return True
	return False
def x_is_woodall__mutmut_24(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p != x): 
			return True
	return False
def x_is_woodall__mutmut_25(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return False
	return False
def x_is_woodall__mutmut_26(x): 
	if (x % 2 == 0): 
		return False
	if (x == 1): 
		return True
	x = x + 1 
	p = 0
	while (x % 2 == 0): 
		x = x/2
		p = p + 1
		if (p == x): 
			return True
	return True

x_is_woodall__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_woodall__mutmut_1': x_is_woodall__mutmut_1, 
    'x_is_woodall__mutmut_2': x_is_woodall__mutmut_2, 
    'x_is_woodall__mutmut_3': x_is_woodall__mutmut_3, 
    'x_is_woodall__mutmut_4': x_is_woodall__mutmut_4, 
    'x_is_woodall__mutmut_5': x_is_woodall__mutmut_5, 
    'x_is_woodall__mutmut_6': x_is_woodall__mutmut_6, 
    'x_is_woodall__mutmut_7': x_is_woodall__mutmut_7, 
    'x_is_woodall__mutmut_8': x_is_woodall__mutmut_8, 
    'x_is_woodall__mutmut_9': x_is_woodall__mutmut_9, 
    'x_is_woodall__mutmut_10': x_is_woodall__mutmut_10, 
    'x_is_woodall__mutmut_11': x_is_woodall__mutmut_11, 
    'x_is_woodall__mutmut_12': x_is_woodall__mutmut_12, 
    'x_is_woodall__mutmut_13': x_is_woodall__mutmut_13, 
    'x_is_woodall__mutmut_14': x_is_woodall__mutmut_14, 
    'x_is_woodall__mutmut_15': x_is_woodall__mutmut_15, 
    'x_is_woodall__mutmut_16': x_is_woodall__mutmut_16, 
    'x_is_woodall__mutmut_17': x_is_woodall__mutmut_17, 
    'x_is_woodall__mutmut_18': x_is_woodall__mutmut_18, 
    'x_is_woodall__mutmut_19': x_is_woodall__mutmut_19, 
    'x_is_woodall__mutmut_20': x_is_woodall__mutmut_20, 
    'x_is_woodall__mutmut_21': x_is_woodall__mutmut_21, 
    'x_is_woodall__mutmut_22': x_is_woodall__mutmut_22, 
    'x_is_woodall__mutmut_23': x_is_woodall__mutmut_23, 
    'x_is_woodall__mutmut_24': x_is_woodall__mutmut_24, 
    'x_is_woodall__mutmut_25': x_is_woodall__mutmut_25, 
    'x_is_woodall__mutmut_26': x_is_woodall__mutmut_26
}

def is_woodall(*args, **kwargs):
	result = _mutmut_trampoline(x_is_woodall__mutmut_orig, x_is_woodall__mutmut_mutants, args, kwargs)
	return result 

is_woodall.__signature__ = _mutmut_signature(x_is_woodall__mutmut_orig)
x_is_woodall__mutmut_orig.__name__ = 'x_is_woodall'