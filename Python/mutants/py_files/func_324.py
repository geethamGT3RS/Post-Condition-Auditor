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
def x_largest_subset__mutmut_orig(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_1(a):
	n = None
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_2(a):
	n = len(a)
	dp = None
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_3(a):
	n = len(a)
	dp = [1 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_4(a):
	n = len(a)
	dp = [0 for i in range(None)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_5(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = None; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_6(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n + 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_7(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 2] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_8(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 2; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_9(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(None, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_10(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, None, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_11(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, None):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_12(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(-1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_13(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_14(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, ):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_15(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n + 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_16(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 3, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_17(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, +1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_18(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -2, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_19(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, +1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_20(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -2):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_21(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = None;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_22(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 1;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_23(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(None, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_24(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, None):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_25(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_26(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, ):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_27(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i - 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_28(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 2, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_29(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 and a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_30(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] / a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_31(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] != 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_32(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 1 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_33(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] / a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_34(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] != 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_35(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 1:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_36(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = None
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_37(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(None, dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_38(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, None)
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_39(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(dp[j])
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_40(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, )
		dp[i] = 1 + mxm
	return max(dp)
def x_largest_subset__mutmut_41(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = None
	return max(dp)
def x_largest_subset__mutmut_42(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 - mxm
	return max(dp)
def x_largest_subset__mutmut_43(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 2 + mxm
	return max(dp)
def x_largest_subset__mutmut_44(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(None)

x_largest_subset__mutmut_mutants : ClassVar[MutantDict] = {
'x_largest_subset__mutmut_1': x_largest_subset__mutmut_1, 
    'x_largest_subset__mutmut_2': x_largest_subset__mutmut_2, 
    'x_largest_subset__mutmut_3': x_largest_subset__mutmut_3, 
    'x_largest_subset__mutmut_4': x_largest_subset__mutmut_4, 
    'x_largest_subset__mutmut_5': x_largest_subset__mutmut_5, 
    'x_largest_subset__mutmut_6': x_largest_subset__mutmut_6, 
    'x_largest_subset__mutmut_7': x_largest_subset__mutmut_7, 
    'x_largest_subset__mutmut_8': x_largest_subset__mutmut_8, 
    'x_largest_subset__mutmut_9': x_largest_subset__mutmut_9, 
    'x_largest_subset__mutmut_10': x_largest_subset__mutmut_10, 
    'x_largest_subset__mutmut_11': x_largest_subset__mutmut_11, 
    'x_largest_subset__mutmut_12': x_largest_subset__mutmut_12, 
    'x_largest_subset__mutmut_13': x_largest_subset__mutmut_13, 
    'x_largest_subset__mutmut_14': x_largest_subset__mutmut_14, 
    'x_largest_subset__mutmut_15': x_largest_subset__mutmut_15, 
    'x_largest_subset__mutmut_16': x_largest_subset__mutmut_16, 
    'x_largest_subset__mutmut_17': x_largest_subset__mutmut_17, 
    'x_largest_subset__mutmut_18': x_largest_subset__mutmut_18, 
    'x_largest_subset__mutmut_19': x_largest_subset__mutmut_19, 
    'x_largest_subset__mutmut_20': x_largest_subset__mutmut_20, 
    'x_largest_subset__mutmut_21': x_largest_subset__mutmut_21, 
    'x_largest_subset__mutmut_22': x_largest_subset__mutmut_22, 
    'x_largest_subset__mutmut_23': x_largest_subset__mutmut_23, 
    'x_largest_subset__mutmut_24': x_largest_subset__mutmut_24, 
    'x_largest_subset__mutmut_25': x_largest_subset__mutmut_25, 
    'x_largest_subset__mutmut_26': x_largest_subset__mutmut_26, 
    'x_largest_subset__mutmut_27': x_largest_subset__mutmut_27, 
    'x_largest_subset__mutmut_28': x_largest_subset__mutmut_28, 
    'x_largest_subset__mutmut_29': x_largest_subset__mutmut_29, 
    'x_largest_subset__mutmut_30': x_largest_subset__mutmut_30, 
    'x_largest_subset__mutmut_31': x_largest_subset__mutmut_31, 
    'x_largest_subset__mutmut_32': x_largest_subset__mutmut_32, 
    'x_largest_subset__mutmut_33': x_largest_subset__mutmut_33, 
    'x_largest_subset__mutmut_34': x_largest_subset__mutmut_34, 
    'x_largest_subset__mutmut_35': x_largest_subset__mutmut_35, 
    'x_largest_subset__mutmut_36': x_largest_subset__mutmut_36, 
    'x_largest_subset__mutmut_37': x_largest_subset__mutmut_37, 
    'x_largest_subset__mutmut_38': x_largest_subset__mutmut_38, 
    'x_largest_subset__mutmut_39': x_largest_subset__mutmut_39, 
    'x_largest_subset__mutmut_40': x_largest_subset__mutmut_40, 
    'x_largest_subset__mutmut_41': x_largest_subset__mutmut_41, 
    'x_largest_subset__mutmut_42': x_largest_subset__mutmut_42, 
    'x_largest_subset__mutmut_43': x_largest_subset__mutmut_43, 
    'x_largest_subset__mutmut_44': x_largest_subset__mutmut_44
}

def largest_subset(*args, **kwargs):
	result = _mutmut_trampoline(x_largest_subset__mutmut_orig, x_largest_subset__mutmut_mutants, args, kwargs)
	return result 

largest_subset.__signature__ = _mutmut_signature(x_largest_subset__mutmut_orig)
x_largest_subset__mutmut_orig.__name__ = 'x_largest_subset'