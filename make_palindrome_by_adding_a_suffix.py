"""
binarysearch.com :: Make Palindrome by Adding a Suffix
jramaswami

REF: https://www.geeksforgeeks.org/print-the-longest-palindromic-prefix-of-a-given-string/
"""


class Solution:
    def solve(self, s):
        t = s[::-1] + "?" + s
        n = len(t)
        lps = [0 for _ in range(n)]
        for i in range(1, n):
            l = lps[i-1]
            while l > 0 and t[l] != t[i]:
                l = lps[l-1]
            if t[i] == t[l]:
                l += 1
            lps[i] = l
        return len(s) - lps[n-1]


def test_1():
    s = "rad"
    expected = 2
    assert Solution().solve(s) == expected
