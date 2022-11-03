"""
binarysearch.com :: Weekly Contest 35 :: Recover Original List From Subsequences
"""
from math import inf
from collections import defaultdict

def dfs(node, path, adj, N):
    if len(path) == N:
        return True

    for neighbor in adj[node]:
        path.append(neighbor)
        if dfs(neighbor, path, adj, N):
            return True
        path.pop()

    return[]
        

class Solution:
    def solve(self, lists):
        max_element = max(max(lst) for lst in lists)
        adj = [[] for _ in range(max_element+1)]
        indegree = [0 for _ in range(max_element+1)]
        nodes = set()
        for lst in lists:
            for u, v in zip(lst[:-1], lst[1:]):
                nodes.add(u)
                nodes.add(v)
                adj[u].append(v)
                indegree[v]+=1

        root = 0
        for u in nodes:
            if indegree[u] == 0:
                root = u

        path = [root]
        if dfs(root, path, adj, len(nodes)):
            return path
        else:
            return []




def test_1():
    lists = [
        [1, 3],
        [2, 3],
        [1, 2]
    ]
    solver = Solution()
    assert solver.solve(lists) == [1, 2, 3]

def test_2():
    lists = [
        [1, 2, 4],
        [2, 3, 4]
    ]
    solver = Solution()
    assert solver.solve(lists) == [1, 2, 3, 4]

def test_3():
    lists = [
        [1, 2, 3]
    ]
    solver = Solution()
    assert solver.solve(lists) == [1, 2, 3]

def test_4():
    lists = [
        [5, 4],
        [4, 3],
        [3, 2, 1, 0]
    ]
    solver = Solution()
    assert solver.solve(lists) == [5, 4, 3, 2, 1, 0]

def test_5():
    lists = [
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 7]
    ]
    solver = Solution()
    assert solver.solve(lists) == [1, 2, 3, 4, 7]
