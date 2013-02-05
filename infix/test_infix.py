import unittest
from infix import Infix

class TestInfix(unittest.TestCase):
    def test_infix_as_decorator(self):
        @Infix
        def x(a, b):
            return a * b


        @Infix
        def isa(a, b):
            return a.__class__ == b.__class__

        self.assertTrue("string" | isa | "another string")

    def test_infix(self):
        x = Infix(lambda x, y: x * y)
        self.assertEqual(8, 2 | x | 4)

        isa = Infix(lambda x, y: x.__class__ == y.__class__)
        self.assertTrue({"a": 1, "b": 2} | isa | {})