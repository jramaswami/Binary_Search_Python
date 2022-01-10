"""
binarysearch.com :: Candy Race
jramaswami


REF: https://www.youtube.com/watch?v=WxpIHvsu1RI
"""

class Solution:

    def solve(self, candies):

        dp = [[(0, 0) for _ in candies] for _ in candies]

        # Initialize
        for i, c in enumerate(candies):
            dp[i][i] = (c, 0)

        # Dynamic programming.
        for length in range(2, len(candies)):
            for i in range(0, len(candies) - length):
                j = i + length
                left1 = dp[i+1][j][0] + candies[i]
                right1 = dp[i][j-1][0] + candies[j]
                if left1 > right1:
                    # Player 1 picks the best.  Player 2 gets the rest.
                    dp[i][j] = (left1, dp[i][j-1][1])
                else:
                    dp[i][j] = (right1, dp[i+1][j][1])

        return dp[-1][-1][0] > dp[-1][-1][1]



def test_1():
    candies = [1, 3, 2, 6]
    assert Solution().solve(candies) == True


def test_2():
    "WA"
    candies = [1, 0]
    assert Solution().solve(candies) == True
