"""
binarysearch.com :: Minimum Spanning Tree
jramaswami
"""


import collections


class UnionFind:
    def __init__(self):
        self.id = dict()
        self.size = dict()

    def add_node(self, u):
        if u not in self.id:
            self.id[u] = u
            self.size[u] = u

    def find(self, u):
        p = self.id[u]
        if p != u:
            self.id[u] = self.find(p)
        return self.id[u]

    def connected(self, u, v):
        return self.find(u) == self.find(v)

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] < self.size[v]:
                u, v = v, u
            self.id[v] = u
            self.size[u] += self.size[v]


class Solution:
    def solve(self, edges, a, b):
        edges.sort(key=lambda e: e[-1])
        # Form the MST
        uf = UnionFind()
        mst = []
        for i, (u, v, w) in enumerate(edges):
            uf.add_node(u)
            uf.add_node(v)
            if not uf.connected(u, v):
                mst.append(i)
                uf.union(u, v)

        # Is a, b in edges?
        for i in mst:
            u, v, _ = edges[i]
            if (a == u and b == v) or (a == v and b == u):
                return True

        # AB edge(s)?
        ab_edge = -1
        for i, (u, v, _) in enumerate(edges):
            if (a == u and b == v) or (a == v and b == u):
                if ab_edge >= 0:
                    raise Exception("There is more than one a-b edge.")
                ab_edge = i

        # Turn mst into a graph.
        graph = collections.defaultdict(list)
        for i in mst:
            u, v, w = edges[i]
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Add the a-b edge.
        graph[a].append((b, edges[ab_edge][-1]))
        graph[b].append((a, edges[ab_edge][-1]))

        # Find the cycle created by adding the ab-edge.
        def find_cycle(parent, node, acc, start):
            if node == start and parent != -1:
                return tuple(acc)
            for neighbor, w in graph[node]:
                if neighbor != parent:
                    acc.append((node, neighbor, w))
                    cycle = find_cycle(node, neighbor, acc, start)
                    acc.pop()
                    if cycle:
                        return cycle
            return None

        # Is there an edge in the cycle that can be replaced, i.e. that is
        # not the a-b edge but has the same weight as the a-b edge.
        cycle = find_cycle(-1, a, [], a)
        for u, v, w in cycle:
            if (a == u and b == v) or (a == v and b == u):
                continue
            if w == edges[ab_edge][-1]:
                return True
        return False


def test_1():
    edges = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 300]
    ]
    a = 0
    b = 2
    expected = False
    assert Solution().solve(edges, a, b) == expected


def test_2():
    edges = [
        [0, 1, 1],
        [0, 2, 1],
        [1, 2, 2]
    ]
    a = 0
    b = 1
    expected = True
    assert Solution().solve(edges, a, b) == expected


def test_3():
    edges = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100]
    ]
    a = 0
    b = 2
    expected = True
    assert Solution().solve(edges, a, b) == expected
