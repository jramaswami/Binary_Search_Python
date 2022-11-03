"""
binarysearch.com :: Weekly Contest 39 :: Minimize Amplitude After Deleting K-Length Sublist
"""
from math import inf

class Solution:
    def solve(self, nums, k):
        max_prefix = [-inf for _ in nums]
        max_suffix = [-inf for _ in nums]
        min_prefix = [inf for _ in nums]
        min_suffix = [inf for _ in nums]
        max_v = -inf
        min_v = inf
        for i, v in enumerate(nums):
            max_v = max(max_v, v)
            min_v = min(min_v, v)
            max_prefix[i] = max_v
            min_prefix[i] = min_v
        max_v = -inf
        min_v = inf
        for i in range(len(nums) - 1, -1, -1):
            v = nums[i]
            max_v = max(max_v, v)
            min_v = min(min_v, v)
            max_suffix[i] = max_v
            min_suffix[i] = min_v

        soln = inf
        for i in range(len(nums) - k+1):
            # I am removing [i, i + k).
            if i == 0:
                soln = min(soln, max_suffix[i+k] - min_suffix[i+k])
            elif i == len(nums) - k:
                soln = min(soln, max_prefix[i-1] - min_prefix[i-1])
            else:
                max_v = max(max_prefix[i-1], max_suffix[i+k])
                min_v = min(min_prefix[i-1], min_suffix[i+k])
                soln = min(soln, max_v - min_v)

        return soln


def test_1():
    nums = [1, 2, 9, 8, 7, 3]
    k = 3
    assert Solution().solve(nums, k) == 2


