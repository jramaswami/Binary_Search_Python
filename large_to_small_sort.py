"""
binarysearch.com :: Large to Small Sort
https://binarysearch.com/problems/Large-to-Small-Sort
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        left = 0
        right = len(nums) - 1
        soln = []
        while left <= right:
            soln.append(nums[right])
            if left < right:
                soln.append(nums[left])
            left += 1
            right -= 1
        return soln


def test_1():
    nums = [5, 2, 9, 3]
    solver = Solution()
    assert solver.solve(nums) == [9, 2, 5, 3]

def test_2():
    nums = nums = [1, 9, 9]
    solver = Solution()
    assert solver.solve(nums) == [9, 1, 9]
            
