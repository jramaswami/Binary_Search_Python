"""
binarysearch.com :: Number of Operations to Decrement Target to Zero
jramaswami
"""
from math import inf
from collections import deque


class Solution:
    def solve(self, nums, target):
        # Edge cases.
        if target == 0:
            return 0
        if nums == []:
            return -1

        N = len(nums)
        target0 = sum(nums) - target

        # If the entire thing sums to target, then return length.
        if target0 == 0:
            return N

        # If there isn't enough in the entire array, then we can't do it.
        if target0 < 0:
            return -1

        ssum = nums[0]
        sublist = deque()
        sublist.append(nums[0])
        soln = inf

        # Check with just the first number.
        if ssum == target0:
            soln = min(soln, N - len(sublist))

        for right in nums[1:]:
            # Add next number
            ssum += right
            sublist.append(right)

            # If we have gone above target number, remove from left
            while ssum > target0:
                ssum -= sublist[0]
                sublist.popleft()

            # If the current subarray sums to target0, then the ends
            # sum to target.
            if ssum == target0:
                soln = min(soln, N - len(sublist))
        return -1 if soln == inf else soln


def test_1():
    nums = [3, 1, 1, 2, 5, 1, 1]
    target = 7
    assert Solution().solve(nums, target) == 3

def test_2():
    nums = [2, 4]
    target = 7
    assert Solution().solve(nums, target) == -1

def test_3():
    nums = []
    target = 0
    assert Solution().solve(nums, target) == 0

def test_4():
    nums = []
    target = 1
    assert Solution().solve(nums, target) == -1

def test_5():
    nums = [1]
    target = 1
    assert Solution().solve(nums, target) == 1

def test_6():
    nums = [1, 2]
    target = 2
    assert Solution().solve(nums, target) == 1
