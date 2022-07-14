"""
binarysearch.com :: Range Query on Two Dimensional List
jramaswami
"""


class RangeSumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefix = [[0 for _ in row] for row in matrix]

        for r, row in enumerate(self.prefix):
            for c, _ in enumerate(row):
                self.prefix[r][c] = (
                    self.matrix[r][c] +
                    self._get_prefix(r-1,c) +
                    self._get_prefix(r, c-1) -
                    self._get_prefix(r-1,c-1)
                )

    def _get_prefix(self, r, c):
        if r < 0 or c < 0 or r >= len(self.prefix) or c >= len(self.prefix[r]):
            return 0
        return self.prefix[r][c]

    def total(self, r0, c0, r1, c1):
        return (
            self._get_prefix(r1, c1) -
            self._get_prefix(r0-1, c1) -
            self._get_prefix(r1, c0-1) +
            self._get_prefix(r0-1, c0-1)
        )


def test_1():
    methods = ["constructor", "total", "total"]
    arguments = [[[[1, 2, 3], [4, 5, 6]]], [0, 0, 1, 1], [0, 1, 0, 2]]
    expected = [None, 12, 5]
    rsm = RangeSumMatrix(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(rsm, m)(*a) == e
