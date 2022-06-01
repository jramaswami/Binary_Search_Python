"""
binarysearch.com :: Max Sum of Two Non-Overlapping Lists
jramaswami
"""


import math


class Solution:

    def solve(self, nums, a, b):
        sums = [-math.inf for _ in nums]
        curr_sum = sum(nums[:a])
        sums[a-1] = curr_sum
        for i, n in enumerate(nums[a:], start=a):
            curr_sum -= nums[i-a]
            curr_sum += n
            sums[i] = curr_sum

        suffix_maxs = [-math.inf for _ in nums]
        curr_max = -math.inf
        for i in range(len(nums)-1, -1, -1):
            curr_max = max(curr_max, sums[i])
            suffix_maxs[i] = curr_max

        prefix_maxs = [-math.inf for _ in nums]
        curr_max = -math.inf
        for i in range(len(nums)):
            curr_max = max(curr_max, sums[i])
            prefix_maxs[i] = curr_max

        print(f"{a=} {b=}")
        print(f"{sums=}")
        print(f"{suffix_maxs=}")
        print(f"{prefix_maxs=}")
        print(f"{nums=}")

        soln = -math.inf
        curr_sum = sum(nums[:b])
        if b < len(suffix_maxs):
            soln = max(soln, curr_sum + suffix_maxs[b])
        for i, n in enumerate(nums[b:], start=b):
            curr_sum -= nums[i-b]
            curr_sum += n
            if i - a >= 0:
                soln = max(soln, curr_sum + prefix_maxs[i-b])
            if i + a < len(suffix_maxs):
                soln = max(soln, curr_sum + suffix_maxs[i+a])
            print(f"{i=} {i-b=} {n=} {curr_sum=} {soln=}")
        return soln


def test_1():
    nums = [2, 1, 9, -3, 6, 5]
    a = 3
    b = 1
    expected = 18
    assert Solution().solve(nums, a, b) == expected


def test_2():
    "WA"
    nums = [1,-2,-2,-2]
    a = 2
    b = 1
    expected = -3
    assert Solution().solve(nums, a, b) == expected
