"""
binarysearch.com :: Special Product Array
https://binarysearch.com/problems/Special-Product-Array
"""
from operator import mul
from itertools import accumulate

class Solution:
    def solve(self, nums):
        product_left = [1 for _ in nums]
        product_left[0] = nums[0]
        for i in range(1, len(nums)):
            product_left[i] = product_left[i-1]*nums[i]
        print(product_left)
        product_right = [1 for _ in nums]
        product_right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            product_right[i] = product_right[i+1]*nums[i]
        print(product_right)

        product = [0 for _ in nums]
        for i in range(len(nums)):
            left = right = 1
            if i > 0:
                left = product_left[i-1]
            if i + 1 < len(nums):
                right = product_right[i+1]
            product[i] = left * right
        return product


def test_1():
    solver = Solution()
    nums = [1, 2, 3, 4, 5]
    assert solver.solve(nums) == [120, 60, 40, 30, 24]

def test_2():
    solver = Solution()
    nums = [3, 2, 1]
    assert solver.solve(nums) == [2, 3, 6]

def test_3():
    solver = Solution()
    nums = [1, 2]
    assert solver.solve(nums) == [2, 1]