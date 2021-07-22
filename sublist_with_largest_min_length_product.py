"""
binarysearch.com :: Sublist with Largest Min-Length Product
jramaswami
"""


from math import inf


class Solution:
    def solve(self, nums, pos):
        i = j = pos
        curr_min = nums[pos]
        soln = nums[pos]
        while i > 0 or j < len(nums) + 1:
            # Expand to the largest number left or right.
            left = -inf if i - 1 < 0 else nums[i-1]
            right = -inf if j + 1 >= len(nums) else nums[j+1]

            if left > right:
                i -= 1
                curr_min = min(curr_min, left)
            else:
                j += 1
                curr_min = min(curr_min, right)
            soln = max(soln, (j - i + 1) * curr_min)
        return soln


def test_1():
    nums = [-1, 1, 4, 3]
    pos = 3
    assert Solution().solve(nums, pos) == 6


def test_2():
    nums = [4, 2, 3, 10, 10, 5, 6, 10, 2, 9]
    pos = 6
    assert Solution().solve(nums, pos) == 25
