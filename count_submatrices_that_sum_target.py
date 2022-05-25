"""
binarysearch.com :: Count Submatrices That Sum Target
jramaswami
"""


import collections
import itertools


class Solution:

    def solve(self, matrix, target):
        prefix = [list(itertools.accumulate(row)) for row in matrix]

        def get_sum(row, left, right):
            "Return the sum of matrix[row][left:right+1]."
            if left - 1 < 0:
                return prefix[row][right]
            return prefix[row][right] - prefix[row][left-1]

        height = len(matrix)
        width = len(matrix[0])
        soln = 0
        for left in range(width):
            for right in range(left, width):
                curr_sum = 0
                prev_sums = collections.defaultdict(int)
                for row in range(height):
                    curr_sum += get_sum(row, left, right)
                    if curr_sum == target:
                        soln += 1
                    # curr_sum - prev_sum = target
                    # curr_sum - target = prev_sum
                    prev_sum = curr_sum - target
                    soln += prev_sums[prev_sum]
                    prev_sums[curr_sum] += 1
        return soln


def test_1():
    matrix = [ [0, -1], [0, 0] ]
    target = 0
    expected = 5
    assert Solution().solve(matrix, target) == expected
