"""
binarysearch.com :: Split Product
jramaswami
"""


class Solution:
    def solve(self, n):
        if n < 3:
            # (1; 1 or 1 + 1; 1 * 1)
            return 1
        if n == 3:
            # (2 + 1; 2 * 1)
            return 2
        soln = 1
        while n > 4:
            n -= 3
            soln *= 3
        return soln * n


def test_1():
    n = 11
    expected = 54
    assert Solution().solve(n) == expected
