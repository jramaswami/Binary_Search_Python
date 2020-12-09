"""
binarysearch.com :: Largest Number By Two Times
https://binarysearch.com/problems/Largest-Number-By-Two-Times
"""
class Solution:
    def solve(self, nums):
        # Base case
        if len(nums) < 2:
            return False

        nums.sort()
        return nums[-1] > 2 * nums[-2]

def test_1():
    nums = [3, 6, 9]
    solver = Solution()
    assert solver.solve(nums) == False

def test_2():
    nums = [3, 6, 15]
    solver = Solution()
    assert solver.solve(nums) == True

def test_3():
    nums = [3, 6, 12]
    solver = Solution()
    assert solver.solve(nums) == False
