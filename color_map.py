"""
binarysearch.com :: Color Map
jramaswami
"""


import collections


class Solution:
    def solve(self, matrix):
        # Boundary case.
        if not matrix or matrix == [[]]:
            return 0

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        freqs = collections.defaultdict(int)
        visited = [[False for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            for c, color in enumerate(row):
                if not visited[r][c]:
                    freqs[color] += 1
                    visited[r][c] = True

                    queue = collections.deque([(r, c)])
                    while queue:
                        r0, c0 = queue.popleft()
                        for r1, c1 in neighbors(r0, c0):
                            if matrix[r0][c0] == matrix[r1][c1] and not visited[r1][c1]:
                                queue.append((r1, c1))
                                visited[r1][c1] = True

        max_freq = max(freqs.values())
        sum_freq = sum(freqs.values())
        return sum_freq - max_freq



def test_1():
    matrix = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [1, 3, 1, 2]
    ]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [[]]
    expected = 0
    assert Solution().solve(matrix) == expected


def test_3():
    matrix = []
    expected = 0
    assert Solution().solve(matrix) == expected


def test_4():
    "TLE"
    matrix = [[4 for _ in range(250)] for _ in range(250)]
    expected = 0
    assert Solution().solve(matrix) == expected
