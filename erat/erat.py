from math import ceil
from operator import sub
from itertools import chain

def eratosthenes_sieve(upto):
    """
    Fully functional implementation of eratosthenes sieve
    Upto - exclusive upper limit. So eratosthenes_sieve(7) = [2,3,5]
    """
    return sorted(reduce(sub, [set(range(x * x, upto, 2 * x)) for x in range(3, int(ceil(upto ** 0.5)), 2)], set(chain([2], set(range(3, upto, 2))))))