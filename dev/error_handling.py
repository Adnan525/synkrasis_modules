import re

from modules.ErrorHandling import ErrorHandling
from utils.output_message_format.output_colour import print_error

unittest_error = """
....E
======================================================================
ERROR: test_with_different_array_types (__main__.TestCases)
Compare gzipped sizes of int and float arrays to acknowledge compression differences.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/src/app/main.py", line 74, in test_with_different_array_types
    float_array = task_func(np.array([1.0, 2.0, 3.0], dtype=float))
  File "/usr/src/app/main.py", line 41, in task_func
    buffer.write(struct.pack('i', element))
struct.error: required argument is not an integer

----------------------------------------------------------------------
Ran 5 tests in 0.002s

FAILED (errors=1)
Traceback (most recent call last):
  File "/usr/src/app/main.py", line 92, in <module>
    raise Exception('An error occurred. This is a generic error message. See previous error message')
Exception: An error occurred. This is a generic error message. See previous error message

"""

e_h: ErrorHandling =  ErrorHandling()
removed_generic: str = e_h.remove_multithread_generic_error(unittest_error).strip()
print(removed_generic)

def is_unittest_error(error_message: str) -> bool:
    """
    Check if the error message is a unittest error.
    Check if the last line matched FAILED(fail_type=number,?\s?)
    """
    # Unittest pattern
    unittest_pattern: str = r"FAILED\s{1}\((?:\w+\=\d+,?\s?)+\)"

    # Edge case and generic error message
    if "This is a generic error message" in error_message:
        print_error("Must remove the generic error message.")
        raise ValueError("Must remove the generic error message.")

    # Get the last line
    last_line: str = error_message.strip().splitlines()[-1]

    # Check if the last line matches the unittest pattern
    return re.match(unittest_pattern, last_line) is not None


# print(is_unittest_error(removed_generic)) # True