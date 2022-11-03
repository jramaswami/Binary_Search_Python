"""
binarysearch.com :: Largest Pair of Points
https://binarysearch.com/room/Weekly-Contest-36-ngNTQirTtw
"""
class Solution:
    def solve(self, nums, values):
        print(nums, values)
        a = max(v-n for n, v in zip(nums, values))
        b = max(v+n for n, v in zip(nums, values))
        return a + b

def test_1():
    solver = Solution()
    nums = [0, 1, 6]
    values = [-5, 5, 4]
    assert solver.solve(nums, values) == 14

def test_2():
    solver = Solution()
    nums = [0, 3, 6]
    values = [-5, 4, 8]
    assert solver.solve(nums, values) == 16