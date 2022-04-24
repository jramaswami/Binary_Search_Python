"""
binarysearch.com :: Number of Swaps to Sort
jramaswami
"""


class Solution:
    def solve(self, nums):
        locations = {n: i for i, n in enumerate(sorted(nums))}
        soln = 0
        for i, _ in enumerate(nums):
            # j is the index where nums[i] should be.
            j = locations[nums[i]]
            while j != i:
                soln += 1
                nums[i], nums[j] = nums[j], nums[i]
                j = locations[nums[i]]
        return soln


def test_1():
    nums = [3, 2, 1, 4]
    expected = 1
    assert Solution().solve(nums) == expected
