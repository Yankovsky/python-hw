import unittest
from erat import eratosthenes_sieve

class TestEratDecorator(unittest.TestCase):
    def test_eratosthenes_sieve(self):
        self.assertEqual([2], eratosthenes_sieve(3))
        self.assertEqual([2, 3], eratosthenes_sieve(4))
        self.assertEqual([2, 3], eratosthenes_sieve(5))
        self.assertEqual([2, 3, 5], eratosthenes_sieve(7))
        self.assertEqual([2, 3, 5, 7], eratosthenes_sieve(10))
        self.assertEqual(self.brute_force(100), eratosthenes_sieve(100))
        self.assertEqual(self.brute_force(1000), eratosthenes_sieve(1000))
        self.assertEqual(self.brute_force(9967), eratosthenes_sieve(9967))

    def brute_force(self, upto):
        primes = []
        for i in range(2, upto):
            if all(i % j != 0 for j in range(2, i)):
                primes.append(i)
        return primes
