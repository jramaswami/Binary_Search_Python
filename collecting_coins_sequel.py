"""
binarysearch.com :: Collecting Coins Sequel
jramaswami
"""


from math import inf


class Solution:
    def solve(self, matrix):


        def inbounds(r, c):
            """Return True if (r, c) is inside the matrix."""
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])


        def neighbors(r, c):
            """Return the four neighbors of (r, c)."""
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0 = r + dr
                c0 = c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)


        def dfs(r, c, acc, visited):
            """DFS to traverse matrix."""
            visited.add((r, c))
            result = acc + matrix[r][c]
            for r0, c0 in neighbors(r, c):
                if (r0, c0) not in visited and matrix[r0][c0] != 0:
                    result = max(result, dfs(r0, c0, acc + matrix[r][c], visited))
            visited.remove((r, c))
            return result


        # Get the maximum path sum from each starting point.  Take the max
        # of those max path sums.
        soln = -inf
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                soln = max(soln, dfs(r, c, 0, set()))
        return soln



def test_1():
    matrix = [
        [1, 3, 2],
        [2, 5, 0],
        [1, 0, 10]
    ]
    expected = 13
    assert Solution().solve(matrix) == 13


def test_2():
    matrix = [[72, 33, 0, 0, 92, 40, 94, 95, 48, 36], [43, 94, 63, 25, 87, 55, 53, 75, 100, 29], [66, 94, 14, 30, 7, 64, 49, 96, 41, 87], [71, 91, 49, 89, 85, 78, 12, 94, 12, 57], [68, 0, 72, 80, 79, 16, 89, 15, 20, 0], [11, 12, 50, 77, 34, 63, 81, 44, 75, 61], [12, 71, 0, 57, 84, 70, 0, 48, 21, 0], [18, 31, 84, 0, 39, 0, 0, 3, 3, 33], [34, 22, 76, 31, 79, 69, 18, 84, 90, 0], [50, 29, 7, 36, 19, 76, 98, 46, 31, 45]]
    expected = 13
    assert Solution().solve(matrix) == 13
