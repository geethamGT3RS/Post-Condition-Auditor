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
def x_sequence__mutmut_orig(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_1(n): 
	if n == 1 and n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_2(n): 
	if n != 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_3(n): 
	if n == 2 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_4(n): 
	if n == 1 or n != 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_5(n): 
	if n == 1 or n == 3: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_6(n): 
	if n == 1 or n == 2: 
		return 2
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_7(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) - sequence(n-sequence(n-1))
def x_sequence__mutmut_8(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(None) + sequence(n-sequence(n-1))
def x_sequence__mutmut_9(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(None)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_10(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n + 1)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_11(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-2)) + sequence(n-sequence(n-1))
def x_sequence__mutmut_12(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(None)
def x_sequence__mutmut_13(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n + sequence(n-1))
def x_sequence__mutmut_14(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(None))
def x_sequence__mutmut_15(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n + 1))
def x_sequence__mutmut_16(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-2))

x_sequence__mutmut_mutants : ClassVar[MutantDict] = {
'x_sequence__mutmut_1': x_sequence__mutmut_1, 
    'x_sequence__mutmut_2': x_sequence__mutmut_2, 
    'x_sequence__mutmut_3': x_sequence__mutmut_3, 
    'x_sequence__mutmut_4': x_sequence__mutmut_4, 
    'x_sequence__mutmut_5': x_sequence__mutmut_5, 
    'x_sequence__mutmut_6': x_sequence__mutmut_6, 
    'x_sequence__mutmut_7': x_sequence__mutmut_7, 
    'x_sequence__mutmut_8': x_sequence__mutmut_8, 
    'x_sequence__mutmut_9': x_sequence__mutmut_9, 
    'x_sequence__mutmut_10': x_sequence__mutmut_10, 
    'x_sequence__mutmut_11': x_sequence__mutmut_11, 
    'x_sequence__mutmut_12': x_sequence__mutmut_12, 
    'x_sequence__mutmut_13': x_sequence__mutmut_13, 
    'x_sequence__mutmut_14': x_sequence__mutmut_14, 
    'x_sequence__mutmut_15': x_sequence__mutmut_15, 
    'x_sequence__mutmut_16': x_sequence__mutmut_16
}

def sequence(*args, **kwargs):
	result = _mutmut_trampoline(x_sequence__mutmut_orig, x_sequence__mutmut_mutants, args, kwargs)
	return result 

sequence.__signature__ = _mutmut_signature(x_sequence__mutmut_orig)
x_sequence__mutmut_orig.__name__ = 'x_sequence'