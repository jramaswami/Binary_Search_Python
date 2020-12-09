"""
binarysearch.com :: A Flight of Stairs
https://binarysearch.com/problems/A-Flight-of-Stairs
"""
MOD = pow(10, 9) + 7


class Solution:
    def solve(self, n):
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for stair in range(n+1):
            if stair+1 <= n:
                dp[stair+1] = (dp[stair] + dp[stair+1]) % MOD
            if stair+2 <= n:
                dp[stair+2] = (dp[stair] + dp[stair+2]) % MOD
        return dp[-1]


def test_1():
    solver = Solution()
    assert solver.solve(4) == 5

def test_2():
    solver = Solution()
    assert solver.solve(1) == 1

def test_3():
    solver = Solution()
    assert solver.solve(3) == 3
