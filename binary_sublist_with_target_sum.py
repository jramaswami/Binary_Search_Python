"""
binarysearch.com :: Binary Sublist with Target Sum
jramaswami
"""


class Solution:

    def solve(self, nums, target):
        # Determine the min index of 1 to the right of any zero.
        one_right = [-1 for _ in nums]
        curr_one = -1
        for i, _ in enumerate(nums):
            j = len(nums) - i - 1
            if nums[j] == 1:
                curr_one = j
            one_right[j] = curr_one

        soln = 0
        left = 0
        right = -1
        curr_sum = 0
        while right < len(nums):
            # Add one to the right.
            right += 1
            if right >= len(nums):
                break
            curr_sum += nums[right]

            # If sum is too much, reduce sum.
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            # The number of sublists ending at right is the number of sublists
            # from current left to the first one to to the right of left.
            if curr_sum == target:
                soln += (1 + one_right[left] - left)

        return soln


def test_1():
    nums = [1, 0, 1, 1]
    target = 2
    expected = 3
    assert Solution().solve(nums, target) == expected


def test_2():
    """RTE"""
    nums = [1]
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected
