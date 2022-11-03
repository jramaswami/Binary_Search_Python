"""
binarysearch.com :: Integer to Base 3
jramaswami
"""


class Solution:
    def solve(self, n):
        if n == 0:
            return '0'

        soln = []
        while n:
            n, r = divmod(n, 3)
            soln.append(r)

        return "".join(str(i) for i in reversed(soln))


def test_1():
    n = 7
    expected = '21'
    assert Solution().solve(n) == expected


def test_2():
    n = 11
    expected = '102'
    assert Solution().solve(n) == expected


def test_3():
    n = 0
    expected = '0'
    assert Solution().solve(n) == expected

