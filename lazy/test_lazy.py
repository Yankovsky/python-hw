from functools import wraps
import unittest
from lazy import lazy
from lazy import lazy_maker

class TestLazyDecorator(unittest.TestCase):
    def test_lazy_without_args(self):
        global dec_executed
        global dec_wrapper_executed
        global func_executed
        dec_executed = False
        dec_wrapper_executed = False
        func_executed = False

        @lazy
        def dec(func):
            global dec_executed
            dec_executed = True

            @wraps(func)
            def wrapper():
                global dec_wrapper_executed
                dec_wrapper_executed = True
                return func()

            return wrapper

        @dec
        def dummy():
            global func_executed
            func_executed = True

        self.assertFalse(dec_executed)
        self.assertFalse(dec_wrapper_executed)
        self.assertFalse(func_executed)

        dummy()

        self.assertTrue(dec_executed)
        self.assertTrue(dec_wrapper_executed)
        self.assertTrue(func_executed)

    def test_lazy_with_args(self):
        global dec_executed
        global dec_wrapper_executed
        global func_executed
        dec_executed = False
        dec_wrapper_executed = False
        func_executed = False

        @lazy
        def dec(func):
            global dec_executed
            dec_executed = True

            @wraps(func)
            def wrapper(*args, **kwargs):
                global dec_wrapper_executed
                dec_wrapper_executed = True
                return func(*args, **kwargs)

            return wrapper

        @dec
        def sum_all_args(*args, **kwargs):
            global func_executed
            func_executed = True
            return sum(args) + sum(kwargs.values())

        self.assertFalse(dec_executed)
        self.assertFalse(dec_wrapper_executed)
        self.assertFalse(func_executed)

        result = sum_all_args(1, 2, a=3, b=4)

        self.assertTrue(dec_executed)
        self.assertTrue(dec_wrapper_executed)
        self.assertTrue(func_executed)
        self.assertEqual(10, result)

    def test_lazy_name_and_doc(self):
        @lazy
        def dec(func):
            """Sample decorator"""

            @wraps(func)
            def wrapper():
                pass

            return wrapper

        @dec
        def dummy():
            """Dummy function"""
            pass

        dummy()

        self.assertEqual("dec", dec.__name__)
        self.assertEqual("Sample decorator", dec.__doc__)
        self.assertEqual("dummy", dummy.__name__)
        self.assertEqual("Dummy function", dummy.__doc__)

    def test_lazy_maker_without_params_and_without_args(self):
        global dec_maker_executed
        global dec_executed
        global dec_wrapper_executed
        global func_executed
        dec_maker_executed = False
        dec_executed = False
        dec_wrapper_executed = False
        func_executed = False

        @lazy_maker
        def dec_maker():
            global dec_maker_executed
            dec_maker_executed = True

            def dec(func):
                global dec_executed
                dec_executed = True

                @wraps(func)
                def wrapper():
                    global dec_wrapper_executed
                    dec_wrapper_executed = True
                    return func()

                return wrapper

            return dec

        @dec_maker()
        def dummy():
            global func_executed
            func_executed = True

        self.assertFalse(dec_maker_executed)
        self.assertFalse(dec_executed)
        self.assertFalse(dec_wrapper_executed)
        self.assertFalse(func_executed)

        dummy()

        self.assertTrue(dec_maker_executed)
        self.assertTrue(dec_executed)
        self.assertTrue(dec_wrapper_executed)
        self.assertTrue(func_executed)

    def test_lazy_maker_without_params_and_with_args(self):
        global dec_maker_executed
        global dec_executed
        global dec_wrapper_executed
        global func_executed
        dec_maker_executed = False
        dec_executed = False
        dec_wrapper_executed = False
        func_executed = False

        @lazy_maker
        def dec_maker_with_params():
            global dec_maker_executed
            dec_maker_executed = True

            def dec_with_params(func):
                global dec_executed
                dec_executed = True

                @wraps(func)
                def wrapper(*args, **kwargs):
                    global dec_wrapper_executed
                    dec_wrapper_executed = True
                    # Here values in dec_kwargs override func kwargs.
                    # Maybe someone can find better way to use decorators which makes
                    # lazy decorators taking any params and executing with any args.
                    return func(*args, **kwargs)

                return wrapper

            return dec_with_params

        @dec_maker_with_params()
        def sum_all_args(*args, **kwargs):
            global func_executed
            func_executed = True
            return sum(args) + sum(kwargs.values())

        self.assertFalse(dec_maker_executed)
        self.assertFalse(dec_executed)
        self.assertFalse(dec_wrapper_executed)
        self.assertFalse(func_executed)

        result = sum_all_args(1, 2, a=3, b=4)

        self.assertTrue(dec_maker_executed)
        self.assertTrue(dec_executed)
        self.assertTrue(dec_wrapper_executed)
        self.assertTrue(func_executed)
        self.assertEqual(10, result)

    def test_lazy_maker_with_params_and_with_args(self):
        global dec_maker_executed
        global dec_executed
        global dec_wrapper_executed
        global func_executed
        dec_maker_executed = False
        dec_executed = False
        dec_wrapper_executed = False
        func_executed = False

        @lazy_maker
        def dec_maker_with_params(*dec_args, **dec_kwargs):
            global dec_maker_executed
            dec_maker_executed = True

            def dec_with_params(func):
                global dec_executed
                dec_executed = True

                @wraps(func)
                def wrapper(*args, **kwargs):
                    global dec_wrapper_executed
                    dec_wrapper_executed = True
                    # Here values in dec_kwargs override func kwargs.
                    # Maybe someone can find better way to use decorators which makes
                    # lazy decorators taking any params and executing with any args.
                    return func(*(args + dec_args), **(dict(kwargs.items() + dec_kwargs.items())))

                return wrapper

            return dec_with_params

        @dec_maker_with_params(5, 6, b=7, c=8)
        def sum_all_args(*args, **kwargs):
            global func_executed
            func_executed = True
            return sum(args) + sum(kwargs.values())

        self.assertFalse(dec_maker_executed)
        self.assertFalse(dec_executed)
        self.assertFalse(dec_wrapper_executed)
        self.assertFalse(func_executed)

        result = sum_all_args(1, 2, a=3, b=4)

        self.assertTrue(dec_maker_executed)
        self.assertTrue(dec_executed)
        self.assertTrue(dec_wrapper_executed)
        self.assertTrue(func_executed)
        self.assertEqual(32, result)

    def test_lazy_maker_name_and_doc(self):
        @lazy_maker
        def dec_maker(*dec_args, **dec_kwargs):
            """Sample decorators maker"""

            def dec(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    pass

                return wrapper

            return dec

        @dec_maker(1, 2, a=3, b=4)
        def dummy():
            """Dummy function"""
            pass

        dummy()

        self.assertEqual("dec_maker", dec_maker.__name__)
        self.assertEqual("Sample decorators maker", dec_maker.__doc__)
        self.assertEqual("dummy", dummy.__name__)
        self.assertEqual("Dummy function", dummy.__doc__)