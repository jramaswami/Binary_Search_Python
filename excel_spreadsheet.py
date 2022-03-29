"""
binarysearch.com :: Excel Spreadsheet
jramaswami
"""


class Solution:
    def solve(self, matrix):
        # Don't mutate original matrix.
        matrix0 = [[None for _ in row] for row in matrix]

        def label_to_indexes(cell):
            c = ord(cell[0]) - ord('A')
            r = int(cell[1:]) - 1
            return r, c

        def xeval(x):
            # Is this a number?
            try:
                v = int(x)
                return v
            except:
                pass

            # Is this a formula?
            if x.startswith('='):
                if '+' in x:
                    a, b = x[1:].split('+')
                    u, v = xeval(a), xeval(b)
                    return u + v
                else:
                    a, b = x[1:].split('-')
                    u, v = xeval(a), xeval(b)
                    return u - v

            # This must be a cell reference.
            r, c = label_to_indexes(x)
            if matrix0[r][c] is None:
                matrix0[r][c] = xeval(matrix[r][c])
            return matrix0[r][c]

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                matrix0[r][c] = xeval(matrix[r][c])

        return [[str(x) for x in row] for row in matrix0]



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
