"""
binarysearch.com :: Multi Knapsack
jramaswami
"""


import functools


class Solution:

    def solve(self, weights, values, capacity, count):

        @functools.cache
        def solve0(i, acc_w, acc_c):
            if i >= len(weights):
                return 0

            # Do not choose this item.
            result = solve0(i + 1, acc_w, acc_c)
            if acc_w + weights[i] <= capacity and acc_c + 1 <= count:
                result = max(
                    result,
                    values[i] + solve0(i + 1, acc_w + weights[i], acc_c + 1)
                )
            return result

        return solve0(0, 0, 0)


def test_1():
    weights = [1, 1, 3, 5]
    values = [10, 10, 20, 30]
    capacity = 5
    count = 3
    expected = 40
    assert Solution().solve(weights, values, capacity, count) == expected
