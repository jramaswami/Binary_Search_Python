"""
binarysearch.com :: Wallstreet Bets
jramaswami
"""
class Solution:
    def solve(self, prices):
        Q = []
        soln = [0 for _ in prices]
        for i, p in enumerate(prices):
            while Q and Q[-1][0] < p:
                p0, i0 = Q.pop()
                soln[i0] = i - i0
            Q.append((p, i))
        return soln

def test_1():
    prices = [3, 2, 4, 8, 6, 5]
    assert Solution().solve(prices) == [2, 1, 1, 0, 0, 0]
