"""
binarysearch.com :: Factory Trail
jramaswami
"""

class Solution:
    def solve(self, n):
        k = 5
        soln = 0
        while k <= n:
            soln += (n // k)
            k *= 5
        return soln


def test_1():
    assert Solution().solve(5) == 1


def test_2():
    assert Solution().solve(3) == 0


def test_2():
    assert Solution().solve(1001) == 249