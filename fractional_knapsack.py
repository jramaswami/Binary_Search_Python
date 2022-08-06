"""
binarysearch.com :: Fractional Knapsack
jramaswami
"""


class Solution:

    def solve(self, weights, values, capacity):
        soln = 0
        t = [(v / w, w, v) for v, w in zip(values, weights)]
        t.sort(reverse=True)
        for ratio, weight, value in t:
            if weight >= capacity:
                soln += ratio * capacity
                break
            else:
                soln += value
                capacity -= weight
        return int(soln)


def test_1():
    weights = [5, 6, 2]
    values = [100, 100, 1]
    capacity = 8
    expected = 150
    assert Solution().solve(weights, values, capacity) == expected


def test_2():
    weights = [5, 6, 2]
    values = [100, 100, 1]
    capacity = 13
    expected = 201
    assert Solution().solve(weights, values, capacity) == expected
