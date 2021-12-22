"""
binarysearch.com :: Triangle Triplets
jramaswami
"""


class Solution:

    def solve(self, nums):
        soln = 0
        nums.sort()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                for k, c in enumerate(nums[j+1:], start=j+1):
                    if a + b > c:
                        soln += 1
        return soln


def test_1():
    nums = [7, 8, 8, 9, 100]
    assert Solution().solve(nums) == 4
