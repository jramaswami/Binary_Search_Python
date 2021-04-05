"""
binarysearch.com :: Zero Matrix
jramaswami
"""
class Solution:
    def solve(self, matrix):
        zero_rows = set()
        zero_cols = set()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        soln = []
        for r, row in enumerate(matrix):
            if r in zero_rows:
                soln.append([0 for _ in row])
            else:
                new_row = []
                for c, val in enumerate(row):
                    new_row.append(0 if c in zero_cols else val)
                soln.append(new_row)

        return soln


def test_1():
    matrix = [[5, 0, 0, 5, 8], [9, 8, 10, 3, 9], [0, 7, 2, 3, 1], [8, 0, 6, 7, 2], [4, 1, 8, 5, 10]]
    expected = [[0, 0, 0, 0, 0], [0, 0, 0, 3, 9], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 5, 10]]
    assert Solution().solve(matrix) == expected
