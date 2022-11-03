"""
binarysearch.com :: Weekly Contest 32 :: Ball Moves 
https://binarysearch.com/room/Weekly-Contest-32-oSuVsQ17Hc?questionsetIndex=1
"""
class Solution:
    def solve(self, nums):
        N = len(nums)
        move_left = [0 for _ in nums]
        move_right = [0 for _ in nums]
        if nums:
            carrying = nums[0]
            for i in range(1, N):
                move_left[i] = move_left[i-1] + carrying
                carrying += nums[i]

            carrying = nums[-1]
            for i in range(N-2, -1, -1):
                move_right[i] = move_right[i+1] + carrying
                carrying += nums[i]

        soln = [l + r for l, r in zip(move_left, move_right)]
        return soln


def test_1():
    nums = [1, 1, 0, 1]
    solver = Solution()
    assert solver.solve(nums) == [4, 3, 4, 5]


def test_2():
    nums = []
    solver = Solution()
    assert solver.solve(nums) == []
