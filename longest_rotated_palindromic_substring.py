"""
binarysearch.com :: Longest Rotated Palindromic Substring
jramaswami
"""


class Solution:

    def solve(self, S):
        # Boundary cases.
        if not S:
            return 0
        if len(S) == 1:
            return 1

        N = len(S)
        soln = 1
        dp = [[False for _ in range(N * 2)] for _ in range(N+1)]
        # Initialize all substrings of length 1 to true b/c they are
        # all palindromes.
        for i, _ in enumerate(dp[0]):
            dp[1][i] = True
        # Initialize all substrings of length 2 that are palindromes
        # to True.
        for i, _ in enumerate(dp[1][:-1]):
            if S[i % N] == S[(i+1) % N]:
                dp[2][i] = True
                soln = 2

        # For substrings of length 3 to N * 2, use previous computations
        # to determine if substring is palindrome.
        for k, _ in enumerate(dp[3:], start=3):
            for i, _ in enumerate(dp[k][:-k]):
                if S[i % N] == S[(i + k - 1) % N] and dp[k-2][i+1]:
                    dp[k][i] = True
                    soln = max(soln, k)
        return soln


def test_1():
    s = "carzrace"
    expected = 7
    assert Solution().solve(s) == expected


def test_2():
    # WA
    s = "kbbkuxxu"
    expected = 8
    assert Solution().solve(s) == expected
