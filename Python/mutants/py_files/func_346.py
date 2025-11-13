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
def x_maxAverageOfPath__mutmut_orig(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_1(cost):
  N = None
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_2(cost):
  N = len(cost)
  dp = None
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_3(cost):
  N = len(cost)
  dp = [[1 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_4(cost):
  N = len(cost)
  dp = [[0 for i in range(None)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_5(cost):
  N = len(cost)
  dp = [[0 for i in range(N - 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_6(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 2)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_7(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(None)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_8(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N - 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_9(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 2)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_10(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = None
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_11(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[1][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_12(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][1] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_13(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[1][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_14(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][1]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_15(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(None, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_16(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, None):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_17(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_18(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, ):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_19(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(2, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_20(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = None
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_21(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][1] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_22(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] - cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_23(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i + 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_24(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 2][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_25(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][1] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_26(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][1]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_27(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(None, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_28(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, None):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_29(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_30(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, ):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_31(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(2, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_32(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = None
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_33(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[1][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_34(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] - cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_35(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[1][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_36(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j + 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_37(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 2] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_38(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[1][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_39(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(None, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_40(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, None):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_41(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_42(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, ):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_43(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(2, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_44(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(None, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_45(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, None):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_46(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_47(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, ):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_48(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(2, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_49(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = None
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_50(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) - cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_51(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(None,
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_52(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     None) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_53(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_54(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     ) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_55(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i + 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_56(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 2][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_57(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j + 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_58(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 2]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_59(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] * (2 * N - 1)
def x_maxAverageOfPath__mutmut_60(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N + 1][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_61(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 2][N - 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_62(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N + 1] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_63(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 2] / (2 * N - 1)
def x_maxAverageOfPath__mutmut_64(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N + 1)
def x_maxAverageOfPath__mutmut_65(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 / N - 1)
def x_maxAverageOfPath__mutmut_66(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (3 * N - 1)
def x_maxAverageOfPath__mutmut_67(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 2)

x_maxAverageOfPath__mutmut_mutants : ClassVar[MutantDict] = {
'x_maxAverageOfPath__mutmut_1': x_maxAverageOfPath__mutmut_1, 
    'x_maxAverageOfPath__mutmut_2': x_maxAverageOfPath__mutmut_2, 
    'x_maxAverageOfPath__mutmut_3': x_maxAverageOfPath__mutmut_3, 
    'x_maxAverageOfPath__mutmut_4': x_maxAverageOfPath__mutmut_4, 
    'x_maxAverageOfPath__mutmut_5': x_maxAverageOfPath__mutmut_5, 
    'x_maxAverageOfPath__mutmut_6': x_maxAverageOfPath__mutmut_6, 
    'x_maxAverageOfPath__mutmut_7': x_maxAverageOfPath__mutmut_7, 
    'x_maxAverageOfPath__mutmut_8': x_maxAverageOfPath__mutmut_8, 
    'x_maxAverageOfPath__mutmut_9': x_maxAverageOfPath__mutmut_9, 
    'x_maxAverageOfPath__mutmut_10': x_maxAverageOfPath__mutmut_10, 
    'x_maxAverageOfPath__mutmut_11': x_maxAverageOfPath__mutmut_11, 
    'x_maxAverageOfPath__mutmut_12': x_maxAverageOfPath__mutmut_12, 
    'x_maxAverageOfPath__mutmut_13': x_maxAverageOfPath__mutmut_13, 
    'x_maxAverageOfPath__mutmut_14': x_maxAverageOfPath__mutmut_14, 
    'x_maxAverageOfPath__mutmut_15': x_maxAverageOfPath__mutmut_15, 
    'x_maxAverageOfPath__mutmut_16': x_maxAverageOfPath__mutmut_16, 
    'x_maxAverageOfPath__mutmut_17': x_maxAverageOfPath__mutmut_17, 
    'x_maxAverageOfPath__mutmut_18': x_maxAverageOfPath__mutmut_18, 
    'x_maxAverageOfPath__mutmut_19': x_maxAverageOfPath__mutmut_19, 
    'x_maxAverageOfPath__mutmut_20': x_maxAverageOfPath__mutmut_20, 
    'x_maxAverageOfPath__mutmut_21': x_maxAverageOfPath__mutmut_21, 
    'x_maxAverageOfPath__mutmut_22': x_maxAverageOfPath__mutmut_22, 
    'x_maxAverageOfPath__mutmut_23': x_maxAverageOfPath__mutmut_23, 
    'x_maxAverageOfPath__mutmut_24': x_maxAverageOfPath__mutmut_24, 
    'x_maxAverageOfPath__mutmut_25': x_maxAverageOfPath__mutmut_25, 
    'x_maxAverageOfPath__mutmut_26': x_maxAverageOfPath__mutmut_26, 
    'x_maxAverageOfPath__mutmut_27': x_maxAverageOfPath__mutmut_27, 
    'x_maxAverageOfPath__mutmut_28': x_maxAverageOfPath__mutmut_28, 
    'x_maxAverageOfPath__mutmut_29': x_maxAverageOfPath__mutmut_29, 
    'x_maxAverageOfPath__mutmut_30': x_maxAverageOfPath__mutmut_30, 
    'x_maxAverageOfPath__mutmut_31': x_maxAverageOfPath__mutmut_31, 
    'x_maxAverageOfPath__mutmut_32': x_maxAverageOfPath__mutmut_32, 
    'x_maxAverageOfPath__mutmut_33': x_maxAverageOfPath__mutmut_33, 
    'x_maxAverageOfPath__mutmut_34': x_maxAverageOfPath__mutmut_34, 
    'x_maxAverageOfPath__mutmut_35': x_maxAverageOfPath__mutmut_35, 
    'x_maxAverageOfPath__mutmut_36': x_maxAverageOfPath__mutmut_36, 
    'x_maxAverageOfPath__mutmut_37': x_maxAverageOfPath__mutmut_37, 
    'x_maxAverageOfPath__mutmut_38': x_maxAverageOfPath__mutmut_38, 
    'x_maxAverageOfPath__mutmut_39': x_maxAverageOfPath__mutmut_39, 
    'x_maxAverageOfPath__mutmut_40': x_maxAverageOfPath__mutmut_40, 
    'x_maxAverageOfPath__mutmut_41': x_maxAverageOfPath__mutmut_41, 
    'x_maxAverageOfPath__mutmut_42': x_maxAverageOfPath__mutmut_42, 
    'x_maxAverageOfPath__mutmut_43': x_maxAverageOfPath__mutmut_43, 
    'x_maxAverageOfPath__mutmut_44': x_maxAverageOfPath__mutmut_44, 
    'x_maxAverageOfPath__mutmut_45': x_maxAverageOfPath__mutmut_45, 
    'x_maxAverageOfPath__mutmut_46': x_maxAverageOfPath__mutmut_46, 
    'x_maxAverageOfPath__mutmut_47': x_maxAverageOfPath__mutmut_47, 
    'x_maxAverageOfPath__mutmut_48': x_maxAverageOfPath__mutmut_48, 
    'x_maxAverageOfPath__mutmut_49': x_maxAverageOfPath__mutmut_49, 
    'x_maxAverageOfPath__mutmut_50': x_maxAverageOfPath__mutmut_50, 
    'x_maxAverageOfPath__mutmut_51': x_maxAverageOfPath__mutmut_51, 
    'x_maxAverageOfPath__mutmut_52': x_maxAverageOfPath__mutmut_52, 
    'x_maxAverageOfPath__mutmut_53': x_maxAverageOfPath__mutmut_53, 
    'x_maxAverageOfPath__mutmut_54': x_maxAverageOfPath__mutmut_54, 
    'x_maxAverageOfPath__mutmut_55': x_maxAverageOfPath__mutmut_55, 
    'x_maxAverageOfPath__mutmut_56': x_maxAverageOfPath__mutmut_56, 
    'x_maxAverageOfPath__mutmut_57': x_maxAverageOfPath__mutmut_57, 
    'x_maxAverageOfPath__mutmut_58': x_maxAverageOfPath__mutmut_58, 
    'x_maxAverageOfPath__mutmut_59': x_maxAverageOfPath__mutmut_59, 
    'x_maxAverageOfPath__mutmut_60': x_maxAverageOfPath__mutmut_60, 
    'x_maxAverageOfPath__mutmut_61': x_maxAverageOfPath__mutmut_61, 
    'x_maxAverageOfPath__mutmut_62': x_maxAverageOfPath__mutmut_62, 
    'x_maxAverageOfPath__mutmut_63': x_maxAverageOfPath__mutmut_63, 
    'x_maxAverageOfPath__mutmut_64': x_maxAverageOfPath__mutmut_64, 
    'x_maxAverageOfPath__mutmut_65': x_maxAverageOfPath__mutmut_65, 
    'x_maxAverageOfPath__mutmut_66': x_maxAverageOfPath__mutmut_66, 
    'x_maxAverageOfPath__mutmut_67': x_maxAverageOfPath__mutmut_67
}

def maxAverageOfPath(*args, **kwargs):
  result = _mutmut_trampoline(x_maxAverageOfPath__mutmut_orig, x_maxAverageOfPath__mutmut_mutants, args, kwargs)
  return result 

maxAverageOfPath.__signature__ = _mutmut_signature(x_maxAverageOfPath__mutmut_orig)
x_maxAverageOfPath__mutmut_orig.__name__ = 'x_maxAverageOfPath'