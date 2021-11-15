"""
binarysearch.com :: Rocketship Rescue
jramaswami
"""


class Solution:
    def solve(self, weights, limit):
        total = sum(weights)
        soln = 0
        while total:
            soln += 1
            rocketship = limit
            for i, w in enumerate(weights):
                if w <= rocketship:
                    rocketship -= w
                    weights[i] = 0
                    total -= w
                    if rocketship == 0 or total == 0:
                        break
        return soln


def test_1():
    weights = [200, 300, 200]
    limit = 400
    expected = 2
    assert Solution().solve(weights, limit) == expected


def test_2():
    """WA"""
    weights = [1, 1, 1, 3]
    limit = 3
    expected = 3
    assert Solution().solve(weights, limit) == expected