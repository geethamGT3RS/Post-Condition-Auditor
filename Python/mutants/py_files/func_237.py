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
def x_cal_sum__mutmut_orig(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_1(n): 
	a = None
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_2(n): 
	a = 4
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_3(n): 
	a = 3
	b = None
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_4(n): 
	a = 3
	b = 1
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_5(n): 
	a = 3
	b = 0
	c = None
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_6(n): 
	a = 3
	b = 0
	c = 3
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_7(n): 
	a = 3
	b = 0
	c = 2
	if (n != 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_8(n): 
	a = 3
	b = 0
	c = 2
	if (n == 1): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_9(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 4
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_10(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n != 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_11(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 2): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_12(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 4
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_13(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n != 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_14(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 3): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_15(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 6
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_16(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = None
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_17(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 6
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_18(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n >= 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_19(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 3): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_20(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = None 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_21(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a - b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_22(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = None 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_23(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum - d 
		a = b 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_24(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = None 
		b = c 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_25(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = None 
		c = d 
		n = n-1
	return sum
def x_cal_sum__mutmut_26(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = None 
		n = n-1
	return sum
def x_cal_sum__mutmut_27(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = None
	return sum
def x_cal_sum__mutmut_28(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n + 1
	return sum
def x_cal_sum__mutmut_29(n): 
	a = 3
	b = 0
	c = 2
	if (n == 0): 
		return 3
	if (n == 1): 
		return 3
	if (n == 2): 
		return 5
	sum = 5
	while (n > 2): 
		d = a + b 
		sum = sum + d 
		a = b 
		b = c 
		c = d 
		n = n-2
	return sum

x_cal_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_cal_sum__mutmut_1': x_cal_sum__mutmut_1, 
    'x_cal_sum__mutmut_2': x_cal_sum__mutmut_2, 
    'x_cal_sum__mutmut_3': x_cal_sum__mutmut_3, 
    'x_cal_sum__mutmut_4': x_cal_sum__mutmut_4, 
    'x_cal_sum__mutmut_5': x_cal_sum__mutmut_5, 
    'x_cal_sum__mutmut_6': x_cal_sum__mutmut_6, 
    'x_cal_sum__mutmut_7': x_cal_sum__mutmut_7, 
    'x_cal_sum__mutmut_8': x_cal_sum__mutmut_8, 
    'x_cal_sum__mutmut_9': x_cal_sum__mutmut_9, 
    'x_cal_sum__mutmut_10': x_cal_sum__mutmut_10, 
    'x_cal_sum__mutmut_11': x_cal_sum__mutmut_11, 
    'x_cal_sum__mutmut_12': x_cal_sum__mutmut_12, 
    'x_cal_sum__mutmut_13': x_cal_sum__mutmut_13, 
    'x_cal_sum__mutmut_14': x_cal_sum__mutmut_14, 
    'x_cal_sum__mutmut_15': x_cal_sum__mutmut_15, 
    'x_cal_sum__mutmut_16': x_cal_sum__mutmut_16, 
    'x_cal_sum__mutmut_17': x_cal_sum__mutmut_17, 
    'x_cal_sum__mutmut_18': x_cal_sum__mutmut_18, 
    'x_cal_sum__mutmut_19': x_cal_sum__mutmut_19, 
    'x_cal_sum__mutmut_20': x_cal_sum__mutmut_20, 
    'x_cal_sum__mutmut_21': x_cal_sum__mutmut_21, 
    'x_cal_sum__mutmut_22': x_cal_sum__mutmut_22, 
    'x_cal_sum__mutmut_23': x_cal_sum__mutmut_23, 
    'x_cal_sum__mutmut_24': x_cal_sum__mutmut_24, 
    'x_cal_sum__mutmut_25': x_cal_sum__mutmut_25, 
    'x_cal_sum__mutmut_26': x_cal_sum__mutmut_26, 
    'x_cal_sum__mutmut_27': x_cal_sum__mutmut_27, 
    'x_cal_sum__mutmut_28': x_cal_sum__mutmut_28, 
    'x_cal_sum__mutmut_29': x_cal_sum__mutmut_29
}

def cal_sum(*args, **kwargs):
	result = _mutmut_trampoline(x_cal_sum__mutmut_orig, x_cal_sum__mutmut_mutants, args, kwargs)
	return result 

cal_sum.__signature__ = _mutmut_signature(x_cal_sum__mutmut_orig)
x_cal_sum__mutmut_orig.__name__ = 'x_cal_sum'