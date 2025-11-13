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
def x_power_base_sum__mutmut_orig(base, power):
    return sum([int(i) for i in str(pow(base, power))])
def x_power_base_sum__mutmut_1(base, power):
    return sum(None)
def x_power_base_sum__mutmut_2(base, power):
    return sum([int(None) for i in str(pow(base, power))])
def x_power_base_sum__mutmut_3(base, power):
    return sum([int(i) for i in str(None)])
def x_power_base_sum__mutmut_4(base, power):
    return sum([int(i) for i in str(pow(None, power))])
def x_power_base_sum__mutmut_5(base, power):
    return sum([int(i) for i in str(pow(base, None))])
def x_power_base_sum__mutmut_6(base, power):
    return sum([int(i) for i in str(pow(power))])
def x_power_base_sum__mutmut_7(base, power):
    return sum([int(i) for i in str(pow(base, ))])

x_power_base_sum__mutmut_mutants : ClassVar[MutantDict] = {
'x_power_base_sum__mutmut_1': x_power_base_sum__mutmut_1, 
    'x_power_base_sum__mutmut_2': x_power_base_sum__mutmut_2, 
    'x_power_base_sum__mutmut_3': x_power_base_sum__mutmut_3, 
    'x_power_base_sum__mutmut_4': x_power_base_sum__mutmut_4, 
    'x_power_base_sum__mutmut_5': x_power_base_sum__mutmut_5, 
    'x_power_base_sum__mutmut_6': x_power_base_sum__mutmut_6, 
    'x_power_base_sum__mutmut_7': x_power_base_sum__mutmut_7
}

def power_base_sum(*args, **kwargs):
    result = _mutmut_trampoline(x_power_base_sum__mutmut_orig, x_power_base_sum__mutmut_mutants, args, kwargs)
    return result 

power_base_sum.__signature__ = _mutmut_signature(x_power_base_sum__mutmut_orig)
x_power_base_sum__mutmut_orig.__name__ = 'x_power_base_sum'