import unittest
from curry import curry

class TestCurryDecorator(unittest.TestCase):
    def test_curry_no_args(self):
        @curry
        def hello():
            return "Hello"

        self.assertEqual("Hello", hello())

    def test_curry_fixed_args(self):
        @curry
        def message(greetings, username, advice):
            return "%s, %s! %s." % (greetings, username, advice)

        self.assertEqual("Hello, Andrey! Take a break.", message("Hello", "Andrey", "Take a break"))
        self.assertEqual("Hi, Steve! Stay cool.", message("Hi", "Steve")("Stay cool"))
        self.assertEqual("Good night, Bill! Try Debian.", message("Good night")("Bill", "Try Debian"))
        self.assertEqual("Good morning, Linus! Try win phone 8.", message("Good morning")("Linus")("Try win phone 8"))
        self.assertEqual("As you wish, Palpatine! But please, don't use lighting on my son.", message()("As you wish")()("Palpatine")()("But please, don't use lighting on my son"))
        self.assertRaises(TypeError, message, "Pysh Pysh", "ololo", "Ya voditel nlo", "voditel nlo shouldn't be here")

    def test_curry_varargs(self):
        @curry
        def args_sum(*args):
            return sum(args)

        self.assertEqual(0, args_sum())
        self.assertEqual(1, args_sum(1))
        self.assertEqual(3, args_sum(1, 2))
        self.assertEqual(7, args_sum(1, 2, 4))

    def test_curry_fixed_args_with_varargs(self):
        @curry
        def args_sum(a, *args):
            return sum(args, a)

        self.assertEqual(1, args_sum()(1))
        self.assertEqual(3, args_sum()(1, 2))
        self.assertEqual(7, args_sum()(1, 2, 4))
        self.assertEqual(1, args_sum(1))
        self.assertEqual(3, args_sum(1, 2))
        self.assertEqual(7, args_sum(1, 2, 4))

    def test_curry_named_args(self):
        @curry
        def kwargs_madness(**kwargs):
            return "".join(sorted(kwargs.iterkeys()) + sorted(kwargs.itervalues()))

        self.assertEqual("", kwargs_madness())
        self.assertEqual("a1", kwargs_madness(a="1"))
        self.assertEqual("ab12", kwargs_madness(a="1", b="2"))
        self.assertEqual("abc123", kwargs_madness(a="1", b="2", c="3"))

    def test_curry_fixed_args_with_named_args(self):
        @curry
        def kwargs_madness(start, **kwargs):
            return start + "".join(sorted(kwargs.iterkeys()) + sorted(kwargs.itervalues()))

        self.assertEqual("q", kwargs_madness()("q"))
        self.assertEqual("qa1", kwargs_madness()(a="1")("q"))
        self.assertEqual("qab12", kwargs_madness()(a="1")(b="2")("q"))
        self.assertEqual("qab12", kwargs_madness()(a="1", b="2")("q"))

        self.assertEqual("q", kwargs_madness("q"))
        self.assertEqual("qa1", kwargs_madness(a="1")("q"))
        self.assertEqual("qab12", kwargs_madness(a="1")(b="2")("q"))
        self.assertEqual("qab12", kwargs_madness(a="1", b="2")("q"))

        self.assertEqual("qa1", kwargs_madness(a="1")()("q"))
        self.assertEqual("qab12", kwargs_madness(a="1")(b="2")()("q"))
        self.assertEqual("qab12", kwargs_madness(a="1", b="2")()("q"))

    def test_curry_defaults(self):
        @curry
        def func_with_defaults(a=1, b=2, c=4):
            return a + b + c

        self.assertEqual(7, func_with_defaults())
        self.assertEqual(14, func_with_defaults(8))
        self.assertEqual(28, func_with_defaults(8, 16))
        self.assertEqual(56, func_with_defaults(8, 16, 32))
        self.assertRaises(TypeError, func_with_defaults, 8, 16, 32, 64)

    def test_curry_fixed_args_with_defaults(self):
        @curry
        def func_with_defaults(start, a=1, b=2, c=4):
            return start + a + b + c

        self.assertEqual(17, func_with_defaults()(10))
        self.assertEqual(24, func_with_defaults()(10, 8))
        self.assertEqual(38, func_with_defaults()(10, 8, 16))
        self.assertEqual(66, func_with_defaults()(10, 8, 16, 32))

        self.assertEqual(17, func_with_defaults(10))
        self.assertEqual(24, func_with_defaults(10, 8))
        self.assertEqual(38, func_with_defaults(10, 8, 16))
        self.assertEqual(66, func_with_defaults(10, 8, 16, 32))

    def test_curry_all_together_now(self):
        @curry
        def sum_all_args(a, b=16, *args, **kwargs):
            return a + b + sum(args) + sum(kwargs.itervalues())

        self.assertEqual(15, sum_all_args(1, 2, 4, d=8))
        self.assertEqual(7, sum_all_args(1, 2, 4))
        self.assertEqual(3, sum_all_args(1, 2))
        self.assertEqual(17, sum_all_args(1))
        self.assertEqual(15, sum_all_args(d=8)(1, 2, 4))
        self.assertEqual(11, sum_all_args(d=8)(1, 2))
        self.assertEqual(25, sum_all_args(d=8)(1))

        self.assertEqual(15, sum_all_args()(1, 2, 4, d=8))
        self.assertEqual(7, sum_all_args()(1, 2, 4))
        self.assertEqual(3, sum_all_args()(1, 2))
        self.assertEqual(17, sum_all_args()(1))
        self.assertEqual(15, sum_all_args()(d=8)(1, 2, 4))
        self.assertEqual(11, sum_all_args()(d=8)(1, 2))
        self.assertEqual(25, sum_all_args()(d=8)(1))

        self.assertEqual(255, sum_all_args()(d=32)(e=64)()(f=128)(1, 2, 4, 8, 16))
