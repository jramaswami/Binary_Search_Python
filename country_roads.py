"""
binarysearch.com :: Country Roads
jramaswami
"""


class Solution:

    def solve(self, source, destination, population):
        # Turn edges (source, destination) into adj.
        adj = [[] for _ in population]
        for u, v in zip(source, destination):
            adj[u].append(v)
            adj[v].append(u)

        BLACK, WHITE = -1, 1
        color = [0 for _ in population]

        def opposite_color(color):
            if color == BLACK:
                return WHITE
            return BLACK

        def dfs(node, parent):
            if parent >= 0 and color[node] == color[parent]:
                raise Exception(f"{node} <-> {parent} not a bipartite graph.")
            color[node] = opposite_color(color[parent])
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                dfs(neighbor, node)

        dfs(0, -1)
        white_sum = sum(p for p, c in zip(population, color) if c == WHITE)
        black_sum = sum(p for p, c in zip(population, color) if c == BLACK)
        return max(white_sum, black_sum)



def test_1():
    source = [0, 0, 2, 2]
    dest = [1, 2, 4, 3]
    population = [5, 7, 3, 2, 4]
    expected = 11
    assert Solution().solve(source, dest, population) == expected
