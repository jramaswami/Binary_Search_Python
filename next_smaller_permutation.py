"""
binarysearch.com :: Next Smaller Permutation
jramaswami
"""
class Solution:
    def solve(self, nums):
        if not nums:
            return []

        # Do not mutate the argument.
        nums0 = list(nums)

        # Find the longest non-decreasing suffix
        pivot_index = -1
        for i in range(len(nums0) - 1, 0, -1):
            if nums0[i-1] > nums0[i]:
                pivot_index = i - 1
                break

        # If you cannot find a pivot, then the digits are in sorted order
        # so there is no previous permutation.
        if pivot_index < 0:
            return nums0

        # Find the largest element smaller than our pivot. If there are
        # equals, take the first.
        swap_index = -1
        swap_value = -1 
        for j, x in enumerate(nums[pivot_index+1:], start=pivot_index+1):
            if x < nums0[pivot_index] and x > swap_value:
                swap_index = j
                swap_value = x

        # Swap pivot and swap_value
        nums0[pivot_index], nums0[swap_index] = nums0[swap_index], nums0[pivot_index]

        return nums0



def test_1():
    nums = [2, 0, 1]
    assert Solution().solve(nums) == [1, 0, 2]

def test_2():
    nums = [1, 2, 3]
    assert Solution().solve(nums) == [1, 2, 3]

def test_3():
    assert Solution().solve([]) == []

def test_4():
    nums = [2, 0, 0]
    assert Solution().solve(nums) == [0, 2, 0]

def test_4():
    nums = [1, 1, 0]
    assert Solution().solve(nums) == [1, 0, 1]
