"""
binarysearch.com :: Sum of Three Numbers Sequel
jramaswami
"""


import bisect


class Solution:
    def solve(self, nums, target):
        nums.sort()
        soln = abs(target - (sum(nums[:3])))
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                d = target - n - m
                # Find index of leftmost value less than or equal to d.
                k = bisect.bisect_left(nums, d) - 1
                print(f"{i=} {n=} {j=} {m=} {d=} {k=}")
                if k > j:
                    soln = min(soln, abs(target - (n + m + nums[k])))
                    if k + 1 < len(nums):
                        soln = min(soln, abs(target - (n + m + nums[k+1])))
        return soln


def test_1():
    nums = [2, 4, 25, 7]
    k = 15
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [2, 4, 25, 7]
    k = 0
    expected = 13
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [1,-1,0,-2]
    k = 0
    expected = 0
    assert Solution().solve(nums, k) == expected
