"""
Binary Search :: Weekly Contest 31 :: Window Queries
"""
from collections import defaultdict

class Solution:
    def solve(self, nums, queries, w):
        positions = defaultdict(list)
        for i, n in enumerate(nums):
            positions[n].append(i)

        soln = [0 for _ in queries]
    
        for qi, q in enumerate(queries):
            for pi, p in enumerate(positions[q]):
                # Compute the minimum starting point for a window that includes
                # position p.
                # It must be greater than 0.
                min_window_start = max(p - w + 1, 0)
                # It cannot include the previous position with the same number.
                if pi > 0:
                    min_window_start = max(positions[q][pi-1]+1, min_window_start)

                # Compute the maximum window start.  The window cannot extend
                # past the end of the array.
                max_window_start = min(p, len(nums) - w)

                # Given the minimum starting window, this position will be in
                # <max windown start> - <min starting window> as the first
                # number of its kind.  Count these.
                window_count = max(max_window_start - min_window_start + 1, 0)
                soln[qi] += window_count
        return soln


def test_1():
    solver = Solution()
    nums = [2, 1, 2, 3, 4]
    queries = [2, 1]
    w = 3
    assert solver.solve(nums, queries, w) == [3, 2]


def test_2():
    solver = Solution()
    nums = [2, 2, 2]
    queries = [2]
    w = 2
    assert solver.solve(nums, queries, w) == [2]


def test_3():
    solver = Solution()
    nums = [1, 0]
    queries = [0]
    w = 2
    assert solver.solve(nums, queries, w) == [1]


def test_4():
    solver = Solution()
    nums = [0, 0, 0]
    queries = [0]
    w = 3
    assert solver.solve(nums, queries, w) == [1]
