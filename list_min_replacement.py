"""
binarysearch.com :: List Min Replacement
jramaswami
"""
class Solution:
    def solve(self, nums):
        nums0 = [0]
        curr_min = nums[0]
        for n in nums[1:]:
            nums0.append(curr_min)
            curr_min = min(curr_min, n)
        return nums0


def test_1():
    assert Solution().solve([10, 5, 7, 9]) == [0, 10, 5, 5]
