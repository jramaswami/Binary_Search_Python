"""
binarysearch.com :: Square of a List
jramaswami
"""
class Solution:
    def solve(self, nums):
        left = 0
        right = len(nums) - 1
        soln = []
        while len(soln) < len(nums):
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            if right_sq > left_sq:
                soln.append(right_sq)
                right -= 1
            else:
                soln.append(left_sq)
                left += 1
        return soln[::-1]


def test_1():
    nums = [-9, -2, 0, 2, 3]
    assert Solution().solve(nums) == [0, 4, 4, 9, 81]

def test_2():
    nums = [1, 2, 3, 4, 5]
    assert Solution().solve(nums) == [1, 4, 9, 16, 25]
