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
def x_lps__mutmut_orig(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_1(str): 
	n = None 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_2(str): 
	n = len(str) 
	L = None 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_3(str): 
	n = len(str) 
	L = [[1 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_4(str): 
	n = len(str) 
	L = [[0 for x in range(None)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_5(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(None)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_6(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(None): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_7(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = None
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_8(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 2
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_9(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(None, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_10(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, None): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_11(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_12(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, ): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_13(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(3, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_14(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n - 1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_15(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+2): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_16(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(None): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_17(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl - 1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_18(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n + cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_19(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+2): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_20(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = None
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_21(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl + 1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_22(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i - cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_23(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-2
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_24(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] or cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_25(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] != str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_26(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl != 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_27(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 3: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_28(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = None
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_29(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 3
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_30(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] != str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_31(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = None
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_32(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] - 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_33(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i - 1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_34(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+2][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_35(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j + 1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_36(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-2] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_37(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 3
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_38(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = None; 
	return L[0][n-1]
def x_lps__mutmut_39(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(None, L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_40(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], None); 
	return L[0][n-1]
def x_lps__mutmut_41(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_42(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], ); 
	return L[0][n-1]
def x_lps__mutmut_43(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j + 1], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_44(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-2], L[i+1][j]); 
	return L[0][n-1]
def x_lps__mutmut_45(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i - 1][j]); 
	return L[0][n-1]
def x_lps__mutmut_46(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+2][j]); 
	return L[0][n-1]
def x_lps__mutmut_47(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[1][n-1]
def x_lps__mutmut_48(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n + 1]
def x_lps__mutmut_49(str): 
	n = len(str) 
	L = [[0 for x in range(n)] for x in range(n)] 
	for i in range(n): 
		L[i][i] = 1
	for cl in range(2, n+1): 
		for i in range(n-cl+1): 
			j = i+cl-1
			if str[i] == str[j] and cl == 2: 
				L[i][j] = 2
			elif str[i] == str[j]: 
				L[i][j] = L[i+1][j-1] + 2
			else: 
				L[i][j] = max(L[i][j-1], L[i+1][j]); 
	return L[0][n-2]

x_lps__mutmut_mutants : ClassVar[MutantDict] = {
'x_lps__mutmut_1': x_lps__mutmut_1, 
    'x_lps__mutmut_2': x_lps__mutmut_2, 
    'x_lps__mutmut_3': x_lps__mutmut_3, 
    'x_lps__mutmut_4': x_lps__mutmut_4, 
    'x_lps__mutmut_5': x_lps__mutmut_5, 
    'x_lps__mutmut_6': x_lps__mutmut_6, 
    'x_lps__mutmut_7': x_lps__mutmut_7, 
    'x_lps__mutmut_8': x_lps__mutmut_8, 
    'x_lps__mutmut_9': x_lps__mutmut_9, 
    'x_lps__mutmut_10': x_lps__mutmut_10, 
    'x_lps__mutmut_11': x_lps__mutmut_11, 
    'x_lps__mutmut_12': x_lps__mutmut_12, 
    'x_lps__mutmut_13': x_lps__mutmut_13, 
    'x_lps__mutmut_14': x_lps__mutmut_14, 
    'x_lps__mutmut_15': x_lps__mutmut_15, 
    'x_lps__mutmut_16': x_lps__mutmut_16, 
    'x_lps__mutmut_17': x_lps__mutmut_17, 
    'x_lps__mutmut_18': x_lps__mutmut_18, 
    'x_lps__mutmut_19': x_lps__mutmut_19, 
    'x_lps__mutmut_20': x_lps__mutmut_20, 
    'x_lps__mutmut_21': x_lps__mutmut_21, 
    'x_lps__mutmut_22': x_lps__mutmut_22, 
    'x_lps__mutmut_23': x_lps__mutmut_23, 
    'x_lps__mutmut_24': x_lps__mutmut_24, 
    'x_lps__mutmut_25': x_lps__mutmut_25, 
    'x_lps__mutmut_26': x_lps__mutmut_26, 
    'x_lps__mutmut_27': x_lps__mutmut_27, 
    'x_lps__mutmut_28': x_lps__mutmut_28, 
    'x_lps__mutmut_29': x_lps__mutmut_29, 
    'x_lps__mutmut_30': x_lps__mutmut_30, 
    'x_lps__mutmut_31': x_lps__mutmut_31, 
    'x_lps__mutmut_32': x_lps__mutmut_32, 
    'x_lps__mutmut_33': x_lps__mutmut_33, 
    'x_lps__mutmut_34': x_lps__mutmut_34, 
    'x_lps__mutmut_35': x_lps__mutmut_35, 
    'x_lps__mutmut_36': x_lps__mutmut_36, 
    'x_lps__mutmut_37': x_lps__mutmut_37, 
    'x_lps__mutmut_38': x_lps__mutmut_38, 
    'x_lps__mutmut_39': x_lps__mutmut_39, 
    'x_lps__mutmut_40': x_lps__mutmut_40, 
    'x_lps__mutmut_41': x_lps__mutmut_41, 
    'x_lps__mutmut_42': x_lps__mutmut_42, 
    'x_lps__mutmut_43': x_lps__mutmut_43, 
    'x_lps__mutmut_44': x_lps__mutmut_44, 
    'x_lps__mutmut_45': x_lps__mutmut_45, 
    'x_lps__mutmut_46': x_lps__mutmut_46, 
    'x_lps__mutmut_47': x_lps__mutmut_47, 
    'x_lps__mutmut_48': x_lps__mutmut_48, 
    'x_lps__mutmut_49': x_lps__mutmut_49
}

def lps(*args, **kwargs):
	result = _mutmut_trampoline(x_lps__mutmut_orig, x_lps__mutmut_mutants, args, kwargs)
	return result 

lps.__signature__ = _mutmut_signature(x_lps__mutmut_orig)
x_lps__mutmut_orig.__name__ = 'x_lps'