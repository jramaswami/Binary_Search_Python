"""
binarysearch.com :: Common Ancestor in a Graph
https://binarysearch.com/room/Weekly-Contest-38-CNs3hGBp9j?questionsetIndex=1
"""
from collections import defaultdict, deque


class Solution:
    def solve(self, edges, a, b):
        rev_adj = defaultdict(list)
        for u, v in edges:
            # [parent, child]
            rev_adj[v].append(u)


        visited_a = set()
        visited_a.add(a)
        queue = deque([a])
        while queue:
            u = queue.popleft()
            for v in rev_adj[u]:
                if v not in visited_a:
                    queue.append(v)
                    visited_a.add(v)

        if b in visited_a:
            return True
        visited_b = set()
        visited_b.add(b)
        queue = deque([b])
        while queue:
            u = queue.popleft()
            for v in rev_adj[u]:
                if v in visited_a:
                    return True
                if v not in visited_b:
                    queue.append(v)
                    visited_b.add(v)

        return False


def test_1():
    edges = [
        [0, 4],
        [4, 3],
        [1, 2],
        [0, 1]
    ]
    a = 2
    b = 3
    assert Solution().solve(edges, a, b) == True

def test_2():
    edges = [
        [0, 1],
        [1, 2],
        [1, 3],
        [4, 5]
    ]
    a = 2
    b = 4
    assert Solution().solve(edges, a, b) == False


def test_3():
    edges = [
        [0, 0]
    ]
    a = 0
    b = 0
    assert Solution().solve(edges, a, b) == True

def test_4():
    edges = [
        [1, 0],
        [2, 0]
    ]
    a = 0
    b = 1
    assert Solution().solve(edges, a, b) == True
