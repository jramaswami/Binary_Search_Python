"""
binarysearch.com :: Longest Bitonic Subsequence
jramaswami
"""
class Solution:
    def solve(self, nums):
        longest_increasing = [1 for _ in nums]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    longest_increasing[j] = max(longest_increasing[j], longest_increasing[i] + 1)

        longest_decreasing = [1 for _ in nums]
        for i in range(len(nums)-1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[i]:
                    longest_decreasing[j] = max(longest_decreasing[j], longest_decreasing[i]  + 1)

        max_incr = [0 for _ in longest_increasing]
        max_incr[0] = longest_increasing[0]
        for i in range(1, len(max_incr)):
            max_incr[i] = max(max_incr[-1], longest_increasing[i])

        max_decr = [0 for _ in longest_decreasing]
        max_decr[-1] = longest_decreasing[-1]
        for i in range(len(longest_decreasing) - 2, -1, -1):
            max_decr[i] = max(max_decr[i+1], longest_decreasing[i])
        
        soln = 0
        for i in range(len(nums)):
            # The longest sequence that will increase to i and then 
            # decrease from i
            soln = max(soln, longest_increasing[i] + longest_decreasing[i] - 1)
            # The longest sequence that will increase to i and then 
            # decrease from some index greater than i
            if i + 1 < len(nums):
                soln = max(soln, max_incr[i] + max_decr[i+1])
        return soln


def test_1():
    nums = [1, 0, 3, 2, 9, 4, 5, 2]
    assert Solution().solve(nums) == 5

def test_2():
    nums = [10, 2, 5, 7, 3, 1]
    assert Solution().solve(nums) == 5

def test_3():
    nums = [1, 3, 2, 5, 9]
    assert Solution().solve(nums) == 4

def test_4():
    nums = [795, 441, 916, 874, 990, 929, 25, 59, 391, 914, 219, 685, 208, 20, 983, 706, 831, 426, 350, 281, 77, 659, 949, 1019, 360, 271, 777, 453]
    assert Solution().solve(nums) == 10

def test_5():
    nums = [713, 464, 628, 504, 111, 503, 465, 148]
    assert Solution().solve(nums) == 6
