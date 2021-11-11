"""
binarysearch.com :: Currency Arbitrage
jramaswami

REF: https://medium.com/swlh/arbitrage-as-a-shortest-path-problem-d8d3ee18c080
REF: https://www.youtube.com/watch?v=lyw4FaxrwHg

A sequence of trades can be thought of as the a path in a graph where the
result of the trades is the product of the edge weights.  We are looking
for a negative cycle, which represents an opportunity to make a profit.

We must, however, transform the problem in order to make use of known
graph algorithms.  We can use logarithms to transform the result of the
trade into a sum where a profit is indicated by a sum greater than 0.  We
can further transform the problem by multiplying the edge weights by negative
one.  This will allows us to use the Bellman-Ford algorithm to find a negative
cycle.
"""


import math


class Solution:

    def solve(self, matrix):
        # Transform edge weights into -log(e[i]).
        cost = [[-math.log(e) for e in row] for row in matrix]

        # Bellman-Ford to find any negative cycle.
        def negative_cycle_from(root):
            node_count = len(matrix)
            dist = [math.inf for _ in matrix]
            dist[root] = 0
            # Do node_count - 1 relaxations.
            for _ in range(node_count-1):
                # Iterate over every edge.
                for node_from in range(node_count-1):
                    for node_to in range(node_count):
                        # edge(node_from, node_to)
                        if dist[node_from] + cost[node_to][node_from] < dist[node_to]:
                            dist[node_to] = dist[node_from] + cost[node_to][node_from]

            # Repeat to find any negative cycles.
            for _ in range(node_count-1):
                # Iterate over every edge.
                for node_from in range(node_count-1):
                    for node_to in range(node_count):
                        # edge(node_from, node_to)
                        if dist[node_from] + cost[node_to][node_from] < dist[node_to]:
                            return True

            return False

        return any(negative_cycle_from(r) for r, _ in enumerate(matrix))


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


def test_4():
    """WA"""
    matrix = [
        [1, 2.5],
        [0.41, 1]
    ]
    expected = True
    assert Solution().solve(matrix) == expected