from math import ceil
from operator import sub
from itertools import chain

def eratosthenes_sieve(upto):
    """
    Fully functional implementation of eratosthenes sieve
    Upto - exclusive upper limit. So eratosthenes_sieve(7) = [2,3,5]
    """
    return sorted(reduce(sub, [set(xrange(x * x, upto, 2 * x)) for x in xrange(3, int(ceil(upto ** 0.5)), 2)], set(chain([2], xrange(3, upto, 2)))))