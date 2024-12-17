from modules.ExampleCallDetection import ExampleCallDetection

example_code = """
from utils.test import too, bar, up
import pandas as pd

assign_example = 1 + 1
another_assign_example = foo(assign_example)

def foo(target: int)->int:
    return target

def load_csv(file_path):
    return pd.read_csv(file_path)

# Example
df = 1
df = load_csv("data.csv")
foo(df)
"""
# actual test file
with open("../test/test.py", "r") as f:
    example_code = f.read()

e_d = ExampleCallDetection()
print(e_d.extract_code_blocks(example_code))
