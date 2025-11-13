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
def x_count_no_of_ways__mutmut_orig(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_1(n, k): 
	dp = None 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_2(n, k): 
	dp = [0] / (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_3(n, k): 
	dp = [1] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_4(n, k): 
	dp = [0] * (n - 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_5(n, k): 
	dp = [0] * (n + 2) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_6(n, k): 
	dp = [0] * (n + 1) 
	total = None 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_7(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = None
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_8(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000008
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_9(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = None 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_10(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[2] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_11(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = None	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_12(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[3] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_13(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k / k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_14(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(None,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_15(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,None): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_16(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_17(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_18(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(4,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_19(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n - 1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_20(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+2): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_21(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = None 
	return dp[n]
def x_count_no_of_ways__mutmut_22(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) / mod 
	return dp[n]
def x_count_no_of_ways__mutmut_23(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) / (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_24(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k + 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_25(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 2) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_26(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] - dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_27(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i + 1] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_28(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 2] + dp[i - 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_29(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i + 2])) % mod 
	return dp[n]
def x_count_no_of_ways__mutmut_30(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 3])) % mod 
	return dp[n]

x_count_no_of_ways__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_no_of_ways__mutmut_1': x_count_no_of_ways__mutmut_1, 
    'x_count_no_of_ways__mutmut_2': x_count_no_of_ways__mutmut_2, 
    'x_count_no_of_ways__mutmut_3': x_count_no_of_ways__mutmut_3, 
    'x_count_no_of_ways__mutmut_4': x_count_no_of_ways__mutmut_4, 
    'x_count_no_of_ways__mutmut_5': x_count_no_of_ways__mutmut_5, 
    'x_count_no_of_ways__mutmut_6': x_count_no_of_ways__mutmut_6, 
    'x_count_no_of_ways__mutmut_7': x_count_no_of_ways__mutmut_7, 
    'x_count_no_of_ways__mutmut_8': x_count_no_of_ways__mutmut_8, 
    'x_count_no_of_ways__mutmut_9': x_count_no_of_ways__mutmut_9, 
    'x_count_no_of_ways__mutmut_10': x_count_no_of_ways__mutmut_10, 
    'x_count_no_of_ways__mutmut_11': x_count_no_of_ways__mutmut_11, 
    'x_count_no_of_ways__mutmut_12': x_count_no_of_ways__mutmut_12, 
    'x_count_no_of_ways__mutmut_13': x_count_no_of_ways__mutmut_13, 
    'x_count_no_of_ways__mutmut_14': x_count_no_of_ways__mutmut_14, 
    'x_count_no_of_ways__mutmut_15': x_count_no_of_ways__mutmut_15, 
    'x_count_no_of_ways__mutmut_16': x_count_no_of_ways__mutmut_16, 
    'x_count_no_of_ways__mutmut_17': x_count_no_of_ways__mutmut_17, 
    'x_count_no_of_ways__mutmut_18': x_count_no_of_ways__mutmut_18, 
    'x_count_no_of_ways__mutmut_19': x_count_no_of_ways__mutmut_19, 
    'x_count_no_of_ways__mutmut_20': x_count_no_of_ways__mutmut_20, 
    'x_count_no_of_ways__mutmut_21': x_count_no_of_ways__mutmut_21, 
    'x_count_no_of_ways__mutmut_22': x_count_no_of_ways__mutmut_22, 
    'x_count_no_of_ways__mutmut_23': x_count_no_of_ways__mutmut_23, 
    'x_count_no_of_ways__mutmut_24': x_count_no_of_ways__mutmut_24, 
    'x_count_no_of_ways__mutmut_25': x_count_no_of_ways__mutmut_25, 
    'x_count_no_of_ways__mutmut_26': x_count_no_of_ways__mutmut_26, 
    'x_count_no_of_ways__mutmut_27': x_count_no_of_ways__mutmut_27, 
    'x_count_no_of_ways__mutmut_28': x_count_no_of_ways__mutmut_28, 
    'x_count_no_of_ways__mutmut_29': x_count_no_of_ways__mutmut_29, 
    'x_count_no_of_ways__mutmut_30': x_count_no_of_ways__mutmut_30
}

def count_no_of_ways(*args, **kwargs):
	result = _mutmut_trampoline(x_count_no_of_ways__mutmut_orig, x_count_no_of_ways__mutmut_mutants, args, kwargs)
	return result 

count_no_of_ways.__signature__ = _mutmut_signature(x_count_no_of_ways__mutmut_orig)
x_count_no_of_ways__mutmut_orig.__name__ = 'x_count_no_of_ways'