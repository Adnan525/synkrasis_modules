from typing import Any
import random

def foo(lambda_func: callable) -> Any:
    my_str: str = "test string"
    return lambda_func(my_str)

my_lambdas: list[callable] = [
    lambda s: len(s),
    lambda s: len(s.splitlines()),
    lambda s: s.upper(),
    lambda s: s.append("new string"),
    lambda s: s.replace("test", "new"),
    lambda s: s.split(" "),
    lambda s: s.strip(),
    lambda s: s.get_next(),
    lambda s: s.get("key"),
]

import unittest
class TestIsUnittest(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(foo(random.choice(my_lambdas)), 11)

    def test_case_2(self):
        self.assertEqual(foo(random.choice(my_lambdas)), "new string")

    def test_case_3(self):
        self.assertEqual(foo(random.choice(my_lambdas)), 1)

    def test_case_4(self):
        self.assertEqual(foo(random.choice(my_lambdas)), ["test", "string"])

if __name__ == '__main__':
    direct_call_counter = 0
    if random.choice([True, False]):
        unittest.main()
    else:
        direct_call_counter += 1
        foo(random.choice(my_lambdas))