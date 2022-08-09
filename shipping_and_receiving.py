"""
binarysearch.com :: Shipping and Receiving
jramaswami
"""


import math


class Solution:

    def solve(self, ports, shipments):
        # Make adjacency matrix.
        adj = [[math.inf for _ in ports] for _ in ports]
        for a, dest in enumerate(ports):
            for b in dest:
                adj[a][b] = 1

        # Floyd Warshall
        for k, _ in enumerate(ports):
            for i, _ in enumerate(ports):
                for j, _ in enumerate(ports):
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

        soln = 0
        for a, b in shipments:
            if adj[a][b] < math.inf:
                soln += adj[a][b]
        return soln


def test_1():
    ports = [ [2, 3], [2], [1, 0], [4], [] ]
    shipments = [ [2, 4] ]
    expected = 3
    assert Solution().solve(ports, shipments) == expected
