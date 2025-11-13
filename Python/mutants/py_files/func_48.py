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
def x_power__mutmut_orig(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_1(a,b):
	if b != 0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_2(a,b):
	if b==1:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_3(a,b):
	if b==0:
		return 2
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_4(a,b):
	if b==0:
		return 1
	elif a != 0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_5(a,b):
	if b==0:
		return 1
	elif a==1:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_6(a,b):
	if b==0:
		return 1
	elif a==0:
		return 1
	elif b==1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_7(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b != 1:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_8(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==2:
		return a
	else:
		return a*power(a,b-1)
def x_power__mutmut_9(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a / power(a,b-1)
def x_power__mutmut_10(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(None,b-1)
def x_power__mutmut_11(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,None)
def x_power__mutmut_12(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(b-1)
def x_power__mutmut_13(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,)
def x_power__mutmut_14(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b + 1)
def x_power__mutmut_15(a,b):
	if b==0:
		return 1
	elif a==0:
		return 0
	elif b==1:
		return a
	else:
		return a*power(a,b-2)

x_power__mutmut_mutants : ClassVar[MutantDict] = {
'x_power__mutmut_1': x_power__mutmut_1, 
    'x_power__mutmut_2': x_power__mutmut_2, 
    'x_power__mutmut_3': x_power__mutmut_3, 
    'x_power__mutmut_4': x_power__mutmut_4, 
    'x_power__mutmut_5': x_power__mutmut_5, 
    'x_power__mutmut_6': x_power__mutmut_6, 
    'x_power__mutmut_7': x_power__mutmut_7, 
    'x_power__mutmut_8': x_power__mutmut_8, 
    'x_power__mutmut_9': x_power__mutmut_9, 
    'x_power__mutmut_10': x_power__mutmut_10, 
    'x_power__mutmut_11': x_power__mutmut_11, 
    'x_power__mutmut_12': x_power__mutmut_12, 
    'x_power__mutmut_13': x_power__mutmut_13, 
    'x_power__mutmut_14': x_power__mutmut_14, 
    'x_power__mutmut_15': x_power__mutmut_15
}

def power(*args, **kwargs):
	result = _mutmut_trampoline(x_power__mutmut_orig, x_power__mutmut_mutants, args, kwargs)
	return result 

power.__signature__ = _mutmut_signature(x_power__mutmut_orig)
x_power__mutmut_orig.__name__ = 'x_power'