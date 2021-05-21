"""
binarysearch.com :: Look and Say
jramaswami
"""


def look_and_say(s):
    """Return the look and say for the string s."""
    prev = s[0]
    freq = 1
    soln = []
    for curr in s[1:]:
        if curr != prev:
            soln.append(str(freq))
            soln.append(prev)
            prev = curr
            freq = 1
        else:
            freq += 1
    soln.append(str(freq))
    soln.append(prev)
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
