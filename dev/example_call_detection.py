import ast, astor
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

# tree = ast.parse(example_code).body
#
# for item in tree:
#     print(item)
#
# print(tree[0].names[0].name)
#
# for key, value in tree[0].__dict__.items():
#     print(key, value)

e_d = ExampleCallDetection()
print()