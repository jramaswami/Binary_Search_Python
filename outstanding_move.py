"""
binarysearch.com :: Outstanding Move
jramaswami
"""


import itertools


class Solution:

    def solve(self, nums):
        # Boundary case.
        if not nums:
            return 0

        def get_sum(left, right, arr):
            if right < left:
                return 0
            if left - 1 < 0:
                return arr[right]
            return arr[right] - arr[left-1]

        same = list(itertools.accumulate(n * (i+1) for i, n in enumerate(nums)))
        incr = list(itertools.accumulate(n * (i+2) for i, n in enumerate(nums)))
        decr = list(itertools.accumulate(n * i for i, n in enumerate(nums)))
        N = len(nums)

        soln = same[-1]
        for i, n in enumerate(nums):
            # Move n to index j.
            for j, _ in enumerate(nums):
                t = (n * (j+1))
                if j < i:
                    # [0, j) same
                    # [j, i) increases
                    # (i, N) same
                    x = get_sum(0, j-1, same)
                    y = get_sum(j, i-1, incr)
                    z = get_sum(i+1, N-1, same)
                    k = (x + y + z + t)
                    soln = max(soln, k)
                elif j > i:
                    # [0, i) same
                    # (i, j] decreases
                    # (j, N) same
                    x = get_sum(0, i-1, same)
                    y = get_sum(i+1, j, decr)
                    z = get_sum(j+1, N-1, same)
                    k = (x + y + z + t)
                    soln = max(soln, k)
        return soln


def test_1():
    nums = [5, 1, 2]
    expected = 20
    assert Solution().solve(nums) == expected
