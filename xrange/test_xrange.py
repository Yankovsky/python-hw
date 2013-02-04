from random import randint
import unittest
from xrange import Xrange

class TestXrange(unittest.TestCase):
    def len_assert(self, start, stop, step):
        expected = len(xrange(start, stop, step))
        actual = len(Xrange(start, stop, step))
        self.assertEqual(expected, actual, "%d != %d: %d %d %d" % (expected, actual, start, stop, step))

    def iter_assert(self, start, stop, step):
        expected = list(xrange(start, stop, step))
        actual = list(Xrange(start, stop, step))
        self.assertEqual(expected, actual, "%s %s %d %d %d" % (expected, actual, start, stop, step))

    def contains_assert(self, start, stop, step, value):
        expected = value in xrange(start, stop, step)
        actual = value in Xrange(start, stop, step)
        self.assertEqual(expected, actual, "%s %s %d %d %d %d" % (expected, actual, start, stop, step, value))

    def slice_assert(self, start, stop, step, new_start, new_stop, new_step):
        expected = range(start, stop, step)[new_start:new_stop:new_step]
        actual = Xrange(start, stop, step)[new_start:new_stop:new_step]
        self.assertEqual(expected, actual, "%s %s %d %d %d %d %d %d" % (expected, actual, start, stop, step, new_start, new_stop, new_step))

    def index_assert(self, start, stop, step, index):
        expected = xrange(start, stop, step)[index]
        actual = Xrange(start, stop, step)[index]
        self.assertEqual(expected, actual, "%s %s %d %d %d %d" % (expected, actual, start, stop, step, index))

    def randargs(self, count):
        args = []
        for x in range(0, count):
            args.append(randint(0, 10))
        return args

    def test_xrange_len(self):
        for i in range(1, 1000):
            try:
                self.len_assert(*self.randargs(3))
            except ValueError:
                # don"t care about step not equal zero exc
                pass

    def test_xrange_iter(self):
        for i in range(1, 1000):
            try:
                self.iter_assert(*self.randargs(3))
            except ValueError:
                # don"t care about step not equal zero exc
                pass

    def test_xrange_contains(self):
        for i in range(1, 1000):
            try:
                self.contains_assert(*self.randargs(4))
            except ValueError:
                # don"t care about step not equal zero exc
                pass

    def test_xrange_slice(self):
        for i in range(1, 1000):
            try:
                self.slice_assert(*self.randargs(6))
            except ValueError:
                # don"t care about step not equal zero exc
                pass

    def test_xrange_index(self):
        for i in range(1, 1000):
            try:
                self.index_assert(*self.randargs(4))
            except (ValueError, IndexError):
                # don"t care about step not equal zero exc
                pass