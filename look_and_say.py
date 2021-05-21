"""
binarysearch.com :: Look and Say
jramaswami
"""
from itertools import groupby


def look_and_say(s):
    """Return the look and say for the string s."""
    soln = []
    for key, grp in groupby(s):
        L = sum(1 for _ in grp)
        soln.append(str(L))
        soln.append(key)
    return "".join(soln)


class Solution:
    def solve(self, n):
        curr = "1"
        for i in range(2, n+1):
            curr = look_and_say(curr)
        return curr


def test_1():
    assert Solution().solve(3) == "21"


def test_2():
    assert Solution().solve(4) == "1211"


def test_3():
    assert Solution().solve(5) == "111221"
