"""
binarysearch.com :: Manipulate Bits To Zero
jramaswami


OEIS search yields A006068: a(n) is Gray-coded into n.
https://oeis.org/A006068
"""


def A006068(n):
    """OEIS code."""
    s = 1
    while True:
        ns = n >> s
        if ns == 0:
            return n
        n = n ^ ns
        s <<= 1


class Solution:
    def solve(self, num):
        # return solve0(num)
        return A006068(num)


def test_1():
    assert Solution().solve(6) == 4


def test_2():
    assert Solution().solve(3) == 2


def test_3():
    assert Solution().solve(174781) == 209705


def test_4():
    """TLE"""
    n = 2147483647
    assert Solution().solve(n) == 1431655765