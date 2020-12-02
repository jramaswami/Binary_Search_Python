"""
binarysearch.com :: Painting Houses
https://binarysearch.com/problems/Painting-Houses
"""
from math import inf
from collections import namedtuple


Min = namedtuple('Min', ['val', 'index'])


class Solution:
    def solve(self, matrix):
        
        # Find the minimum two values for row 0
        min0, min1 = Min(inf, inf), Min(inf, inf)
        for col, val in enumerate(matrix[0]):
            if val < min0.val:
                min0, min1 = Min(val, col), min0
            elif val < min1.val:
                min0, min1 = min0, Min(val, col)

        # For each of the remaining rows ...
        for row in range(1, len(matrix)):
            # These will be the two lowest costs for this row.
            new_min0, new_min1 = Min(inf, inf), Min(inf, inf)
            # For each column see what the minimum cost is to reach that col
            # from the row above.
            for col, val in enumerate(matrix[row]):
                val0 = val + min0.val
                # You cannot use the value from the column above, so if the
                # lowest cost for the row above uses this column, then you
                # must pick the second lowest cost.
                if col == min0.index:
                    val0 = val + min1.val

                # Update the minimums for the whole row.
                if val0 < new_min0.val:
                    new_min0, new_min1 = Min(val0, col), new_min0
                elif val0 < new_min1.val:
                    new_min0, new_min1 = new_min0, Min(val0, col)

            # Now swap these minimums to be the minimums for the next row.
            min0, min1 = new_min0, new_min1

        # Return the lowest cost.
        return min0.val



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
