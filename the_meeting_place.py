"""
binarysearch.com :: The Meeting Place
jramaswami

You are given a two dimensional integer matrix consisting of:

0 which represents an empty cell.
1 which represents a wall.
2 which represents a person.

A person can walk up, down, left and right. Find a non-wall cell such that it
minimizes the total travel distance each person has to walk to and return the
distance.

Note: two people can walk through a same non-wall cell and you can assume there
is some path between any two people.
"""

from collections import deque
from math import inf


class Solution:
    def solve(self, matrix):
        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0])

        def neighborhood(r, c):
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0 = r + dr
                c0 = c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        person_starts = [(r, c) for r, row in enumerate(matrix)
                                for c, v in enumerate(row) if v == 2]
        distance = [[inf for v in row] for row in matrix]
        for row, col in person_starts:
            visited = [[False for _ in row] for row in matrix]
            visited[row][col] = True
            if distance[row][col] == inf:
                distance[row][col] = 0
            queue = deque([(row, col, 0)])
            while queue:
                r, c, d = queue.popleft()
                for r0, c0 in neighborhood(r, c):
                    if matrix[r0][c0] != 1 and not visited[r0][c0]:
                        visited[r0][c0] = True
                        if distance[r0][c0] == inf:
                            distance[r0][c0] = 0
                        distance[r0][c0] += (1 + d)
                        queue.append((r0, c0, d + 1))

        for row in distance:
            print(row)

        return min(min(row) for row in distance)



def test_1():
    matrix = [
        [2, 0, 1, 0],
        [1, 0, 1, 2],
        [0, 0, 2, 2]
    ]
    assert Solution().solve(matrix) == 7


def test_2():
    """WA"""
    matrix = [
        [0, 1, 1, 2, 2],
        [0, 0, 0, 0, 1],
        [2, 0, 1, 0, 1],
        [2, 1, 0, 1, 1]
    ]
    assert Solution().solve(matrix) == 12

def test_3():
    """WA"""
    matrix = [
        [0, 0, 1, 0, 0, 1, 2, 1],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1]
    ]
    assert Solution().solve(matrix) == 0
