"""
binarysearch.com :: Tree Detection
jramaswami
"""


import collections


class Solution:
    def solve(self, left, right):

        parent = [-1 for _ in left]
        children = [[] for _ in left]
        for u, v in enumerate(left):
            if v >= 0:
                # Node can only have one parent.
                if parent[v] >= 0:
                    return False
                parent[v] = u
                children[u].append(v)

        for u, v in enumerate(right):
            if v >= 0:
                # Node can only have one parent.
                if parent[v] >= 0:
                    return False
                parent[v] = u
                children[u].append(v)

        # For a binary tree, exactly one node should have no parent.
        possible_roots = [i for i, p in enumerate(parent) if p == -1]
        if len(possible_roots) != 1:
            return False
        root = possible_roots[0]

        # Now make sure the all nodes are connected and no cycles exist.
        queue = collections.deque()
        queue.append(root)
        visited = [False for _ in left]
        visited[root] = True
        while queue:
            node = queue.popleft()
            for child in children[node]:
                # If the child has been visited already then the graph
                # is a cyclic and not a tree.
                if visited[child]:
                    return False
                queue.append(child)
                visited[child] = True
        return all(visited)



def test_1():
    left = [1, -1, 3, -1]
    right = [2, -1, -1, -1]
    expected = True
    assert Solution().solve(left, right) == expected


def test_2():
    left = [0]
    right = [0]
    expected = False
    assert Solution().solve(left, right) == expected


def test_3():
    "WA"
    left = [-1, 1]
    right = [1, 0]
    expected = False
    assert Solution().solve(left, right) == expected
