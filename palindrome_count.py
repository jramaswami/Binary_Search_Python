"""
binarysearch.com :: Palindrome Count
jramaswami
"""

class Solution:
    def solve(self, S, k):
        T = set(S)
        soln = 1
        left = 0
        right = k - 1
        while left <= right:
            soln *= len(T)
            left += 1
            right -= 1
        return soln


def test_1():
    s = "ab"
    k = 4
    expected = 4
    assert Solution().solve(s, k) == expected


def test_2():
    s = "ab"
    k = 5
    expected = 8
    assert Solution().solve(s, k) == expected
