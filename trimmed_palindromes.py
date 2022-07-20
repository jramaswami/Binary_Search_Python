"""
binarysearch.com :: Trimmed Palindromes
jramaswami
"""


class Solution:

    def solve(self, S):
        # Boundary cases:
        if len(S) == 0:
            return 0
        if len(S) == 1:
            return 1
        if len(S) == 2:
            if S[0] == S[1]:
                return 3
            return 2

        # dp[length of palindrome][starting index]
        dp = [[False for _ in S] for _ in range(len(S)+1)]
        soln = 0
        # All single letters are palindromes
        for i, _ in enumerate(dp[1]):
            dp[1][i] = True
            soln += 1
        # Double letters as palindromes.
        for i, _ in enumerate(dp[2][:-1]):
            if S[i] == S[i+1]:
                dp[2][i] = True
                soln += 1
        # Remaining length palindromes.
        for k, _ in enumerate(dp[3:], start=3):
            for i, _ in enumerate(dp[k]):
                # A palindrome of length k starts at i if there is a palindrome
                # of size k-2 starting a i+1 and S[i] is the same as S[i+k-1].
                if i+k-1 < len(S) and S[i] == S[i+k-1] and dp[k-2][i+1]:
                    dp[k][i] = True
                    soln += 1
        for row in dp:
            print(row)
        return soln


def test_1():
    S = "bobo"
    expected = 6
    assert Solution().solve(S) == expected