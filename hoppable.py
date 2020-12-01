"""
binarysearch.com :: Hoppable
https://binarysearch.com/problems/Hoppable
"""
class Solution:
    def solve(self, nums):
        max_reachable = 0
        for i, hops in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + hops)
        return max_reachable >= len(nums) - 1


def test_1():
    solver = Solution()
    nums = [1, 0, 0, 0]
    assert solver.solve(nums) == False

def test_2():
    solver = Solution()
    nums = [2, 4, 0, 1, 0]
    assert solver.solve(nums) == True

def test_3():
    solver = Solution()
    nums = [1, 1, 0, 1]
    assert solver.solve(nums) == False

def test_4():
    solver = Solution()
    nums = [0, 2, 3]
    assert solver.solve(nums) == False