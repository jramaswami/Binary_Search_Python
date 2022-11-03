"""
binarysearch.com :: Weekly Contest 26 :: Consecutive Wins
"""
MOD = pow(10, 9) + 7

# At any step you can
# (1) add a L to the end,
# (2) add a W to the end.
# If you add a L to the end you have zero consecutive Ws immediately preceding
# the next addition.
# If you add a W, then you have 1 + the number of immediately preceding
# consective Ws.
# Note: you cannot add a W when there are already k Ws immediately preceding
# the new game.

# DP
# -----> length of string
# |
# |
# |
# v
# the number of preceding zeros

class Solution:
    def solve(self, n, k):
        dp = [[0 for _ in range(n+1)] for _ in range(k + 1)]
        dp[0][0] = 1
        for length in range(1, n+1):
            for wins in range(k+1):
                if dp[wins][length-1] == 0:
                    continue
                if wins == k:
                    # You cannot add a win.
                    dp[0][length] = (dp[0][length] + dp[wins][length-1]) % MOD
                else:
                    # Add a win.
                    dp[wins+1][length] = (dp[wins+1][length] + dp[wins][length-1]) % MOD
                    # Add a loss to this.
                    dp[0][length] = (dp[0][length] + dp[wins][length-1]) % MOD
        
        soln = 0
        for row in dp:
            soln = (soln + row[-1]) % MOD
        return soln % MOD



def test_1():
    solver = Solution()
    assert 7 == solver.solve(3, 2)


def test_2():
    solver = Solution()
    assert 64256 == solver.solve(16, 7)
