"""
binarysearch.com :: Number of Operations to Decrement Target to Zero
jramaswami
"""
from math import inf


class Solution:
    def solve(self, nums, target):
        if target == 0:
            return 0

        if nums == []:
            return -1
        
        N = len(nums)
        prefix = [0 for _ in range(N+1)]
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + nums[i-1]

        suffix = [0 for _ in range(N)]
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i] + suffix[i+1]
        suffix.append(0)

        soln = inf
        for left, _ in enumerate(prefix):
            for right in range(len(suffix)-1, left-1, -1):
                if prefix[left] + suffix[right] == target:
                    S = left + (N - right)
                    soln = min(soln, S)
                elif prefix[left] + suffix[right] > target:
                    break

        return (-1 if soln == inf else soln)


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

