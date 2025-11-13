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
def x_sum_div__mutmut_orig(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_1(number):
    divisors = None
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_2(number):
    divisors = [2]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_3(number):
    divisors = [1]
    for i in range(None, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_4(number):
    divisors = [1]
    for i in range(2, None):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_5(number):
    divisors = [1]
    for i in range(number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_6(number):
    divisors = [1]
    for i in range(2, ):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_7(number):
    divisors = [1]
    for i in range(3, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_8(number):
    divisors = [1]
    for i in range(2, number):
        if (number / i)==0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_9(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i) != 0:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_10(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==1:
            divisors.append(i)
    return sum(divisors)
def x_sum_div__mutmut_11(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(None)
    return sum(divisors)
def x_sum_div__mutmut_12(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return sum(None)

x_sum_div__mutmut_mutants : ClassVar[MutantDict] = {
'x_sum_div__mutmut_1': x_sum_div__mutmut_1, 
    'x_sum_div__mutmut_2': x_sum_div__mutmut_2, 
    'x_sum_div__mutmut_3': x_sum_div__mutmut_3, 
    'x_sum_div__mutmut_4': x_sum_div__mutmut_4, 
    'x_sum_div__mutmut_5': x_sum_div__mutmut_5, 
    'x_sum_div__mutmut_6': x_sum_div__mutmut_6, 
    'x_sum_div__mutmut_7': x_sum_div__mutmut_7, 
    'x_sum_div__mutmut_8': x_sum_div__mutmut_8, 
    'x_sum_div__mutmut_9': x_sum_div__mutmut_9, 
    'x_sum_div__mutmut_10': x_sum_div__mutmut_10, 
    'x_sum_div__mutmut_11': x_sum_div__mutmut_11, 
    'x_sum_div__mutmut_12': x_sum_div__mutmut_12
}

def sum_div(*args, **kwargs):
    result = _mutmut_trampoline(x_sum_div__mutmut_orig, x_sum_div__mutmut_mutants, args, kwargs)
    return result 

sum_div.__signature__ = _mutmut_signature(x_sum_div__mutmut_orig)
x_sum_div__mutmut_orig.__name__ = 'x_sum_div'