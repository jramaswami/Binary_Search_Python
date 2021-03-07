"""
binarysearch.com :: Just Average
jramaswami

Given a list of integers nums and an integer k, return true if you can remove
exactly one element from the list to make the average equal to exactly k.

Normally: avg = sum(nums) / len(nums)

We want to remove one item, x, to make the average k. So out equations becomes:
k = (sum(nums) - x) / (len(nums) - 1)

Do a little algebra.

k * (len(nums) - 1) = sum(nums) - x
k * (len(nums) - 1) - sum(nums) = -x
sum(nums) - (k * (len(nums) - 1)) = x
"""
class Solution:
    def solve(self, nums, k):
        N = len(nums)
        S = sum(nums)
        x = S - (k * (N - 1))
        return x in nums


def test_1():
    nums = [1, 2, 3, 10]
    k = 2
    assert Solution().solve(nums, k) == True

def test_2():
    nums = [1, 3]
    k = 2
    assert Solution().solve(nums, k) == False



