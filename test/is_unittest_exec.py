import subprocess
from dev.error_handling import is_unittest_error
script_name = "is_unittest.py"

for i in range(101):
        result = subprocess.run(
            ["python", script_name],
            capture_output=True,
            text=True
        )
        error_message = result.stderr
        try:
            # If correct wont have anything in stderr
            if not is_unittest_error(error_message):
                print("=" * 50)
                print(error_message)
                print("="*50)
        except Exception as e:
            print("#"*50)
            print(result.returncode)
            print("#" * 50)
