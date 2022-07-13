"""
binarysearch.com :: Largest Kth Value of List
jramaswami
"""


class Solution:
    def solve(self, n, total, k):

        def S(x):
            return (x * (x + 1)) // 2

        # Let x be the largest value at the kth place.
        # ... (x - 2) + (x - 1) + x + (x - 1) + (x - 2) ... = total
        # There are k elements to the left of k. (Zero based.)
        # There are n - k - 1 elements to the right of k.
        # nx - (k + ... + 2 + 1) - ((n - k - 1) + ... + 2 + 1) = total
        # nx = total + S(k) + S(n-k-1) where S(t) is summation of 1 to t.
        return (total + S(k) + S(n - k - 1)) // n


def test_1():
    n = 3
    total = 10
    k = 1
    expected = 4
    assert Solution().solve(n, total, k) == expected


def test_2():
    n = 4
    total = 10
    k = 3
    expected = 4
    assert Solution().solve(n, total, k) == expected
