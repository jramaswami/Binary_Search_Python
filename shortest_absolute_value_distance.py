"""
binarysearch.com :: Shortest Absolute Value Distance
jramaswami
"""


import math
import collections


class Solution:
    def solve(self, matrix):
        dist = [[math.inf for _ in row] for row in matrix]
        dist[0][0] = 0

        queue = collections.deque([(0, 0, 0)])
        while queue:
            d, r, c = queue.popleft()
            if dist[r][c] != d:
                continue
            # Go down
            if r+1 < len(matrix):
                d0 = d + abs(matrix[r][c] - matrix[r+1][c])
                if d0 < dist[r+1][c]:
                    dist[r+1][c] = d0
                    queue.append((d0, r+1, c))
            # Go up
            if r-1 >= 0:
                d0 = d + abs(matrix[r][c] - matrix[r-1][c])
                if d0 < dist[r-1][c]:
                    dist[r-1][c] = d0
                    queue.append((d0, r-1, c))
            # Go left
            if c-1 >= 0:
                d0 = d + abs(matrix[r][c] - matrix[r][c-1])
                if d0 < dist[r][c-1]:
                    dist[r][c-1] = d0
                    queue.append((d0, r, c-1))
            # Go right
            if c+1 < len(matrix[r]):
                d0 = d + abs(matrix[r][c] - matrix[r][c+1])
                if d0 < dist[r][c+1]:
                    dist[r][c+1] = d0
                    queue.append((d0, r, c+1))

        return dist[-1][-1]





def test_1():
    matrix = [
        [1, 100, 1],
        [2, 5, 3],
        [1, 2, 3]
    ]
    assert Solution().solve(matrix) == 4


def test_2():
    "WA"
    matrix = [
        [2, 3, -2],
        [-3, 3, -1],
        [-2, 0, 0],
        [3, 0, 3],
        [-2, 2, 0]
    ]
    assert Solution().solve(matrix) == 8
