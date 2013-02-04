import unittest
from operator import add
from ireduce import ireduce

class TestReduce(unittest.TestCase):
    def compare_reduce_and_ireduce_results_without_initial(self, func, sequence):
        ireduce_iterator = ireduce(func, sequence)
        n = len(sequence)
        if n == 1:
            expected = reduce(func, sequence)
            actual = ireduce_iterator.next()
            self.assertEquals(expected, actual)
        else:
            ireduce_iterator.next()
            for i in range(1, n - 1):
                expected = reduce(func, sequence[0:i + 1])
                actual = ireduce_iterator.next()
                self.assertEqual(expected, actual)

    def compare_reduce_and_ireduce_results_with_initial(self, func, sequence, initial):
        ireduce_iterator = ireduce(func, sequence, initial)
        n = len(sequence)
        if n == 1:
            expected = reduce(func, sequence, initial)
            actual = ireduce_iterator.next()
            self.assertEquals(expected, actual)
        else:
            ireduce_iterator.next()
            for i in range(1, n - 1):
                expected = reduce(func, sequence[0:i + 1], initial)
                actual = ireduce_iterator.next()
                self.assertEqual(expected, actual)

    # Check api of reduce.
    def test_reduce_contract(self):
        none = lambda x, y: None

        self.assertRaises(TypeError, reduce, none, None)
        self.assertRaises(TypeError, reduce, none, [])
        self.assertEqual(1, reduce(none, [1]))
        self.assertEqual(None, reduce(none, [1, 2]))

        self.assertRaises(TypeError, reduce, none, None, 1)
        self.assertEqual(1, reduce(none, [], 1))
        self.assertEqual(None, reduce(none, [1], 2))
        self.assertEqual(None, reduce(none, [1, 2], 4))

        self.assertRaises(TypeError, reduce, add, None)
        self.assertRaises(TypeError, reduce, add, [])
        self.assertEqual(1, reduce(add, [1]))
        self.assertEqual(3, reduce(add, [1, 2]))

        self.assertRaises(TypeError, reduce, add, None, 1)
        self.assertEqual(1, reduce(add, [], 1))
        self.assertEqual(3, reduce(add, [1], 2))
        self.assertEqual(7, reduce(add, [1, 2], 4))

    def test_ireduce_contract(self):
        none = lambda x, y: None

        self.assertRaises(TypeError, ireduce, none, None)
        self.assertRaises(TypeError, ireduce, none, [])
        self.compare_reduce_and_ireduce_results_without_initial(none, [1])
        self.compare_reduce_and_ireduce_results_without_initial(none, [1, 2])
        self.compare_reduce_and_ireduce_results_without_initial(none, [1, 2, 3, 4, 5, 6, 7])

        self.assertRaises(TypeError, ireduce, none, None, 1)
        self.compare_reduce_and_ireduce_results_with_initial(none, [], 1)
        self.compare_reduce_and_ireduce_results_with_initial(none, [1, 2], 4)
        self.compare_reduce_and_ireduce_results_with_initial(none, [1, 2, 3, 4, 5, 6, 7], 8)

        self.assertRaises(TypeError, ireduce, add, None)
        self.assertRaises(TypeError, ireduce, add, [])
        self.compare_reduce_and_ireduce_results_without_initial(add, [1])
        self.compare_reduce_and_ireduce_results_without_initial(add, [1, 2])
        self.compare_reduce_and_ireduce_results_without_initial(add, [1, 2, 3, 4, 5, 6, 7])

        self.assertRaises(TypeError, ireduce, add, None, 1)
        self.compare_reduce_and_ireduce_results_with_initial(add, [], 1)
        self.compare_reduce_and_ireduce_results_with_initial(add, [1, 2], 4)
        self.compare_reduce_and_ireduce_results_with_initial(none, [1, 2, 3, 4, 5, 6, 7], 8)