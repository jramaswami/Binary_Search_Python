"""
binarysearch.com :: Excel Spreadsheet
jramaswami
"""


class Solution:
    def solve(self, matrix):
        # Don't mutate original matrix.
        matrix0 = [list(row) for row in matrix]

        def label_to_indexes(cell):
            c = ord(cell[0]) - ord('A')
            r = int(cell[1]) - 1
            return r, c

        def indexes_to_label(r, c):
            return chr(ord('A') + c) + str(r + 1)

        def eval_cell(cell):
            try:
                v = int(cell)
                return v
            except:
                pass

            r, c = label_to_indexes(cell)
            if matrix0[r][c][0] == '=':
                # Formula
                if '+' in matrix0[r][c]:
                    left_ref, right_ref = matrix0[r][c][1:].split('+')
                    left_val, right_val = eval_cell(left_ref), eval_cell(right_ref)
                    matrix0[r][c] = str(left_val + right_val)
                else:
                    left_ref, right_ref = matrix0[r][c][1:].split('-')
                    left_val, right_val = eval_cell(left_ref), eval_cell(right_ref)
                    matrix0[r][c] = str(left_val - right_val)
            else:
                # Cell ref
                v = eval_cell(matrix0[r][c])
                matrix0[r][c] = str(v)
            return int(matrix0[r][c])

        for r, row in enumerate(matrix0):
            for c, _ in enumerate(row):
                eval_cell(indexes_to_label(r, c))

        return matrix0



def test_1():
    matrix = [ ["B1", "2", "0"], ["3", "5", "=A1+A2"] ]
    expected = [ ["2", "2", "0"], ["3", "5", "5"] ]
    result = Solution().solve(matrix)
    assert result == expected


def test_2():
    matrix = [ ["B1", "-2", "=6+0"], ["1", "=A3+A3", "=A2-A1"], ["=-2+B1", "=C1+10", "C2"] ]
    expected = [ ["-2", "-2", "6"], ["1", "-8", "3"], ["-4", "16", "3"] ]
    result = Solution().solve(matrix)
    assert result == expected
