"""
binarysearch.com :: Strictly Increasing or Strictly Decreasing
https://binarysearch.com/problems/Strictly-Increasing-or-Strictly-Decreasing
"""
class Solution:
    def solve(self, nums):
        # Base case
        if len(nums) < 2:
            return True

        # Check the first and last to see which direction we should be heading
        if nums[0] < nums[-1]:
            return all(a < b for a, b in zip(nums[:-1], nums[1:]))
        elif nums[0] > nums[-1]:
            return all(a > b for a, b in zip(nums[:-1], nums[1:]))
        else:
            # If the two are equal then we cannot have either strictly
            # increasing or strictly decreasing.
            return False

def test_1():
    nums = [1, 2, 3, 4, 5]
    solver = Solution()
    assert solver.solve(nums) == True

def test_2():
    nums = [1, 2, 3, 4, 5, 5]
    solver = Solution()
    assert solver.solve(nums) == False

def test_3():
    nums = [5, 4, 3, 2, 1]
    solver = Solution()
    assert solver.solve(nums) == True

def test_4():
    nums = []
    solver = Solution()
    assert solver.solve(nums) == True

def test_5():
    nums = [2]
    solver = Solution()
    assert solver.solve(nums) == True

