"""
binarysearch.com :: Longest Matrix Path
jramaswami
"""


class Solution:
    def solve(self, matrix):
        def row_maxes(row):
            """Determine the maximum distance moving left or right."""
            rms = [0 for _ in row]
            curr = 0
            for i in range(0, len(row)):
                if row[i] == 0:
                    curr += 1
                else:
                    curr = 0
                rms[i] = max(rms[i], curr)

            curr = 0
            fir i in range(len(row) - 1, -1, -1):
                if row[i] == 0:
                    curr += 1
                else:
                    curr = 0
                rms[i] = max(rms[i], curr)
            return rms


        for row in matrix:
            print(row_maxes(row))



def test_1():
    matrix = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 10


def xtest_2():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def xtest_3():
    matrix = [[0]]
    assert Solution().solve(matrix) == 1


def xtest_4():
    matrix = [[1]]
    assert Solution().solve(matrix) == 0


def xtest_5():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
    assert Solution().solve(matrix) == 0


def test_6():
    """WA"""
    matrix = [ [1, 0] ]
    assert Solution().solve(matrix) == 1
