import heapq
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
def x_k_smallest_pairs__mutmut_orig(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_1(nums1, nums2, k):
   queue = None
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_2(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) or j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_3(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i <= len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_4(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j <= len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_5(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(None, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_6(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, None)
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_7(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush([nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_8(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, )
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_9(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] - nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_10(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(None, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_11(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, None)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_12(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_13(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, )
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_14(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(1, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_15(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 1)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_16(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = None
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_17(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue or len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_18(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) <= k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_19(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = None
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_20(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(None)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_21(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append(None)
       push(i, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_22(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(None, j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_23(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, None)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_24(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(j + 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_25(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, )
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_26(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j - 1)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_27(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 2)
       if j == 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_28(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j != 0:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_29(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 1:
           push(i + 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_30(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(None, 0)
   return pairs
def x_k_smallest_pairs__mutmut_31(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, None)
   return pairs
def x_k_smallest_pairs__mutmut_32(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(0)
   return pairs
def x_k_smallest_pairs__mutmut_33(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, )
   return pairs
def x_k_smallest_pairs__mutmut_34(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i - 1, 0)
   return pairs
def x_k_smallest_pairs__mutmut_35(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 2, 0)
   return pairs
def x_k_smallest_pairs__mutmut_36(nums1, nums2, k):
   queue = []
   def push(i, j):
       if i < len(nums1) and j < len(nums2):
           heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
   push(0, 0)
   pairs = []
   while queue and len(pairs) < k:
       _, i, j = heapq.heappop(queue)
       pairs.append([nums1[i], nums2[j]])
       push(i, j + 1)
       if j == 0:
           push(i + 1, 1)
   return pairs

x_k_smallest_pairs__mutmut_mutants : ClassVar[MutantDict] = {
'x_k_smallest_pairs__mutmut_1': x_k_smallest_pairs__mutmut_1, 
    'x_k_smallest_pairs__mutmut_2': x_k_smallest_pairs__mutmut_2, 
    'x_k_smallest_pairs__mutmut_3': x_k_smallest_pairs__mutmut_3, 
    'x_k_smallest_pairs__mutmut_4': x_k_smallest_pairs__mutmut_4, 
    'x_k_smallest_pairs__mutmut_5': x_k_smallest_pairs__mutmut_5, 
    'x_k_smallest_pairs__mutmut_6': x_k_smallest_pairs__mutmut_6, 
    'x_k_smallest_pairs__mutmut_7': x_k_smallest_pairs__mutmut_7, 
    'x_k_smallest_pairs__mutmut_8': x_k_smallest_pairs__mutmut_8, 
    'x_k_smallest_pairs__mutmut_9': x_k_smallest_pairs__mutmut_9, 
    'x_k_smallest_pairs__mutmut_10': x_k_smallest_pairs__mutmut_10, 
    'x_k_smallest_pairs__mutmut_11': x_k_smallest_pairs__mutmut_11, 
    'x_k_smallest_pairs__mutmut_12': x_k_smallest_pairs__mutmut_12, 
    'x_k_smallest_pairs__mutmut_13': x_k_smallest_pairs__mutmut_13, 
    'x_k_smallest_pairs__mutmut_14': x_k_smallest_pairs__mutmut_14, 
    'x_k_smallest_pairs__mutmut_15': x_k_smallest_pairs__mutmut_15, 
    'x_k_smallest_pairs__mutmut_16': x_k_smallest_pairs__mutmut_16, 
    'x_k_smallest_pairs__mutmut_17': x_k_smallest_pairs__mutmut_17, 
    'x_k_smallest_pairs__mutmut_18': x_k_smallest_pairs__mutmut_18, 
    'x_k_smallest_pairs__mutmut_19': x_k_smallest_pairs__mutmut_19, 
    'x_k_smallest_pairs__mutmut_20': x_k_smallest_pairs__mutmut_20, 
    'x_k_smallest_pairs__mutmut_21': x_k_smallest_pairs__mutmut_21, 
    'x_k_smallest_pairs__mutmut_22': x_k_smallest_pairs__mutmut_22, 
    'x_k_smallest_pairs__mutmut_23': x_k_smallest_pairs__mutmut_23, 
    'x_k_smallest_pairs__mutmut_24': x_k_smallest_pairs__mutmut_24, 
    'x_k_smallest_pairs__mutmut_25': x_k_smallest_pairs__mutmut_25, 
    'x_k_smallest_pairs__mutmut_26': x_k_smallest_pairs__mutmut_26, 
    'x_k_smallest_pairs__mutmut_27': x_k_smallest_pairs__mutmut_27, 
    'x_k_smallest_pairs__mutmut_28': x_k_smallest_pairs__mutmut_28, 
    'x_k_smallest_pairs__mutmut_29': x_k_smallest_pairs__mutmut_29, 
    'x_k_smallest_pairs__mutmut_30': x_k_smallest_pairs__mutmut_30, 
    'x_k_smallest_pairs__mutmut_31': x_k_smallest_pairs__mutmut_31, 
    'x_k_smallest_pairs__mutmut_32': x_k_smallest_pairs__mutmut_32, 
    'x_k_smallest_pairs__mutmut_33': x_k_smallest_pairs__mutmut_33, 
    'x_k_smallest_pairs__mutmut_34': x_k_smallest_pairs__mutmut_34, 
    'x_k_smallest_pairs__mutmut_35': x_k_smallest_pairs__mutmut_35, 
    'x_k_smallest_pairs__mutmut_36': x_k_smallest_pairs__mutmut_36
}

def k_smallest_pairs(*args, **kwargs):
   result = _mutmut_trampoline(x_k_smallest_pairs__mutmut_orig, x_k_smallest_pairs__mutmut_mutants, args, kwargs)
   return result 

k_smallest_pairs.__signature__ = _mutmut_signature(x_k_smallest_pairs__mutmut_orig)
x_k_smallest_pairs__mutmut_orig.__name__ = 'x_k_smallest_pairs'