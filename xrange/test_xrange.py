from random import randint
import unittest
from xrange import Xrange

class TestXrange(unittest.TestCase):
    def len_check(self, start, stop, step):
        actual = len(Xrange(start, stop, step))
        expected = len(xrange(start, stop, step))
        self.assertEqual(expected, actual)

    def test_xrange_len(self):
        self.len_check(1, 2, 2)
        self.len_check(1, 1, 1)
        self.len_check(-1, -2, -2)
        self.len_check(-1, -1, -1)
        self.len_check(40, 60, 2)
        self.len_check(40, 20, 2)
        self.len_check(40, 20, -2)
        self.len_check(40, 60, -2)
        self.len_check(-40, -60, 2)
        self.len_check(-40, -20, 2)
        self.len_check(-40, -20, -2)
        self.len_check(-40, -60, -2)
        for i in range(1, 100):
            try:
                self.len_check(*self.randargs(3))
            except ValueError:
                # don't care about step not equal zero exc
                pass

    def iter_check(self, start, stop, step):
        actual = list(Xrange(start, stop, step))
        expected = list(xrange(start, stop, step))
        self.assertEqual(expected, actual)

    def test_xrange_iter(self):
        self.iter_check(1, 20, 2)
        self.iter_check(100, 100, 40)
        self.iter_check(40, 20, 2)
        self.iter_check(-31, -400, -22)
        self.iter_check(-31, 220, -42)
        self.iter_check(151, 20, 2)
        for i in range(1, 100):
            try:
                self.iter_check(*self.randargs(3))
            except ValueError:
                # don't care about step not equal zero exc
                pass

    def contains_check(self, start, stop, step, value):
        self.assertEqual(value in xrange(start, stop, step), value in Xrange(start, stop, step), "%d %d %d %d" % (start, stop, step, value))

    def test_xrange_contains(self):
        self.contains_check(0, 2, -8, -8)
        for i in range(1, 100):
            try:
                self.contains_check(*self.randargs(4))
            except ValueError:
                # don't care about step not equal zero exc
                pass

    def randargs(self, count):
        args = []
        for x in range(0, count):
            args.append(randint(-10, 10))
        return args