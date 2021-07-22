"""
binarysearch.com :: Sublist with Largest Min-Length Product
jramaswami
"""


from math import inf
from collections import defaultdict


def binsearch_left(A, lo, hi, x):
    """
    Return the index of the leftmost element in A[lo:hi+1] >= x.
    A[lo:hi+1] will be sorted in descending order.
    [5 4 3 2 1]
    """
    soln = hi + 1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if A[mid] >= x:
            # This item is lower than or equal to x.  Since we are looking for
            # the leftmost element less than x, see if there are any elements
            # greater than  or equal to x to the left of here.
            soln = min(soln, mid)
            hi = mid - 1
        else:
            # This item is more than x.  Since the elements are in descending
            # order, we must look to the right of the curent position.
            lo = mid + 1
    return soln


def binsearch_right(A, lo, hi, x):
    """
    Return the index of the rightmost element in A[lo:hi+1] >= x.
    A[lo:hi+1] will be sorted in asending order.
    [1 2 3 4]
    """
    soln = lo - 1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2)
        if A[mid] >= x:
            # This item is greater than or equal to x.  Since we are looking
            # for the rightmost element less than x, see if there are any
            # elements greater than or equal to than x to the right of here.
            soln = max(soln, mid)
            lo = mid + 1
        else:
            # This item is more then x.  Since the elements are in descending
            # order, look to the left.
            hi = mid - 1
    return soln


class Solution:
    def solve(self, nums, pos):
        min_to_pos = [inf for _ in nums]

        # Right to left, from pos to 0.
        curr_min = inf
        for i in range(pos, -1, -1):
            curr_min = min(curr_min, nums[i])
            min_to_pos[i] = curr_min

        # Left to right, from pos to len(nums) - 1
        curr_min = inf
        for i in range(pos, len(nums)):
            curr_min = min(curr_min, nums[i])
            min_to_pos[i] = curr_min

        soln = nums[pos]
        for i, k in enumerate(min_to_pos):
            if i < pos:
                # Where is the rightmost element in A[pos+1:] where
                # min_to_pos[i] is still the minimum.
                j = binsearch_right(min_to_pos, pos, len(nums)-1, k)
                if j >= pos:
                    soln = max(soln, (j - i + 1) * k)
            elif i > pos:
                # Where is the rightmost element in A[0:pos] where min_to_pos[i]
                # is still the minimum.
                j = binsearch_left(min_to_pos, 0, pos, k)
                if j <= pos:
                    soln = max(soln, (i - j + 1) * k)
        return soln



def test_1():
    nums = [-1, 1, 4, 3]
    pos = 3
    assert Solution().solve(nums, pos) == 6


def test_2():
    nums = [4, 2, 3, 10, 10, 5, 6, 10, 2, 9]
    pos = 6
    assert Solution().solve(nums, pos) == 25
