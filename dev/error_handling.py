import re
from modules.ErrorHandling import ErrorHandling
e_h = ErrorHandling()


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
  File "/usr/src/app/main.py", line 105, in <module>
    raise Exception('An error occurred. This is a generic error message. See previous error message')
Exception: An error occurred. This is a generic error message. See previous error message)
"""


big_code_example = """
list index out of range
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

"""

big_code_example = big_code_example.strip()
# print(e_h.is_unittest_error(big_code_example))

with open("../log/all_errors.txt", "r") as f:
    big_code_error = f.read()

big_code_error = big_code_error.split("#"*100)

for item in big_code_error:
    temp = e_h.remove_multithread_generic_error(item)
    try:
        if not e_h.is_unittest_error(temp):
            print(item)
            print("#"*100)
    except Exception as e:
        print(temp)
        print("$"*50)
        print(e)
# big_code_error = [e_h.remove_multithread_generic_error(err) for err in big_code_error]
#
# for err in big_code_error:
#     try:
#         if not e_h.is_unittest_error(err):
#             if "FAILED" in err:
#                 pass
#             else:
#                 print(err)
#                 print("#"*100)
#     except IndexError as e:
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#
# with open("../log/all_errors_cleaned.txt", "w") as clean_f:
#     for err in big_code_error:
#         clean_f.write(err)
#         clean_f.write("\n")
#         clean_f.write("#"*100)
#         clean_f.write("\n")

# print(e_h.remove_multithread_generic_error(big_code_example))


# external_file_error_test = """Traceback (most recent call last):
#   File "/usr/src/app/main_test.py", line 85, in test_case_2
#     transformed_df, fig = task_func(df)
#   File "/usr/src/app/main.py", line 51, in task_func
#     transformed_df[col], _ = stats.boxcox(transformed_df[col].replace(0, np.nan))
#   File "/usr/local/lib/python3.8/dist-packages/scipy/stats/morestats.py", line 1061, in boxcox
#     raise ValueError("Data must not be constant.")
# ValueError: Data must not be constant.
# """

# for item in e_h._unittest_extract_all_tracebacks(big_code_example):
#     print(item)
#     print("#"*100)