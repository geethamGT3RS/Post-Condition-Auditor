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
def x_get_max_sum__mutmut_orig (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_1 (n):
	res = None
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_2 (n):
	res = list()
	res.append(None)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_3 (n):
	res = list()
	res.append(1)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_4 (n):
	res = list()
	res.append(0)
	res.append(None)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_5 (n):
	res = list()
	res.append(0)
	res.append(2)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_6 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = None
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_7 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 3
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_8 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i <= n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_9 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n - 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_10 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 2:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_11 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(None)
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_12 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(None, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_13 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, None))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_14 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max((res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_15 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, ))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_16 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)] - res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_17 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] - res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_18 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] - res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_19 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(None)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_20 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i * 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_21 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 3)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_22 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(None)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_23 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i * 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_24 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 4)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_25 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(None)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_26 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i * 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_27 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 5)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_28 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(None)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_29 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i * 5)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_30 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 6)])))
		i = i + 1
	return res[n]
def x_get_max_sum__mutmut_31 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = None
	return res[n]
def x_get_max_sum__mutmut_32 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i - 1
	return res[n]
def x_get_max_sum__mutmut_33 (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 2
	return res[n]

x_get_max_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_max_sum__mutmut_1': x_get_max_sum__mutmut_1, 
    'x_get_max_sum__mutmut_2': x_get_max_sum__mutmut_2, 
    'x_get_max_sum__mutmut_3': x_get_max_sum__mutmut_3, 
    'x_get_max_sum__mutmut_4': x_get_max_sum__mutmut_4, 
    'x_get_max_sum__mutmut_5': x_get_max_sum__mutmut_5, 
    'x_get_max_sum__mutmut_6': x_get_max_sum__mutmut_6, 
    'x_get_max_sum__mutmut_7': x_get_max_sum__mutmut_7, 
    'x_get_max_sum__mutmut_8': x_get_max_sum__mutmut_8, 
    'x_get_max_sum__mutmut_9': x_get_max_sum__mutmut_9, 
    'x_get_max_sum__mutmut_10': x_get_max_sum__mutmut_10, 
    'x_get_max_sum__mutmut_11': x_get_max_sum__mutmut_11, 
    'x_get_max_sum__mutmut_12': x_get_max_sum__mutmut_12, 
    'x_get_max_sum__mutmut_13': x_get_max_sum__mutmut_13, 
    'x_get_max_sum__mutmut_14': x_get_max_sum__mutmut_14, 
    'x_get_max_sum__mutmut_15': x_get_max_sum__mutmut_15, 
    'x_get_max_sum__mutmut_16': x_get_max_sum__mutmut_16, 
    'x_get_max_sum__mutmut_17': x_get_max_sum__mutmut_17, 
    'x_get_max_sum__mutmut_18': x_get_max_sum__mutmut_18, 
    'x_get_max_sum__mutmut_19': x_get_max_sum__mutmut_19, 
    'x_get_max_sum__mutmut_20': x_get_max_sum__mutmut_20, 
    'x_get_max_sum__mutmut_21': x_get_max_sum__mutmut_21, 
    'x_get_max_sum__mutmut_22': x_get_max_sum__mutmut_22, 
    'x_get_max_sum__mutmut_23': x_get_max_sum__mutmut_23, 
    'x_get_max_sum__mutmut_24': x_get_max_sum__mutmut_24, 
    'x_get_max_sum__mutmut_25': x_get_max_sum__mutmut_25, 
    'x_get_max_sum__mutmut_26': x_get_max_sum__mutmut_26, 
    'x_get_max_sum__mutmut_27': x_get_max_sum__mutmut_27, 
    'x_get_max_sum__mutmut_28': x_get_max_sum__mutmut_28, 
    'x_get_max_sum__mutmut_29': x_get_max_sum__mutmut_29, 
    'x_get_max_sum__mutmut_30': x_get_max_sum__mutmut_30, 
    'x_get_max_sum__mutmut_31': x_get_max_sum__mutmut_31, 
    'x_get_max_sum__mutmut_32': x_get_max_sum__mutmut_32, 
    'x_get_max_sum__mutmut_33': x_get_max_sum__mutmut_33
}

def get_max_sum(*args, **kwargs):
	result = _mutmut_trampoline(x_get_max_sum__mutmut_orig, x_get_max_sum__mutmut_mutants, args, kwargs)
	return result 

get_max_sum.__signature__ = _mutmut_signature(x_get_max_sum__mutmut_orig)
x_get_max_sum__mutmut_orig.__name__ = 'x_get_max_sum'