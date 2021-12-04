"""
binarysearch.com :: Paint Bucket
jramaswami
"""


import collections


class Solution:

    def solve(self, matrix, r, c, target):

        OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        original = matrix[r][c]
        matrix[r][c] = target
        queue = collections.deque()
        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if matrix[r0][c0] == original:
                    matrix[r0][c0] = target
                    queue.append((r0, c0))
        return matrix


def test_1():
    matrix = [
        ["r", "r", "r"],
        ["r", "g", "b"],
        ["g", "b", "b"]
    ]
    r = 0
    c = 0
    target = "g"
    expected = [
        ["g", "g", "g"],
        ["g", "g", "b"],
        ["g", "b", "b"]
    ]
    assert Solution().solve(matrix, r, c, target) == expected


def test_2():
    "TLE: endless loop"
    matrix = [["r"], ["r"]]
    r = 1
    c = 0
    target = "r"
    expected = [["r"], ["r"]]
    assert Solution().solve(matrix, r, c, target) == expected
