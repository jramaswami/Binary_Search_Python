"""
binarysearch.com :: Reflected Binary Code
jramaswami

REF: https://cp-algorithms.com/algebra/gray-code.html
"""


class Solution:
    def solve(self, n):
        return n ^ (n >> 1)


def test_1():
    assert Solution().solve(3) == 2


def test_2():
    assert Solution().solve(13) == 11
