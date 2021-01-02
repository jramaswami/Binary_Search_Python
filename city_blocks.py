"""
binarysearch.com :: City Blocks
jramaswami
"""
def manhattan_distance(p1, p2):
    """Manhattan distance between two positions."""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


class Solution:
    def solve(self, matrix, blocks):
        positions = dict()
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                positions[v] = (r, c)

        prev = (0, 0)
        distance = 0
        for b in blocks:
            distance += manhattan_distance(prev, positions[b])
            prev = positions[b]
        return distance


def test_1():
    matrix = [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"]
    ]
    blocks = ["h", "b", "c"]
    assert Solution().solve(matrix, blocks) == 6
