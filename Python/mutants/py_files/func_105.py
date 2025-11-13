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
def x_is_majority__mutmut_orig(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_1(arr, n, x):
	i = None
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_2(arr, n, x):
	i = binary_search(None, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_3(arr, n, x):
	i = binary_search(arr, None, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_4(arr, n, x):
	i = binary_search(arr, 0, None, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_5(arr, n, x):
	i = binary_search(arr, 0, n-1, None)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_6(arr, n, x):
	i = binary_search(0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_7(arr, n, x):
	i = binary_search(arr, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_8(arr, n, x):
	i = binary_search(arr, 0, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_9(arr, n, x):
	i = binary_search(arr, 0, n-1, )
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_10(arr, n, x):
	i = binary_search(arr, 1, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_11(arr, n, x):
	i = binary_search(arr, 0, n + 1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_12(arr, n, x):
	i = binary_search(arr, 0, n-2, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_13(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i != -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_14(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == +1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_15(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -2:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_16(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return True
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_17(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) or arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_18(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i - n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_19(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n / 2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_20(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//3) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_21(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) < (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_22(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n + 1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_23(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -2)) and arr[i + n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_24(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i - n//2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_25(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n / 2] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_26(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//3] == x:
		return True
	else:
		return False
def x_is_majority__mutmut_27(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] != x:
		return True
	else:
		return False
def x_is_majority__mutmut_28(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return False
	else:
		return False
def x_is_majority__mutmut_29(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return True

x_is_majority__mutmut_mutants : ClassVar[MutantDict] = {
'x_is_majority__mutmut_1': x_is_majority__mutmut_1, 
    'x_is_majority__mutmut_2': x_is_majority__mutmut_2, 
    'x_is_majority__mutmut_3': x_is_majority__mutmut_3, 
    'x_is_majority__mutmut_4': x_is_majority__mutmut_4, 
    'x_is_majority__mutmut_5': x_is_majority__mutmut_5, 
    'x_is_majority__mutmut_6': x_is_majority__mutmut_6, 
    'x_is_majority__mutmut_7': x_is_majority__mutmut_7, 
    'x_is_majority__mutmut_8': x_is_majority__mutmut_8, 
    'x_is_majority__mutmut_9': x_is_majority__mutmut_9, 
    'x_is_majority__mutmut_10': x_is_majority__mutmut_10, 
    'x_is_majority__mutmut_11': x_is_majority__mutmut_11, 
    'x_is_majority__mutmut_12': x_is_majority__mutmut_12, 
    'x_is_majority__mutmut_13': x_is_majority__mutmut_13, 
    'x_is_majority__mutmut_14': x_is_majority__mutmut_14, 
    'x_is_majority__mutmut_15': x_is_majority__mutmut_15, 
    'x_is_majority__mutmut_16': x_is_majority__mutmut_16, 
    'x_is_majority__mutmut_17': x_is_majority__mutmut_17, 
    'x_is_majority__mutmut_18': x_is_majority__mutmut_18, 
    'x_is_majority__mutmut_19': x_is_majority__mutmut_19, 
    'x_is_majority__mutmut_20': x_is_majority__mutmut_20, 
    'x_is_majority__mutmut_21': x_is_majority__mutmut_21, 
    'x_is_majority__mutmut_22': x_is_majority__mutmut_22, 
    'x_is_majority__mutmut_23': x_is_majority__mutmut_23, 
    'x_is_majority__mutmut_24': x_is_majority__mutmut_24, 
    'x_is_majority__mutmut_25': x_is_majority__mutmut_25, 
    'x_is_majority__mutmut_26': x_is_majority__mutmut_26, 
    'x_is_majority__mutmut_27': x_is_majority__mutmut_27, 
    'x_is_majority__mutmut_28': x_is_majority__mutmut_28, 
    'x_is_majority__mutmut_29': x_is_majority__mutmut_29
}

def is_majority(*args, **kwargs):
	result = _mutmut_trampoline(x_is_majority__mutmut_orig, x_is_majority__mutmut_mutants, args, kwargs)
	return result 

is_majority.__signature__ = _mutmut_signature(x_is_majority__mutmut_orig)
x_is_majority__mutmut_orig.__name__ = 'x_is_majority'
def x_binary_search__mutmut_orig(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_1(arr, low, high, x):
	if high > low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_2(arr, low, high, x):
	if high >= low:
		mid = None 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_3(arr, low, high, x):
	if high >= low:
		mid = (low + high) / 2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_4(arr, low, high, x):
	if high >= low:
		mid = (low - high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_5(arr, low, high, x):
	if high >= low:
		mid = (low + high)//3 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_6(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) or (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_7(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 and x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_8(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid != 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_9(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 1 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_10(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x >= arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_11(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid + 1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_12(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-2]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_13(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] != x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_14(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x >= arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_15(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(None, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_16(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, None, high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_17(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), None, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_18(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, None)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_19(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search((mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_20(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_21(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_22(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, )
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_23(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid - 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_24(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 2), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_25(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(None, low, (mid -1), x)
	return -1
def x_binary_search__mutmut_26(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, None, (mid -1), x)
	return -1
def x_binary_search__mutmut_27(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, None, x)
	return -1
def x_binary_search__mutmut_28(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), None)
	return -1
def x_binary_search__mutmut_29(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(low, (mid -1), x)
	return -1
def x_binary_search__mutmut_30(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, (mid -1), x)
	return -1
def x_binary_search__mutmut_31(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, x)
	return -1
def x_binary_search__mutmut_32(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), )
	return -1
def x_binary_search__mutmut_33(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid + 1), x)
	return -1
def x_binary_search__mutmut_34(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -2), x)
	return -1
def x_binary_search__mutmut_35(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return +1
def x_binary_search__mutmut_36(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -2

x_binary_search__mutmut_mutants : ClassVar[MutantDict] = {
'x_binary_search__mutmut_1': x_binary_search__mutmut_1, 
    'x_binary_search__mutmut_2': x_binary_search__mutmut_2, 
    'x_binary_search__mutmut_3': x_binary_search__mutmut_3, 
    'x_binary_search__mutmut_4': x_binary_search__mutmut_4, 
    'x_binary_search__mutmut_5': x_binary_search__mutmut_5, 
    'x_binary_search__mutmut_6': x_binary_search__mutmut_6, 
    'x_binary_search__mutmut_7': x_binary_search__mutmut_7, 
    'x_binary_search__mutmut_8': x_binary_search__mutmut_8, 
    'x_binary_search__mutmut_9': x_binary_search__mutmut_9, 
    'x_binary_search__mutmut_10': x_binary_search__mutmut_10, 
    'x_binary_search__mutmut_11': x_binary_search__mutmut_11, 
    'x_binary_search__mutmut_12': x_binary_search__mutmut_12, 
    'x_binary_search__mutmut_13': x_binary_search__mutmut_13, 
    'x_binary_search__mutmut_14': x_binary_search__mutmut_14, 
    'x_binary_search__mutmut_15': x_binary_search__mutmut_15, 
    'x_binary_search__mutmut_16': x_binary_search__mutmut_16, 
    'x_binary_search__mutmut_17': x_binary_search__mutmut_17, 
    'x_binary_search__mutmut_18': x_binary_search__mutmut_18, 
    'x_binary_search__mutmut_19': x_binary_search__mutmut_19, 
    'x_binary_search__mutmut_20': x_binary_search__mutmut_20, 
    'x_binary_search__mutmut_21': x_binary_search__mutmut_21, 
    'x_binary_search__mutmut_22': x_binary_search__mutmut_22, 
    'x_binary_search__mutmut_23': x_binary_search__mutmut_23, 
    'x_binary_search__mutmut_24': x_binary_search__mutmut_24, 
    'x_binary_search__mutmut_25': x_binary_search__mutmut_25, 
    'x_binary_search__mutmut_26': x_binary_search__mutmut_26, 
    'x_binary_search__mutmut_27': x_binary_search__mutmut_27, 
    'x_binary_search__mutmut_28': x_binary_search__mutmut_28, 
    'x_binary_search__mutmut_29': x_binary_search__mutmut_29, 
    'x_binary_search__mutmut_30': x_binary_search__mutmut_30, 
    'x_binary_search__mutmut_31': x_binary_search__mutmut_31, 
    'x_binary_search__mutmut_32': x_binary_search__mutmut_32, 
    'x_binary_search__mutmut_33': x_binary_search__mutmut_33, 
    'x_binary_search__mutmut_34': x_binary_search__mutmut_34, 
    'x_binary_search__mutmut_35': x_binary_search__mutmut_35, 
    'x_binary_search__mutmut_36': x_binary_search__mutmut_36
}

def binary_search(*args, **kwargs):
	result = _mutmut_trampoline(x_binary_search__mutmut_orig, x_binary_search__mutmut_mutants, args, kwargs)
	return result 

binary_search.__signature__ = _mutmut_signature(x_binary_search__mutmut_orig)
x_binary_search__mutmut_orig.__name__ = 'x_binary_search'