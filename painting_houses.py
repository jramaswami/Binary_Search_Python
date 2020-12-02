"""
binarysearch.com :: Painting Houses
https://binarysearch.com/problems/Painting-Houses
"""
from math import inf
import heapq


class Solution:
    def solve(self, matrix):
        # Use dijkstra's algorithm to solve
        # Set up queue
        queue = []
        for col, val in enumerate(matrix[0]):
            heapq.heappush(queue, (val, (0, col)))

        # Set up distances
        dist = [[inf for _ in row] for row in matrix]
        dist[0] = list(matrix[0])
        soln = inf

        # Run through queue
        while queue:
            val, (row, col) = heapq.heappop(queue)
            for col0 in range(len(matrix[0])):
                if col == col0:
                    continue
                
                if row + 1 >= len(matrix):
                    soln = min(soln, dist[row][col])
                else:
                    d = dist[row][col] + matrix[row+1][col0]
                    if d < dist[row+1][col0]:
                        dist[row+1][col0] = d
                        heapq.heappush(queue, (d, (row+1, col0)))

        for row in dist:
            print(row)
        return soln


def test_1():
    matrix = [
        [5, 3, 4],
        [2, 1, 6],
        [2, 3, 4],
        [4, 3, 3]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 10

def test_2():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 5

def test_3():
    matrix = [
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 5

def test_4():
    matrix = [
        [1, 2, 3],
        [4, 1, 8],
        [2, 3, 4],
        [3, 3, 1],
        [4, 2, 3]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 7
