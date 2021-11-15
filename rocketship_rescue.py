"""
binarysearch.com :: Rocketship Rescue
jramaswami
"""


class Solution:
    def solve(self, weights, limit):
        weights0 = sorted(weights)
        soln = 0
        while weights0:
            # Remove any already used weights (over limit).
            while weights0 and weights0[-1] > limit:
                weights0.pop()

            if weights0:
                soln += 1
                # Take the largest weight
                rocketship = limit - weights0.pop()
                # Take the next largest weight that fits.
                for i in range(len(weights0) - 1, -1, -1):
                    if weights0[i] <= rocketship:
                        weights0[i] = limit + 1
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


def test_3():
    weights = [1, 1, 2, 2]
    limit = 3
    expected = 2
    assert Solution().solve(weights, limit) == expected