"""
binarysearch.com :: Logically Consistent Book
jramaswami
"""


import collections


class Solution:

    def solve(self, lists):
        graph = collections.defaultdict(list)
        nodes = set()
        # Turn edges into half-open intervals.
        for i, (u, v, w) in enumerate(lists):
            u, v = min(u, v), max(u, v) + 1
            graph[u].append((v, w))
            nodes.add(u)

        # DFS Forward only.
        def dfs(u, parity):
            for v, w in graph[u]:
                if v in parity:
                    # Parity from root node must be the same.
                    if (parity[u] + w) % 2 != parity[v]:
                        return False
                else:
                    parity[v] = (parity[u] + w) % 2
                    if v in nodes:
                        if not dfs(v, parity):
                            return False
            return True

        for u in sorted(nodes):
            parity = dict()
            parity[u] = 0
            if not dfs(u, parity):
                return False
        return True


def test_1():
    lists = [ [1, 5, 1], [6, 10, 0], [1, 10, 0] ]
    expected = False
    assert Solution().solve(lists) == expected


def test_2():
    lists = [ [0, 2, 0], [2, 4, 0], [0, 4, 0] ]
    expected = True
    assert Solution().solve(lists) == expected


def test_3():
    lists = [ [0, 2, 1], [3, 4, 1], [0, 4, 0] ]
    expected = True
    assert Solution().solve(lists) == expected


def test_4():
    "WA"
    lists = [[1, 1, 1]]
    expected = True
    assert Solution().solve(lists) == expected


def test_5():
    "WA"
    lists = [[0, 0, 1], [0, 1, 0], [1, 2, 0], [2, 2, 0]]
    expected = False
    assert Solution().solve(lists) == expected


def test_6():
    "WA"
    lists = [[0, 1, 0], [0, 2, 0], [1, 1, 1], [1, 2, 0]]
    expected = False
    assert Solution().solve(lists) == expected
