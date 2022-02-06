"""
binarysearch.com :: Remove Duplicates Occurring More Than Twice
jramaswami
"""


class Solution:

    def solve(self, nums):
        # Special case: empty list.
        if not nums:
            return nums

        # Mark numbers for removal.
        removals = 0
        curr_count = 1
        curr_value = nums[0]
        for i, n in enumerate(nums[1:], start=1):
            if n == curr_value:
                curr_count += 1
            else:
                curr_count = 1
                curr_value = n
            if curr_count > 2:
                nums[i] = None

        # Swap good values and then remove extraneous values.
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] is None:
                right += 1
                removals += 1
            else:
                nums[left] = nums[right]
                right += 1
                left += 1
        for _ in range(removals):
            nums.pop()
        return nums


def test_1():
    nums = [3, 3, 3, 3, 4, 4, 8]
    expected = [3, 3, 4, 4, 8]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1,1]
    expected = [1,1]
    assert Solution().solve(nums) == expected
