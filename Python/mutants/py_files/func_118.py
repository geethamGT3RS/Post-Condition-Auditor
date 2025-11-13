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
def x_get_total_number_of_sequences__mutmut_orig(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_1(m,n): 
	T=None 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_2(m,n): 
	T=[[1 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_3(m,n): 
	T=[[0 for i in range(None)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_4(m,n): 
	T=[[0 for i in range(n - 1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_5(m,n): 
	T=[[0 for i in range(n+2)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_6(m,n): 
	T=[[0 for i in range(n+1)] for i in range(None)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_7(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m - 1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_8(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+2)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_9(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(None): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_10(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m - 1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_11(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+2): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_12(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(None): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_13(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n - 1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_14(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+2): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_15(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 and j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_16(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i != 0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_17(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==1 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_18(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j != 0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_19(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==1: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_20(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=None
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_21(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=1
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_22(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i <= j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_23(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=None
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_24(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=1
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_25(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j != 1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_26(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==2: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_27(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=None 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_28(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=None 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_29(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j] - T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_30(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i + 1][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_31(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-2][j]+T[i//2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_32(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i / 2][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_33(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//3][j-1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_34(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j + 1] 
	return T[m][n]
def x_get_total_number_of_sequences__mutmut_35(m,n): 
	T=[[0 for i in range(n+1)] for i in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i==0 or j==0: 
				T[i][j]=0
			elif i<j: 
				T[i][j]=0
			elif j==1: 
				T[i][j]=i 
			else: 
				T[i][j]=T[i-1][j]+T[i//2][j-2] 
	return T[m][n]

x_get_total_number_of_sequences__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_total_number_of_sequences__mutmut_1': x_get_total_number_of_sequences__mutmut_1, 
    'x_get_total_number_of_sequences__mutmut_2': x_get_total_number_of_sequences__mutmut_2, 
    'x_get_total_number_of_sequences__mutmut_3': x_get_total_number_of_sequences__mutmut_3, 
    'x_get_total_number_of_sequences__mutmut_4': x_get_total_number_of_sequences__mutmut_4, 
    'x_get_total_number_of_sequences__mutmut_5': x_get_total_number_of_sequences__mutmut_5, 
    'x_get_total_number_of_sequences__mutmut_6': x_get_total_number_of_sequences__mutmut_6, 
    'x_get_total_number_of_sequences__mutmut_7': x_get_total_number_of_sequences__mutmut_7, 
    'x_get_total_number_of_sequences__mutmut_8': x_get_total_number_of_sequences__mutmut_8, 
    'x_get_total_number_of_sequences__mutmut_9': x_get_total_number_of_sequences__mutmut_9, 
    'x_get_total_number_of_sequences__mutmut_10': x_get_total_number_of_sequences__mutmut_10, 
    'x_get_total_number_of_sequences__mutmut_11': x_get_total_number_of_sequences__mutmut_11, 
    'x_get_total_number_of_sequences__mutmut_12': x_get_total_number_of_sequences__mutmut_12, 
    'x_get_total_number_of_sequences__mutmut_13': x_get_total_number_of_sequences__mutmut_13, 
    'x_get_total_number_of_sequences__mutmut_14': x_get_total_number_of_sequences__mutmut_14, 
    'x_get_total_number_of_sequences__mutmut_15': x_get_total_number_of_sequences__mutmut_15, 
    'x_get_total_number_of_sequences__mutmut_16': x_get_total_number_of_sequences__mutmut_16, 
    'x_get_total_number_of_sequences__mutmut_17': x_get_total_number_of_sequences__mutmut_17, 
    'x_get_total_number_of_sequences__mutmut_18': x_get_total_number_of_sequences__mutmut_18, 
    'x_get_total_number_of_sequences__mutmut_19': x_get_total_number_of_sequences__mutmut_19, 
    'x_get_total_number_of_sequences__mutmut_20': x_get_total_number_of_sequences__mutmut_20, 
    'x_get_total_number_of_sequences__mutmut_21': x_get_total_number_of_sequences__mutmut_21, 
    'x_get_total_number_of_sequences__mutmut_22': x_get_total_number_of_sequences__mutmut_22, 
    'x_get_total_number_of_sequences__mutmut_23': x_get_total_number_of_sequences__mutmut_23, 
    'x_get_total_number_of_sequences__mutmut_24': x_get_total_number_of_sequences__mutmut_24, 
    'x_get_total_number_of_sequences__mutmut_25': x_get_total_number_of_sequences__mutmut_25, 
    'x_get_total_number_of_sequences__mutmut_26': x_get_total_number_of_sequences__mutmut_26, 
    'x_get_total_number_of_sequences__mutmut_27': x_get_total_number_of_sequences__mutmut_27, 
    'x_get_total_number_of_sequences__mutmut_28': x_get_total_number_of_sequences__mutmut_28, 
    'x_get_total_number_of_sequences__mutmut_29': x_get_total_number_of_sequences__mutmut_29, 
    'x_get_total_number_of_sequences__mutmut_30': x_get_total_number_of_sequences__mutmut_30, 
    'x_get_total_number_of_sequences__mutmut_31': x_get_total_number_of_sequences__mutmut_31, 
    'x_get_total_number_of_sequences__mutmut_32': x_get_total_number_of_sequences__mutmut_32, 
    'x_get_total_number_of_sequences__mutmut_33': x_get_total_number_of_sequences__mutmut_33, 
    'x_get_total_number_of_sequences__mutmut_34': x_get_total_number_of_sequences__mutmut_34, 
    'x_get_total_number_of_sequences__mutmut_35': x_get_total_number_of_sequences__mutmut_35
}

def get_total_number_of_sequences(*args, **kwargs):
	result = _mutmut_trampoline(x_get_total_number_of_sequences__mutmut_orig, x_get_total_number_of_sequences__mutmut_mutants, args, kwargs)
	return result 

get_total_number_of_sequences.__signature__ = _mutmut_signature(x_get_total_number_of_sequences__mutmut_orig)
x_get_total_number_of_sequences__mutmut_orig.__name__ = 'x_get_total_number_of_sequences'