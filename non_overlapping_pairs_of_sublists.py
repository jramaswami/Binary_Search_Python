"""
binarysearch.com :: Non-Overlapping Pairs of Sublists
jramaswami
"""

from collections import deque


MOD = pow(10, 9) + 7
MOD_INV_2 = 500000004


def compute_subarray_count(list_len):
    return (list_len * (list_len + 1)) // 2

class Solution:

    # TODO: First count the number of splits in a contiguos array
    #       Then count the number of pairs that go across arrays.

    def solve(self, nums, k):
        soln = 0
        curr = 0
        subarray_count = 0
        for n in nums:
            if n >= k:
                curr += 1
            else:
                if curr > 0:
                    # How many ways can you split a subarray of length L?
                    soln = soln + (curr - 1)
                    # How many subarrays can you make from a subarray of length L?
                    M = compute_subarray_count(curr)

                    # How many ways can you choose a subarray from the current
                    # subarray along with a subarray from previous subarrays?
                    soln = soln + (subarray_count * M)
                    subarray_count += M
                    curr = 0

        if curr > 0:
            # How many ways can you split a subarray of length L?
            soln = soln + (curr - 1)
            # How many subarrays can you make from a subarray of length L?
            M = compute_subarray_count(curr)

            # How many ways can you choose a subarray from the current
            # subarray along with a subarray from previous subarrays?
            soln = soln + (subarray_count * M)
            subarray_count += M

        print(f"{subarray_count=}")
        return soln





def test_1():
    nums = [3, 4, 4, 9]
    k = 4
    expected = 5
    assert Solution().solve(nums, k) == expected
