"""
binarysearch.com :: Edges that Disconnect the Graph
jramaswami

REF: https://cp-algorithms.com/graph/bridge-searching.html
"""


class Graph:

    def __init__(self, adj):
        self.adj = adj
        self.timer = 0
        self.time_in = []
        self.low = []
        self.visited = []
        self.bridges = 0

    def find_bridges(self):
        self.timer = 0
        self.time_in = [-1 for _ in self.adj]
        self.low = [-1 for _ in self.adj]
        self.visited = [False for _ in self.adj]
        self.bridges = 0
        self._dfs(0, -1)

    def _dfs(self, node, parent):
        self.visited[node] = True
        self.time_in[node] = self.low[node] = self.timer
        self.timer += 1
        for neighbor in self.adj[node]:
            if neighbor == parent:
                continue
            if self.visited[neighbor]:
                self.low[node] = min(self.low[node], self.time_in[neighbor])
            else:
                self._dfs(neighbor, node)
                self.low[node] = min(self.low[node], self.low[neighbor])
                if self.low[neighbor] > self.time_in[node]:
                    self.bridges += 1


class Solution:

    def solve(self, adj):
        graph = Graph(adj)
        graph.find_bridges()
        return graph.bridges


def test_1():
    graph = [
        [1, 2, 3, 5],
        [0],
        [0, 3],
        [0, 2, 4],
        [3],
        [0]
    ]
    assert Solution().solve(graph) == 3
