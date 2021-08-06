"""
binarysearch.com :: 0-1 Knapsack
jramaswami
"""


import math
import collections


class Solution:
    def solve(self, weights, values, capacity):
        prev_dp = [-math.inf for _ in range(capacity+1)]
        prev_dp[0] = 0
        curr_dp = list(prev_dp)

        for w, v in zip(weights, values):
            # For every existing weight that is possible so far ...
            for i, k in enumerate(prev_dp):
                if k < 0:
                    continue
                # If adding the weight of the current item is less than or
                # equal to the capacity of the knapsack ...
                curr_dp[i] = max(prev_dp[i], curr_dp[i])
                if w + i <= capacity:
                    # the maximum value possible for the new weight is either
                    # the current value for the new weight, or the value of
                    # the previous weight plus the weight of the item.
                    curr_dp[w + i] = max(prev_dp[w + i], k + v)

            curr_dp, prev_dp = [-math.inf for _ in prev_dp], curr_dp
        return max(prev_dp)


def test_1():
    weights = [1, 2, 3]
    values = [1, 5, 3]
    capacity = 5
    expected = 8
    assert Solution().solve(weights, values, capacity) == expected
