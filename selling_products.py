"""
binarysearch.com :: Selling Products
jramaswami
"""


from collections import Counter


class Solution:
    def solve(self, items, n):
        items0 = sorted((freq, key) for key, freq in Counter(items).items())
        soln = len(items0)
        for freq, item in items0:
            if freq > n:
                break
            soln -= 1
            n -= freq
        return soln


def test_1():
    items = [1, 1, 1, 0, 0]
    n = 2
    assert Solution().solve(items, n) == 1


def test_2():
    items = [0, 0, 1, 1, 2, 3]
    n = 2
    assert Solution().solve(items, n) == 2
