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
def x_subject_marks__mutmut_orig(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[1])
 return subjectmarks
def x_subject_marks__mutmut_1(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = None)
 return subjectmarks
def x_subject_marks__mutmut_2(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: None)
 return subjectmarks
def x_subject_marks__mutmut_3(subjectmarks):
#subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
 subjectmarks.sort(key = lambda x: x[2])
 return subjectmarks

x_subject_marks__mutmut_mutants : ClassVar[MutantDict] = {
'x_subject_marks__mutmut_1': x_subject_marks__mutmut_1, 
    'x_subject_marks__mutmut_2': x_subject_marks__mutmut_2, 
    'x_subject_marks__mutmut_3': x_subject_marks__mutmut_3
}

def subject_marks(*args, **kwargs):
 result = _mutmut_trampoline(x_subject_marks__mutmut_orig, x_subject_marks__mutmut_mutants, args, kwargs)
 return result 

subject_marks.__signature__ = _mutmut_signature(x_subject_marks__mutmut_orig)
x_subject_marks__mutmut_orig.__name__ = 'x_subject_marks'