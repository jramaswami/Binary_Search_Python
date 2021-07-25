"""
binarysearch.com :: Contiguous Intervals
jramaswami
"""


class Solution:
    def solve(self, nums):
        # Corner case: empty array.
        if not nums:
            return []

        # Sort the numbers in order to both construct the intervals and to
        # return them in sorted order.
        nums0 = sorted(nums)
        curr_start = curr_end = nums0[0]
        soln = []
        for n in nums0[1:]:
            if n == curr_end + 1:
                # Part of the same interval.  Extend interval to 1 to n.
                curr_end = n
            else:
                # Not part of the same interval.  Put previous interval
                # in the solution.  Then start a new interval.
                soln.append([curr_start, curr_end])
                curr_start = curr_end = n
        # Put the last interval in the solution.
        soln.append([curr_start, curr_end])
        return soln


def test_1():
    nums = [1, 3, 2, 7, 6]
    expected = [ [1, 3], [6, 7] ]
    assert Solution().solve(nums) == expected


def test_2():
    """Corner case of empty nums."""
    nums = []
    expected = []
    assert Solution().solve(nums) == expected

