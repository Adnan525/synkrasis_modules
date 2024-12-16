import re
from modules.ErrorHandling import ErrorHandling

e_h = ErrorHandling()

error_message = """
EEEE.E
======================================================================
ERROR: test_custom_values_successful_script (__main__.TestCases)
Test the function with custom script name and log file with successful execution
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/mock.py", line 1325, in patched
    return func(*newargs, **newkeywargs)
  File "/usr/src/app/main.py", line 103, in test_custom_values_successful_script
    result = task_func(script_name, log_file)
  File "/usr/src/app/main.py", line 42, in task_func
    raise FileNotFoundError(f"Script '{script_name}' does not exist.")
FileNotFoundError: Script 'custom_backup.sh' does not exist.

======================================================================
ERROR: test_default_values_successful_script (__main__.TestCases)
Test the function with default parameters and successful execution
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/mock.py", line 1325, in patched
    return func(*newargs, **newkeywargs)
  File "/usr/src/app/main.py", line 81, in test_default_values_successful_script
    result = task_func()
  File "/usr/src/app/main.py", line 42, in task_func
    raise FileNotFoundError(f"Script '{script_name}' does not exist.")
FileNotFoundError: Script 'backup.sh' does not exist.

======================================================================
ERROR: test_log_data_format (__main__.TestCases)
Test that the timestamps are in the correct format
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/mock.py", line 1325, in patched
    return func(*newargs, **newkeywargs)
  File "/usr/src/app/main.py", line 112, in test_log_data_format
    result = task_func()
  File "/usr/src/app/main.py", line 42, in task_func
    raise FileNotFoundError(f"Script '{script_name}' does not exist.")
FileNotFoundError: Script 'backup.sh' does not exist.

======================================================================
ERROR: test_non_zero_exit_status (__main__.TestCases)
Test the function with a non-zero exit status
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/mock.py", line 1325, in patched
    return func(*newargs, **newkeywargs)
  File "/usr/src/app/main.py", line 120, in test_non_zero_exit_status
    result = task_func()
  File "/usr/src/app/main.py", line 42, in task_func
    raise FileNotFoundError(f"Script '{script_name}' does not exist.")
FileNotFoundError: Script 'backup.sh' does not exist.

======================================================================
ERROR: test_script_execution_failure (__main__.TestCases)
Test the function raising RuntimeError on script execution failure
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.8/unittest/mock.py", line 1325, in patched
    return func(*newargs, **newkeywargs)
  File "/usr/src/app/main.py", line 95, in test_script_execution_failure
    task_func()
  File "/usr/src/app/main.py", line 42, in task_func
    raise FileNotFoundError(f"Script '{script_name}' does not exist.")
FileNotFoundError: Script 'backup.sh' does not exist.

----------------------------------------------------------------------
Ran 6 tests in 0.033s

FAILED (errors=5)
Traceback (most recent call last):
  File "/usr/src/app/main.py", line 131, in <module>
    raise Exception('An error occurred. This is a generic error message. See previous error message')
Exception: An error occurred. This is a generic error message. See previous error message
"""

print(e_h.remove_multithread_generic_error(error_message))
