"""
binarysearch.com :: Recurring Character
jramaswami
"""


class Solution:
    def solve(self, s):
        first = set()
        for i, c in enumerate(s):
            if c in first:
                return i
            first.add(c)
        return -1


def test_1():
    s = "abcda"
    expected = 4
    assert Solution().solve(s) == expected


def test_2():
    s = "abcde"
    expected = -1
    assert Solution().solve(s) == expected


def test_3():
    s = "aaaaa"
    expected = 1
    assert Solution().solve(s) == expected


def test_4():
    s = ""
    expected = -1
    assert Solution().solve(s) == expected
