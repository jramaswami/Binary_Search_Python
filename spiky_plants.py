"""
binarysearch.com :: Spiky Plants
jramaswami
"""


import math


class Solution:

    def solve(self, heights, costs):
        # You will increase the height any given plant zero, one, or two times.
        dp = [[math.inf for _ in range(3)] for _ in heights]
        # Base case.
        dp[0][0] = 0
        dp[0][1] = costs[0]
        dp[0][2] = costs[0] * 2

        for i, init_ht in enumerate(heights[1:], start=1):
            # Grow the current tree 0, 1, or 2 ...
            for curr_growth in range(3):
                curr_ht = init_ht + curr_growth
                curr_cost = (curr_growth * costs[i])
                for prev_growth in range(3):
                    # For each possible growth of the previous tree ...
                    prev_ht = heights[i-1] + prev_growth
                    # If the heights are different ...
                    if prev_ht != curr_ht:
                        # The cost of reaching curr_height for tree i is
                        # the cost of growing tree i plus the cost of
                        # the previous tree (i-1) reaching the height of
                        # prev_ht.
                        dp[i][curr_growth] = min(
                            dp[i][curr_growth],
                            curr_cost + dp[i-1][prev_growth]
                        )
        return min(dp[-1])


def test_1():
    heights = [1, 1, 2]
    costs = [3, 1, 7]
    expected = 2
    assert Solution().solve(heights, costs) == expected
