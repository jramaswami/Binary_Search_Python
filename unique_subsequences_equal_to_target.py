"""
binarysearch.com :: Unique Subsequences Equal to Target
jramaswami
"""


MOD = pow(10, 9) + 7


class Solution:

    def solve(self, S, T):
        # Corner case.
        if T == "":
            return 0

        # DP: columns are S, rows are T.
        dp = [[0 for _ in S] for _ in T]

        # Initialize first row as 1 for every T[0] in S.
        for i, c in enumerate(S):
            if c == T[0]:
                dp[0][i] = 1

        # Now DP.
        for r, curr_c in enumerate(T[1:], start=1):
            running = 0
            for c, val in enumerate(dp[r]):
                if S[c] == curr_c:
                    dp[r][c] = running
                running = (running + dp[r-1][c]) % MOD

        soln = 0
        for k in dp[-1]:
            soln = (soln + k) % MOD
        return soln


def test_1():
    S = "ello"
    T = "el"
    expected = 2
    assert Solution().solve(S, T) == expected


def test_2():
    "WA"
    S = "hello"
    T = ""
    expected = 0
    assert Solution().solve(S, T) == expected


def test_3():
    S = "itmsanjvabhkadrhgbqujzukrbmausyxaxpucjhbakicbfcgtyrhzeziyidavzombofrbcjfqsqobgcioghtchzkotusyrisczulhlgfwpkbhceyittmaxvfskpgkbhhcofoxnyyomnotrcyjpogdlqajlrspztofiwibarllpidqgsokqtuksleohttjqsqnoqfrpyguyhtekhsovdvtlmwggdingehlhnubgsjfjzacrsobhybvnmtlgzsfrraddaylvsggmykhqdawuzpikgaadrovzdrisugqmqdvhwlbficvrbekq"

    T = "ijbuyfftzgheaibalsfhvrydaadl"
    expected = 2633472
    assert Solution().solve(S, T) == expected