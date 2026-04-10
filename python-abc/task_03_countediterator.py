#!/usr/bin/python3


class CountedIterator:
    """Iterator that counts number of accessed items"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # StopIteration avtomatik qalxacaq
        self.count += 1
        return item

    def get_count(self):
        return self.count
