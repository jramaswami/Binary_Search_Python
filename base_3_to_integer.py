"""
binarysearch.com :: Base 3 to Integer
jramaswami
"""


class Solution:
    def solve(self, s):
        soln = 0
        mult = 1
        for c in reversed(s):
            soln += (mult * int(c))
            mult *= 3
        return soln


def test_1():
    assert Solution().solve("10") == 3

def test_2():
    assert Solution().solve("21") == 7