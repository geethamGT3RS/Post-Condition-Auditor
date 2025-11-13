import pytest
import sys
import os
import math
sys.path.insert(0, os.path.abspath('.'))
from py_files.func_391 import odd_num_sum

def test_llm_generated_postconditions():
    n = 2
    result = odd_num_sum(n)

    assert result == 82

    assert isinstance(result, int) and result >= 0