"""
binarysearch.com :: Maximize Rook Square Values
jramaswami
"""
from math import inf

class SegmentTree2D:

    def __init__(self, matrix, merge_fn):
        self.merge_fn = merge_fn
        self.row_count = len(matrix)
        self.col_count = len(matrix[0])
        self.tree = [None for _ in range(2 * self.col_count)]

        # Make segment trees for each col in the matrix.
        for c in range(self.col_count):
            self.tree[c + self.col_count] = [0 for _ in range(2 * self.row_count)]
            for r in range(self.row_count):
                self.tree[c + self.col_count][r + self.row_count] = matrix[r][c]

            for r in range(self.row_count - 1, 0, -1):
                left, right = 2 * r, 1 + (2 * r)
                self.tree[c + self.col_count][r] = self.merge_fn(
                        self.tree[c + self.col_count][left], 
                        self.tree[c + self.col_count][right]
                )

        # Populate upper branches of tree.
        for c in range(self.col_count - 1, 0, -1):
            left, right = 2 * c, 1 + (2 * c)
            self.tree[c] = [self.merge_fn(l, r) for l, r in zip(self.tree[left], self.tree[right])]
        print(self.tree)


    def query_cols(self, st, left, right):
        print('query cols', st, left, right)
        result = -inf
        left += self.col_count
        right += self.col_count
        while left < right:
            if left & 1:
                result = self.merge_fn(result, st[left])
                left += 1
            if right & 1:
                right -= 1
                result = self.merge_fn(result, st[right])

            left >>= 1
            right >>= 1

        print('query cols', result)
        return result

    def query(self, row1, col1, row2, col2):
        print('query', row1, col1, row2, col2)
        result = -inf
        left = row1 + self.row_count
        right = row2 + self.row_count
        while left < right:
            if left & 1:
                result = self.merge_fn(result, self.query_cols(self.tree[left], col1, col2))
                left += 1
            if right & 1:
                right -= 1
                result = self.merge_fn(result, self.query_cols(self.tree[right], col1, col2))

            left >>= 1
            right >>= 1

        return result


class Solution:
    def solve(self, board):
        st = SegmentTree2D(board, max)
        print(st.query(0, 0, 4, 1))

        assert False


def test_1():
    board = [
        [1, 9, 3, 1, 9],
        [1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1]
    ]
    assert Solution().solve(board) == 17
