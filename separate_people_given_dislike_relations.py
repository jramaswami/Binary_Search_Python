"""
binarysearch.com :: Separate People Given Dislike Relations
jramaswami

Is graph bipartite?
"""


import enum


class Color(enum.Enum):
    NONE = enum.auto()
    BLACK = enum.auto()
    WHITE = enum.auto()


class Solution:

    def solve(self, node_count, edges):
        # Convert edges into adjacency lists.
        adj = [[] for _ in range(node_count)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Keep track of node color.
        color = [Color.NONE for _ in range(node_count)]

        def is_bipartite(node):
            "DFS to find bipartiteness."
            result = True
            for neighbor in adj[node]:
                if color[neighbor] == color[node]:
                    result = False
                    break
                elif color[neighbor] == Color.NONE:
                    if color[node] == Color.BLACK:
                        color[neighbor] = Color.WHITE
                    elif color[node] == Color.WHITE:
                        color[neighbor] = Color.BLACK
                    result = result and is_bipartite(neighbor)
            return result

        for node in range(node_count):
            if color[node] == Color.NONE:
                color[node] = Color.WHITE
                if not is_bipartite(node):
                    return False
        return True


def test_1():
    n = 4
    enemies = [
        [0, 1],
        [1, 2]
    ]
    assert Solution().solve(n, enemies) == True


def test_2():
    n = 3
    enemies = [
        [0, 1],
        [0, 2],
        [1, 2]
    ]
    assert Solution().solve(n, enemies) == False


def test_3():
    n = 4
    enemies = [
    ]
    assert Solution().solve(n, enemies) == True
