import re

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
Exception: An error occurred. This is a generic error message. See previous error message)

"""

pattern = (r'Traceback \(most recent call last\):\n\s*'
           r'File "/usr/src/app/main.py", line \d+, in <module>\n\s*'
           r'raise Exception\(\'An error occurred. This is a generic error message. See previous error message\'\).*'
           r'Exception: An error occurred. This is a generic error message. See previous error message\).*')

new_text = re.sub(pattern, "", unittest_error, flags=re.DOTALL|re.MULTILINE)

print(new_text)