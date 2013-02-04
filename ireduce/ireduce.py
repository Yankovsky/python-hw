from functools import wraps

def ireduce(func, sequence, initial=None):
    """
    Make an iterator that apply a function of two arguments cumulatively
    to the items of a sequence, from left to right, so as to reduce
    the sequence to a single value. If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    Like reduce() except that it returns an iterator instead of a result value.
    """

    try:
        iterator = iter(sequence)
    except TypeError:
        raise TypeError("reduce() arg 2 must support iteration")

    if initial is None:
        try:
            accumulator = next(iterator)
        except StopIteration:
            raise TypeError('ireduce() of empty sequence with no initial value')
    else:
        accumulator = initial

    def ireduce_generator(accumulator):
        try:
            temp = next(iterator)

            yield func(accumulator, temp)
        except StopIteration:
            yield accumulator

        for i in iterator:
            accumulator = func(accumulator, i)
            yield accumulator

    return ireduce_generator(accumulator)