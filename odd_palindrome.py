"""
binarysearch.com :: Odd Palindrome
jramaswami
"""


class Solution:

    def solve(self, s):
        # If a string has an even length palindrome, it must have a
        # palindrome of length 2.
        for i, _ in enumerate(s[:-1]):
            if s[i] == s[i+1]:
                return False
        return True


def test_1():
    s = "bab"
    expected = True
    assert Solution().solve(s) == expected


def test_2():
    s = "aa"
    expected = False
    assert Solution().solve(s) == expected