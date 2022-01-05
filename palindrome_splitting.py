"""
binarysearch.com :: Palindrome Splitting
jramaswami
"""


from functools import cache


class Solution:

    def solve(self, s):

        @cache
        def is_palindrome(left, right):
            "Return True if s[left:right+1] is a palindrome."
            if left >= right:
                return True

            if s[left] == s[right]:
                return is_palindrome(left + 1, right - 1)

            return False

        def solve0(left):
            if left >= len(s):
                return 1

            result = 0
            for right in range(left, len(s)):
                if is_palindrome(left, right):
                    result += solve0(right+1)
            return result

        return solve0(0)


def test_1():
    s = "abba"
    assert Solution().solve(s) == 3


def test_2():
    s = "a" * 15
    assert Solution().solve(s) == 3
