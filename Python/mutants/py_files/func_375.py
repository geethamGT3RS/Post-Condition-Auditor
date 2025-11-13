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
def x_jacobsthal_num__mutmut_orig(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_1(n): 
	dp = None 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_2(n): 
	dp = [0] / (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_3(n): 
	dp = [1] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_4(n): 
	dp = [0] * (n - 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_5(n): 
	dp = [0] * (n + 2) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_6(n): 
	dp = [0] * (n + 1) 
	dp[0] = None
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_7(n): 
	dp = [0] * (n + 1) 
	dp[1] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_8(n): 
	dp = [0] * (n + 1) 
	dp[0] = 1
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_9(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = None
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_10(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[2] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_11(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 2
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_12(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(None, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_13(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, None): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_14(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_15(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, ): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_16(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(3, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_17(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n - 1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_18(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+2): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_19(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = None 
	return dp[n]
def x_jacobsthal_num__mutmut_20(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] - 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_21(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i + 1] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_22(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 2] + 2 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_23(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 / dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_24(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 3 * dp[i - 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_25(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i + 2] 
	return dp[n]
def x_jacobsthal_num__mutmut_26(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 3] 
	return dp[n]

x_jacobsthal_num__mutmut_mutants : ClassVar[MutantDict] = {
'x_jacobsthal_num__mutmut_1': x_jacobsthal_num__mutmut_1, 
    'x_jacobsthal_num__mutmut_2': x_jacobsthal_num__mutmut_2, 
    'x_jacobsthal_num__mutmut_3': x_jacobsthal_num__mutmut_3, 
    'x_jacobsthal_num__mutmut_4': x_jacobsthal_num__mutmut_4, 
    'x_jacobsthal_num__mutmut_5': x_jacobsthal_num__mutmut_5, 
    'x_jacobsthal_num__mutmut_6': x_jacobsthal_num__mutmut_6, 
    'x_jacobsthal_num__mutmut_7': x_jacobsthal_num__mutmut_7, 
    'x_jacobsthal_num__mutmut_8': x_jacobsthal_num__mutmut_8, 
    'x_jacobsthal_num__mutmut_9': x_jacobsthal_num__mutmut_9, 
    'x_jacobsthal_num__mutmut_10': x_jacobsthal_num__mutmut_10, 
    'x_jacobsthal_num__mutmut_11': x_jacobsthal_num__mutmut_11, 
    'x_jacobsthal_num__mutmut_12': x_jacobsthal_num__mutmut_12, 
    'x_jacobsthal_num__mutmut_13': x_jacobsthal_num__mutmut_13, 
    'x_jacobsthal_num__mutmut_14': x_jacobsthal_num__mutmut_14, 
    'x_jacobsthal_num__mutmut_15': x_jacobsthal_num__mutmut_15, 
    'x_jacobsthal_num__mutmut_16': x_jacobsthal_num__mutmut_16, 
    'x_jacobsthal_num__mutmut_17': x_jacobsthal_num__mutmut_17, 
    'x_jacobsthal_num__mutmut_18': x_jacobsthal_num__mutmut_18, 
    'x_jacobsthal_num__mutmut_19': x_jacobsthal_num__mutmut_19, 
    'x_jacobsthal_num__mutmut_20': x_jacobsthal_num__mutmut_20, 
    'x_jacobsthal_num__mutmut_21': x_jacobsthal_num__mutmut_21, 
    'x_jacobsthal_num__mutmut_22': x_jacobsthal_num__mutmut_22, 
    'x_jacobsthal_num__mutmut_23': x_jacobsthal_num__mutmut_23, 
    'x_jacobsthal_num__mutmut_24': x_jacobsthal_num__mutmut_24, 
    'x_jacobsthal_num__mutmut_25': x_jacobsthal_num__mutmut_25, 
    'x_jacobsthal_num__mutmut_26': x_jacobsthal_num__mutmut_26
}

def jacobsthal_num(*args, **kwargs):
	result = _mutmut_trampoline(x_jacobsthal_num__mutmut_orig, x_jacobsthal_num__mutmut_mutants, args, kwargs)
	return result 

jacobsthal_num.__signature__ = _mutmut_signature(x_jacobsthal_num__mutmut_orig)
x_jacobsthal_num__mutmut_orig.__name__ = 'x_jacobsthal_num'