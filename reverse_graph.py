"""
binarysearch.com :: Reverse Graph
jramaswami
"""
class Solution:
    def solve(self, graph):
        graph0 = [[] for _ in graph]
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                graph0[neighbor].append(node)
        return graph0


def test_1():
    graph = [[1], [2], []]
    expected = [[], [0], [1]]
    assert Solution().solve(graph) == expected
