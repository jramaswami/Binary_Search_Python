"""
binarysearch.com :: Weekly Contest 33 :: Max Multiplied Pairings
"""
from collections import deque

class Solution:
    def solve(self, nums, multipliers):
        nums = deque(sorted(nums))
        multipliers = deque(sorted(multipliers))

        soln = 0
        while nums and multipliers:
            left = nums[0] * multipliers[0]
            right = nums[-1] * multipliers[-1]
            if left > right:
                nums.popleft()
                multipliers.popleft()
                soln += left
            else:
                nums.pop()
                multipliers.pop()
                soln += right
        return soln


def test_1():
    nums = [-5, 3, 2]
    multipliers = [-3, 1]
    solver = Solution()
    assert solver.solve(nums, multipliers) == 18

