class Xrange:
    """
    Xrange reimplementation
    Currently supports only int type for start, stop and step.
    """
    def __init__(self, *args):
        if len(args) == 1:
            start, stop, step = 0, args[0], 1
        elif len(args) == 2:
            start, stop, step = args[0], args[1], 1
        elif len(args) == 3:
            start, stop, step = args
        else:
            raise TypeError("Xrange() requires 1-3 int arguments")

        if not all(isinstance(x, (int, long)) for x in [start, stop, step]):
            raise TypeError("integer argument expected, got float")

        if start < stop and step < 0 or start > stop and step > 0:
            stop = start

        if not step:
            raise ValueError("Xrange() arg 3 must not be zero")

        if step < 0:
            stop = min(stop, start)
        else:
            stop = max(stop, start)

        self._start = start
        self._stop = stop
        self._step = step
        q, r = divmod((stop - start), step)
        if not r:
            self._len = q
        else:
            self._len = q + 1



    def __repr__(self):
        return "%s(%r, %r, %r)" % (self.__class__.__name__,
                                   self._start, self._stop, self._step)

    def __str__(self):
        return "%s(%r, %r, %r)" % (self.__class__.__name__,
                                   self._start, self._stop, self._step)

    def __len__(self):
        return self._len

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)
            return list(Xrange(self._value_by_index(start), self._value_by_index(stop), step * self._step))
        elif isinstance(index, (int, long)):
            if index < 0:
                index = self._len - index
            else:
                index = index

            if index < 0 or index >= self._len:
                raise IndexError("Xrange object index out of range")

            return self._value_by_index(index)
        else:
            raise TypeError("sequence index must be integer, not '%s'") % (type(index))

    def _value_by_index(self, i):
        return self._start + self._step * i

    def __contains__(self, value):
        quotient, remainder = divmod(value - self._start, self._step)
        return remainder == 0 and 0 <= quotient < self._len

    def __eq__(self, other):
        return isinstance(other, xrange) and\
               self._start == other._start and\
               self._stop == other._stop and\
               self._step == other._step