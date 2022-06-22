"""
binarysearch.com :: Lexicographically Smallest Non-Palindromic String
jramaswami
"""


class Solution:
    def solve(self, s):
        first_down_index = -1
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != 'a':
                first_down_index = left
                return s[:left] + 'a' + s[left+1:]
            left += 1
            right -= 1
        next_char = chr(ord(s[-1])+1)
        return s[:-1] + next_char


def test_1():
    s = "racecar"
    expected = "aacecar"
    assert Solution().solve(s) == expected


def test_2():
    s = "aaaaa"
    expected = "aaaab"
    assert Solution().solve(s) == expected


def test_3():
    "WA"
    s = "aba"
    expected = "abb"
    assert Solution().solve(s) == expected
