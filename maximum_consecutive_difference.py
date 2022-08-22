"""
binarysearch.com :: Maximum Consecutive Difference
jramaswami
"""


from typing import *
from math import inf, ceil


def solve_using_buckets(nums):
    """Solution using buckets, i.e. Pigeon Hole Principle"""
    mn = min(nums)
    mx = max(nums)
    rng = mx - mn
    if rng == 0:
        return 0
    bucket_count = len(nums) + 1
    bucket_size = int(ceil(rng / len(nums)))
    bucket_min = [inf for _ in range(bucket_count)]
    bucket_max = [-inf for _ in range(bucket_count)]
    for n in nums:
        bucket_index = (n - mn) // bucket_size
        bucket_min[bucket_index] = min(bucket_min[bucket_index], n)
        bucket_max[bucket_index] = max(bucket_max[bucket_index], n)

    prev_min = bucket_min[0]
    prev_max = bucket_max[0]
    soln = prev_max - prev_min
    for i in range(1, bucket_count):
        curr_min, curr_max = bucket_min[i], bucket_max[i]
        if curr_min != inf:
            soln = max(soln, curr_max - curr_min)
            soln = max(soln, curr_min - prev_max)
            prev_min, prev_max = curr_min, curr_max

    return soln


class Solution:
    def solve(self, nums):
        # Base case
        if len(nums) < 2:
            return 0

        return solve_using_buckets(nums)