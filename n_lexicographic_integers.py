"""
binarysearch.com :: N Lexicographic Integers
jramaswami
"""


import functools


@functools.total_ordering
class Digits:

    def __init__(self, x: int):
        self.digits = []
        self.x = x
        while x:
            x, r = divmod(x, 10)
            self.digits.append(r)
        self.digits = self.digits[::-1]

    def __lt__(self, other) -> bool:
        for a, b in zip(self.digits, other.digits):
            if a < b:
                return True
            elif a > b:
                return False
        return len(self.digits) < len(other.digits)

    def __repr__(self):
        return f"Digits({self.digits}, {self.x}"

    def __eq__(self, other) -> bool:
        return self.digits == other.digits


class Solution:

    def solve(self, n):
        return [t.x for t in sorted(Digits(k) for k in range(1, n+1))]

def test_1():
    n = 12
    expected = [1, 10, 11, 12, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution().solve(n) == expected