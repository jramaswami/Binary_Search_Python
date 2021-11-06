"""
binarysearch.com :: Detecting an Odd Length Cycle
jramaswami
"""


import collections


class Solution:
    def solve(self, graph):
        # REF: https://en.wikipedia.org/wiki/Bipartite_graph
        # A bipartite graph is a graph that does not contain any
        # odd-length cycles.

        if graph:
            color = [0 for _ in graph]
            # BFS from every uncolored node.
            for root, _ in enumerate(graph):
                if color[root] == 0:
                    color[root] = 1
                    queue = collections.deque([root])
                    while queue:
                        node = queue.popleft()
                        neighbor_color = color[node] * -1
                        for neighbor in graph[node]:
                            if color[neighbor] == 0:
                                color[neighbor] = neighbor_color
                                queue.append(neighbor)
                            elif color[neighbor] == color[node]:
                                # Not a bipartite graph; graph has odd-length cycle.
                                return True
        return False


def test_1():
    graph = [[1], [0]]
    expected = False
    assert Solution().solve(graph) == expected


def test_2():
    graph = [
        [1, 2, 3],
        [0, 2],
        [0, 1, 3],
        [0, 2]
    ]
    expected = True
    assert Solution().solve(graph) == expected


def test_3():
    graph = []
    expected = False
    assert Solution().solve(graph) == expected


def test_4():
    """WA"""
    graph = [
        [],
        [2, 3],
        [1, 3],
        [1, 2]
    ]
    expected = True
    assert Solution().solve(graph) == expected
