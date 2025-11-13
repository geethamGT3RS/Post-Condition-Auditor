NO_OF_CHARS = 256
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
def x_str_to_list__mutmut_orig(string): 
	temp = [] 
	for x in string: 
		temp.append(x) 
	return temp 
def x_str_to_list__mutmut_1(string): 
	temp = None 
	for x in string: 
		temp.append(x) 
	return temp 
def x_str_to_list__mutmut_2(string): 
	temp = [] 
	for x in string: 
		temp.append(None) 
	return temp 

x_str_to_list__mutmut_mutants : ClassVar[MutantDict] = {
'x_str_to_list__mutmut_1': x_str_to_list__mutmut_1, 
    'x_str_to_list__mutmut_2': x_str_to_list__mutmut_2
}

def str_to_list(*args, **kwargs):
	result = _mutmut_trampoline(x_str_to_list__mutmut_orig, x_str_to_list__mutmut_mutants, args, kwargs)
	return result 

str_to_list.__signature__ = _mutmut_signature(x_str_to_list__mutmut_orig)
x_str_to_list__mutmut_orig.__name__ = 'x_str_to_list'
def x_lst_to_string__mutmut_orig(List): 
	return ''.join(List) 
def x_lst_to_string__mutmut_1(List): 
	return ''.join(None) 
def x_lst_to_string__mutmut_2(List): 
	return 'XXXX'.join(List) 

x_lst_to_string__mutmut_mutants : ClassVar[MutantDict] = {
'x_lst_to_string__mutmut_1': x_lst_to_string__mutmut_1, 
    'x_lst_to_string__mutmut_2': x_lst_to_string__mutmut_2
}

def lst_to_string(*args, **kwargs):
	result = _mutmut_trampoline(x_lst_to_string__mutmut_orig, x_lst_to_string__mutmut_mutants, args, kwargs)
	return result 

