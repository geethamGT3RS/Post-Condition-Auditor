from collections import defaultdict
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
def x_count_Substrings__mutmut_orig(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_1(s):
    n = None
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_2(s):
    n = len(s)
    count,sum = None
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_3(s):
    n = len(s)
    count,sum = 1,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_4(s):
    n = len(s)
    count,sum = 0,1
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_5(s):
    n = len(s)
    count,sum = 0,0
    mp = None
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_6(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(None)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_7(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : None)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_8(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 1)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_9(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] = 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_10(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] -= 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_11(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[1] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_12(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 2
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_13(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(None):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_14(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum = ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_15(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum -= ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_16(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) + ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_17(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(None) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_18(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord(None)
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_19(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('XX0XX')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_20(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count = mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_21(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count -= mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_22(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum + (i + 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_23(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i - 1)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_24(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 2)]
        mp[sum - (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_25(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] = 1
    return count
def x_count_Substrings__mutmut_26(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] -= 1
    return count
def x_count_Substrings__mutmut_27(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum + (i + 1)] += 1
    return count
def x_count_Substrings__mutmut_28(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i - 1)] += 1
    return count
def x_count_Substrings__mutmut_29(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 2)] += 1
    return count
def x_count_Substrings__mutmut_30(s):
    n = len(s)
    count,sum = 0,0
    mp = defaultdict(lambda : 0)
    mp[0] += 1
    for i in range(n):
        sum += ord(s[i]) - ord('0')
        count += mp[sum - (i + 1)]
        mp[sum - (i + 1)] += 2
    return count

x_count_Substrings__mutmut_mutants : ClassVar[MutantDict] = {
'x_count_Substrings__mutmut_1': x_count_Substrings__mutmut_1, 
    'x_count_Substrings__mutmut_2': x_count_Substrings__mutmut_2, 
    'x_count_Substrings__mutmut_3': x_count_Substrings__mutmut_3, 
    'x_count_Substrings__mutmut_4': x_count_Substrings__mutmut_4, 
    'x_count_Substrings__mutmut_5': x_count_Substrings__mutmut_5, 
    'x_count_Substrings__mutmut_6': x_count_Substrings__mutmut_6, 
    'x_count_Substrings__mutmut_7': x_count_Substrings__mutmut_7, 
    'x_count_Substrings__mutmut_8': x_count_Substrings__mutmut_8, 
    'x_count_Substrings__mutmut_9': x_count_Substrings__mutmut_9, 
    'x_count_Substrings__mutmut_10': x_count_Substrings__mutmut_10, 
    'x_count_Substrings__mutmut_11': x_count_Substrings__mutmut_11, 
    'x_count_Substrings__mutmut_12': x_count_Substrings__mutmut_12, 
    'x_count_Substrings__mutmut_13': x_count_Substrings__mutmut_13, 
    'x_count_Substrings__mutmut_14': x_count_Substrings__mutmut_14, 
    'x_count_Substrings__mutmut_15': x_count_Substrings__mutmut_15, 
    'x_count_Substrings__mutmut_16': x_count_Substrings__mutmut_16, 
    'x_count_Substrings__mutmut_17': x_count_Substrings__mutmut_17, 
    'x_count_Substrings__mutmut_18': x_count_Substrings__mutmut_18, 
    'x_count_Substrings__mutmut_19': x_count_Substrings__mutmut_19, 
    'x_count_Substrings__mutmut_20': x_count_Substrings__mutmut_20, 
    'x_count_Substrings__mutmut_21': x_count_Substrings__mutmut_21, 
    'x_count_Substrings__mutmut_22': x_count_Substrings__mutmut_22, 
    'x_count_Substrings__mutmut_23': x_count_Substrings__mutmut_23, 
    'x_count_Substrings__mutmut_24': x_count_Substrings__mutmut_24, 
    'x_count_Substrings__mutmut_25': x_count_Substrings__mutmut_25, 
    'x_count_Substrings__mutmut_26': x_count_Substrings__mutmut_26, 
    'x_count_Substrings__mutmut_27': x_count_Substrings__mutmut_27, 
    'x_count_Substrings__mutmut_28': x_count_Substrings__mutmut_28, 
    'x_count_Substrings__mutmut_29': x_count_Substrings__mutmut_29, 
    'x_count_Substrings__mutmut_30': x_count_Substrings__mutmut_30
}

def count_Substrings(*args, **kwargs):
    result = _mutmut_trampoline(x_count_Substrings__mutmut_orig, x_count_Substrings__mutmut_mutants, args, kwargs)
    return result 

count_Substrings.__signature__ = _mutmut_signature(x_count_Substrings__mutmut_orig)
x_count_Substrings__mutmut_orig.__name__ = 'x_count_Substrings'