"""
binarysearch.com :: Two-Dimensional List Iterator
jramaswami
"""


import itertools


class TwoDimensionalIterator:
    def __init__(self, lists):
        self.iterator = itertools.chain(*lists)
        self.next_item = None
        self._advance()

    def _advance(self):
        try:
            self.next_item = next(self.iterator)
        except StopIteration:
            self.next_item = None

    def next(self):
        x = self.next_item
        self._advance()
        return x

    def hasnext(self):
        return self.next_item is not None
