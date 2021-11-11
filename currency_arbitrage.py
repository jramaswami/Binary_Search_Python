"""
binarysearch.com :: Currency Arbitrage
jramaswami

REF: https://medium.com/swlh/arbitrage-as-a-shortest-path-problem-d8d3ee18c080

A sequence of trades can be thought of as the a path in a graph where the
result of the trades is the product of the edge weights.  We are looking
for a path where that product is greater than one and thus turns a profit.
We must, however, transform the problem in order to make use of known
graph algorithms.  We can use logarithms to transform the result of the
trade into a sum where a profit is indicated by a sum greater than 0.  We
can further transform the problem by multiplying the edge weights by nefative
one.  This will make our problem one of finding any shortest path that is less
than zero.  We can use the Bellman-Ford algorithm to solve our problem.
"""


import math


class Solution:

    def solve(self, matrix):
        # Transform edge weights into -log(e[i]).
        matrix0 = [[-math.log(e) for e in row] for row in matrix]

        # Bellman-Ford to find any negative paths.
        node_count = len(matrix)
        for r in range(node_count):
            dist = [math.inf for _ in matrix]
            dist[r] = 0
            for i in range(node_count):
                for j in range(i+1, node_count):
                    # edge(i, j)
                    if dist[i] < math.inf:
                        dist[j] = min(dist[j], dist[i] + matrix0[i][j])

            # Are there any negative weight (profitable) paths starting at r?
            print(f"{r=} {dist=}")
            if any(d < 0 for d in dist):
                return True

        return False


def test_1():
    matrix = [
        [1, 1.32, 0.9],
        [0.76, 1, 0.72],
        [1.11, 1.47, 1]
    ]
    expected = True
    assert Solution().solve(matrix) == True


def test_2():
    matrix = [
        [1, 0.726, 0.6139],
        [1.3773, 1, 0.8456],
        [1.6287, 1.1825, 1]
    ]
    expected = False
    assert Solution().solve(matrix) == expected


def test_3():
    """WA"""
    matrix = [
        [1, 2.5],
        [0.39, 1]
    ]
    expected = False
    assert Solution().solve(matrix) == expected