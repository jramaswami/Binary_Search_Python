"""
binarysearch.com :: Roomba Sequel
jramaswami
"""


import collections


class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.left = dict()
        self.right = dict()

    def add(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.size[u] = u
            self.left[u] = u
            self.right[u] = u

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.left[a] = min(self.left[a], self.left[b])
            self.right[a] = max(self.right[a], self.right[b])

    def next_west(self, a):
        a = self.find(a)
        return self.left[a]-1

    def next_east(self, a):
        a = self.find(a)
        return self.right[a]+1

    def next_north(self, a):
        return self.next_west(a)

    def next_south(self, b):
        return self.next_east(b)


class Solver:

    OFFSETS = {
        "WEST": (-1, 0), "EAST": (1, 0), "NORTH": (0, 1), "SOUTH": (0, -1)
    }

    def __init__(self):
        self.visited = set()
        self.visited_x = collections.defaultdict(lambda: UnionFind())
        self.visited_y = collections.defaultdict(lambda: UnionFind())

    def visit(self, x, y):
        self.visited.add((x, y))
        # E/W
        self.visited_y[y].add(x)
        if (x-1, y) in self.visited:
            self.visited_y[y].union(x-1, x)
        if (x+1, y) in self.visited:
            self.visited_y[y].union(x+1, x)
        # N/S
        self.visited_x[x].add(y)
        if (x, y-1) in self.visited:
            self.visited_x[x].union(y-1, y)
        if (x, y+1) in self.visited:
            self.visited_x[x].union(y+1, y)

    def simulate(self, moves):
        x = y = 0
        self.visit(0, 0)
        for move in moves:
            dx, dy = Solver.OFFSETS[move]
            x, y = x + dx, y + dy
            if (x, y) in self.visited:
                # Continue to move to the next unvisited position.
                if move == "WEST":
                    x = self.visited_y[y].next_west(x)
                elif move == "EAST":
                    x = self.visited_y[y].next_east(x)
                elif move == "NORTH":
                    y = self.visited_x[x].next_north(y)
                elif move == "SOUTH":
                    y = self.visited_x[x].next_south(y)
            else:
                self.visit(x, y)
            # print(f"{x=} {y=}")

        return x, y



class Solution:

    def solve(self, moves, xn, yn):
        solver = Solver()
        x, y = solver.simulate(moves)
        return x == xn and y == yn


def test_1():
    moves = ["NORTH", "EAST", "SOUTH", "WEST"]
    x = -1
    y = 0
    expected = True
    assert Solution().solve(moves, x, y) == expected


def test_2():
    moves = ["NORTH", "SOUTH"]
    x = 0
    y = 0
    expected = False
    assert Solution().solve(moves, x, y) == expected


def test_3():
    "WA"
    moves = ["WEST","SOUTH","NORTH","SOUTH","WEST","WEST","NORTH","WEST","SOUTH","EAST","SOUTH","EAST","NORTH","WEST","EAST","WEST","SOUTH","WEST","WEST","WEST","WEST","WEST","EAST","SOUTH","EAST","SOUTH","SOUTH","NORTH","SOUTH","EAST","SOUTH","WEST","SOUTH","EAST","WEST","SOUTH","NORTH","SOUTH","WEST","WEST","WEST","SOUTH","NORTH","SOUTH","NORTH","EAST","NORTH","SOUTH","WEST","NORTH","SOUTH","NORTH","SOUTH","NORTH","WEST","EAST","EAST","EAST","EAST","WEST","NORTH","EAST","NORTH","SOUTH","SOUTH","WEST","EAST","SOUTH","SOUTH","EAST","WEST","EAST","EAST","EAST","NORTH","SOUTH","WEST","SOUTH","EAST","EAST","SOUTH","NORTH","EAST","SOUTH","WEST","EAST","EAST","NORTH","WEST","WEST","EAST","WEST","WEST","NORTH","EAST","EAST","NORTH","NORTH","WEST","NORTH","SOUTH","WEST","EAST","WEST","SOUTH","EAST","WEST","EAST","WEST","SOUTH","EAST","WEST","EAST","SOUTH","EAST","SOUTH","EAST","SOUTH","EAST","WEST","EAST","EAST","EAST","EAST","EAST","WEST","SOUTH","WEST","NORTH","WEST","WEST","EAST","SOUTH","SOUTH","WEST","SOUTH","SOUTH","NORTH","NORTH","WEST","EAST","SOUTH","NORTH","EAST","EAST","WEST","WEST","SOUTH","WEST","SOUTH","WEST","NORTH","EAST","NORTH","WEST","NORTH","NORTH","EAST","SOUTH","NORTH","EAST","SOUTH","WEST","SOUTH","EAST","WEST","SOUTH","NORTH","EAST","WEST","NORTH","SOUTH","SOUTH","WEST","WEST","WEST","WEST","NORTH","EAST","NORTH","NORTH","NORTH","WEST","EAST","SOUTH","WEST","NORTH","WEST","WEST","NORTH","EAST","SOUTH","NORTH","EAST","WEST","SOUTH","NORTH","EAST","SOUTH","WEST","EAST","SOUTH","SOUTH","EAST","NORTH","EAST","SOUTH","WEST","WEST","WEST","WEST","WEST","SOUTH","WEST","NORTH","WEST","SOUTH","WEST","NORTH","WEST","EAST","SOUTH","WEST","WEST","WEST","SOUTH","WEST","EAST","WEST","EAST","WEST","NORTH","SOUTH","NORTH","SOUTH","WEST","SOUTH","EAST","WEST","NORTH","WEST","EAST","EAST","SOUTH","EAST","NORTH","NORTH","WEST","EAST","WEST","SOUTH","WEST","NORTH","SOUTH","WEST","EAST","WEST","SOUTH","SOUTH","WEST","EAST","NORTH","WEST","WEST","EAST"]
    x = -3
    y = 24
    expected = True
    assert Solution().solve(moves, x, y) == expected
