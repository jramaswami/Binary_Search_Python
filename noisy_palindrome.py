"""
binarysearch.com :: Noisy Palindrome
jramaswami
"""
class Solution:
    def solve(self, s):
        s0 = [c for c in s if c.islower()]
        return s0 == s0[::-1]


def test_1():
    s = "a92bcbXa"
    assert Solution().solve(s) == True

