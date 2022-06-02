"""
binarysearch.com :: Knight Remains
jramaswami
"""


class Solution:

    MOVES = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))

    def solve(self, n, x, y, k):

        def inbounds(x, y):
            return x >= 0 and x < n and y >= 0 and y < n

        def neighbors(x, y):
            for dx, dy in Solution.MOVES:
                x0, y0 = x + dx, y + dy
                if inbounds(x0, y0):
                    yield x0, y0

        # dp[steps][x][y] = number of ways to reach in i steps.
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]
        dp[0][x][y] = 1

        for i in range(k):
            for x0 in range(n):
                for y0 in range(n):
                    for x1, y1 in neighbors(x0, y0):
                        dp[i+1][x1][y1] += dp[i][x0][y0]

        t = sum(sum(row) for row in dp[-1])
        return int(100 * (t / pow(8, k)))



def test_1():
    n = 8
    x = 0
    y = 0
    k = 1
    expected = 25
    assert Solution().solve(n, x, y, k) == expected


def test_2():
    n = 25
    x = 0
    y = 0
    k = 100
    expected = 0
    assert Solution().solve(n, x, y, k) == expected


def test_3():
    "TLE"
    n = 24
    x = 20
    y = 23
    k = 20
    expected = 6
    assert Solution().solve(n, x, y, k) == expected