lst_to_string.__signature__ = _mutmut_signature(x_lst_to_string__mutmut_orig)
x_lst_to_string__mutmut_orig.__name__ = 'x_lst_to_string'
def x_get_char_count_array__mutmut_orig(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def x_get_char_count_array__mutmut_1(string): 
	count = None 
	for i in string: 
		count[ord(i)] += 1
	return count 
def x_get_char_count_array__mutmut_2(string): 
	count = [0] / NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def x_get_char_count_array__mutmut_3(string): 
	count = [1] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 1
	return count 
def x_get_char_count_array__mutmut_4(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] = 1
	return count 
def x_get_char_count_array__mutmut_5(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] -= 1
	return count 
def x_get_char_count_array__mutmut_6(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(None)] += 1
	return count 
def x_get_char_count_array__mutmut_7(string): 
	count = [0] * NO_OF_CHARS 
	for i in string: 
		count[ord(i)] += 2
	return count 

x_get_char_count_array__mutmut_mutants : ClassVar[MutantDict] = {
'x_get_char_count_array__mutmut_1': x_get_char_count_array__mutmut_1, 
    'x_get_char_count_array__mutmut_2': x_get_char_count_array__mutmut_2, 
    'x_get_char_count_array__mutmut_3': x_get_char_count_array__mutmut_3, 
    'x_get_char_count_array__mutmut_4': x_get_char_count_array__mutmut_4, 
    'x_get_char_count_array__mutmut_5': x_get_char_count_array__mutmut_5, 
    'x_get_char_count_array__mutmut_6': x_get_char_count_array__mutmut_6, 
    'x_get_char_count_array__mutmut_7': x_get_char_count_array__mutmut_7
}

def get_char_count_array(*args, **kwargs):
	result = _mutmut_trampoline(x_get_char_count_array__mutmut_orig, x_get_char_count_array__mutmut_mutants, args, kwargs)
	return result 

get_char_count_array.__signature__ = _mutmut_signature(x_get_char_count_array__mutmut_orig)
x_get_char_count_array__mutmut_orig.__name__ = 'x_get_char_count_array'
def x_remove_dirty_chars__mutmut_orig(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_1(string, second_string): 
	count = None 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_2(string, second_string): 
	count = get_char_count_array(None) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_3(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = None
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_4(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 1
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_5(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = None
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_6(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 1
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_7(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = None 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_8(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = 'XXXX' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_9(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = None 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_10(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(None) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_11(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind == len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_12(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = None 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_13(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(None)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_14(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] != 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_15(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 1: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_16(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = None 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_17(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind = 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_18(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind -= 1
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_19(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 2
		ip_ind+=1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_20(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind = 1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_21(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind -= 1
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_22(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=2
	return lst_to_string(str_list[0:res_ind]) 
def x_remove_dirty_chars__mutmut_23(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(None) 
def x_remove_dirty_chars__mutmut_24(string, second_string): 
	count = get_char_count_array(second_string) 
	ip_ind = 0
	res_ind = 0
	temp = '' 
	str_list = str_to_list(string) 
	while ip_ind != len(str_list): 
		temp = str_list[ip_ind] 
		if count[ord(temp)] == 0: 
			str_list[res_ind] = str_list[ip_ind] 
			res_ind += 1
		ip_ind+=1
	return lst_to_string(str_list[1:res_ind]) 

x_remove_dirty_chars__mutmut_mutants : ClassVar[MutantDict] = {
'x_remove_dirty_chars__mutmut_1': x_remove_dirty_chars__mutmut_1, 
    'x_remove_dirty_chars__mutmut_2': x_remove_dirty_chars__mutmut_2, 
    'x_remove_dirty_chars__mutmut_3': x_remove_dirty_chars__mutmut_3, 
    'x_remove_dirty_chars__mutmut_4': x_remove_dirty_chars__mutmut_4, 
    'x_remove_dirty_chars__mutmut_5': x_remove_dirty_chars__mutmut_5, 
    'x_remove_dirty_chars__mutmut_6': x_remove_dirty_chars__mutmut_6, 
    'x_remove_dirty_chars__mutmut_7': x_remove_dirty_chars__mutmut_7, 
    'x_remove_dirty_chars__mutmut_8': x_remove_dirty_chars__mutmut_8, 
    'x_remove_dirty_chars__mutmut_9': x_remove_dirty_chars__mutmut_9, 
    'x_remove_dirty_chars__mutmut_10': x_remove_dirty_chars__mutmut_10, 
    'x_remove_dirty_chars__mutmut_11': x_remove_dirty_chars__mutmut_11, 
    'x_remove_dirty_chars__mutmut_12': x_remove_dirty_chars__mutmut_12, 
    'x_remove_dirty_chars__mutmut_13': x_remove_dirty_chars__mutmut_13, 
    'x_remove_dirty_chars__mutmut_14': x_remove_dirty_chars__mutmut_14, 
    'x_remove_dirty_chars__mutmut_15': x_remove_dirty_chars__mutmut_15, 
    'x_remove_dirty_chars__mutmut_16': x_remove_dirty_chars__mutmut_16, 
    'x_remove_dirty_chars__mutmut_17': x_remove_dirty_chars__mutmut_17, 
    'x_remove_dirty_chars__mutmut_18': x_remove_dirty_chars__mutmut_18, 
    'x_remove_dirty_chars__mutmut_19': x_remove_dirty_chars__mutmut_19, 
    'x_remove_dirty_chars__mutmut_20': x_remove_dirty_chars__mutmut_20, 
    'x_remove_dirty_chars__mutmut_21': x_remove_dirty_chars__mutmut_21, 
    'x_remove_dirty_chars__mutmut_22': x_remove_dirty_chars__mutmut_22, 
    'x_remove_dirty_chars__mutmut_23': x_remove_dirty_chars__mutmut_23, 
    'x_remove_dirty_chars__mutmut_24': x_remove_dirty_chars__mutmut_24
}

def remove_dirty_chars(*args, **kwargs):
	result = _mutmut_trampoline(x_remove_dirty_chars__mutmut_orig, x_remove_dirty_chars__mutmut_mutants, args, kwargs)
	return result 

remove_dirty_chars.__signature__ = _mutmut_signature(x_remove_dirty_chars__mutmut_orig)
x_remove_dirty_chars__mutmut_orig.__name__ = 'x_remove_dirty_chars'