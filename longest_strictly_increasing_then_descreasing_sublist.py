"""
binarysearch.com :: Longest Strictly Increasing Then Decreasing Sublist
jramaswami
"""
class Solution:
    def solve(self, nums):
        longest_increasing = [1 for _ in nums]
        for i, (a, b) in enumerate(zip(nums[:-1], nums[1:])):
            if a < b:
                longest_increasing[i+1] = longest_increasing[i] + 1

        longest_decreasing = [1 for _ in nums]
        for negi, a in enumerate(reversed(nums[1:]), start=-(len(nums) - 1)):
            i = abs(negi)
            b = nums[i-1]
            if a < b:
                longest_decreasing[i-1] = longest_decreasing[i] + 1

        print(longest_increasing)
        print(longest_decreasing)
        return max(i + d - 1 if i > 1 and d > 1 else 0 for i, d in zip(longest_increasing, longest_decreasing))


def test_1():
    nums = [7, 1, 3, 5, 2, 0]
    assert Solution().solve(nums) == 5

def test_2():
    nums = [1, 2, 3]
    assert Solution().solve(nums) == 0

def test_3():
    nums = [1, 2, 0]
    assert Solution().solve(nums) == 3

def test_4():
    nums = [1, 0]
    assert Solution().solve(nums) == 0

def test_5():
    nums = [2, 3, 1, 0]
    assert Solution().solve(nums) == 4
