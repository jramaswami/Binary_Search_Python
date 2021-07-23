"""
binarysearch.com :: Matrix Search
jramaswami
"""


from math import inf


class Solution:
    def solve(self, matrix, k):

        def count_lte(n, matrix):
            """Count the number of items in the matrix <= n."""
            result = 0
            c = len(matrix[0]) - 1
            # For each row.
            for r, row in enumerate(matrix):
                # Move left to the first item <= n
                while c >= 0 and row[c] > n:
                    c -= 1
                # Add to the result the number of items in this row <= n
                result += (c + 1)
            return result

        # Binary search for the element with k items less than it.
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            p = count_lte(mid, matrix)
            # There are p + 1 items less than k. (Include itself.)
            if p <= k:
                lo = lo + 1
            else:
                soln = min(soln, mid)
                hi = mid - 1
        return soln


def test_1():
    matrix = [
        [1, 3, 30],
        [2, 3, 31],
        [5, 5, 32]
    ]
    k = 4
    expected = 5
    for row in matrix:
        print(row)
    assert Solution().solve(matrix, k) == expected


def test_2():
    matrix = [
        [1, 2, 3]
    ]
    k = 0
    expected = 1
    assert Solution().solve(matrix, k) == expected

def test_3():
    matrix = [
        [1],
        [2],
        [3]
    ]
    k = 2
    expected = 3
    assert Solution().solve(matrix, k) == expected


def test_4():
    matrix = [
        [1, 3, 30, 33],
        [2, 3, 31, 40],
        [5, 5, 32, 50]
    ]
    k = 4
    expected = 5
    for row in matrix:
        print(row)
    assert Solution().solve(matrix, k) == expected
