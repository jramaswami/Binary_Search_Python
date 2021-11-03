"""
binarysearch.com :: Course Scheduling
jramaswami
"""


import enum


class Color(enum.Enum):
    WHITE = enum.auto()
    GRAY = enum.auto()
    BLACK = enum.auto()


class Solver:

    def __init__(self, adj):
        self.adj = adj
        self.color = [Color.WHITE for _ in adj]
        self.cycle_detected = False

    def dfs(self):
        for node, _ in enumerate(self.adj):
            if self.color[node] == Color.WHITE:
                self.dfs_visit(node)

    def dfs_visit(self, node):
        self.color[node] = Color.GRAY
        for neighbor in self.adj[node]:
            if self.color[neighbor] == Color.WHITE:
                self.dfs_visit(neighbor)
            elif self.color[neighbor] == Color.GRAY:
                # Cycle detected
                self.cycle_detected = True
        self.color[node] = Color.BLACK


class Solution:

    def solve(self, courses):
        # A topological sort exists if the graph does *not* contain a cycle.
        solver = Solver(courses)
        solver.dfs()
        return not solver.cycle_detected