"""
binarysearch.com :: Range Update
jramaswami
"""


class Solution:

    def solve(self, nums, operations):
        delta = [0 for _ in nums]
        for l, r, x in operations:
            delta[l] += x
            if r + 1 < len(delta):
                delta[r+1] -= x

        curr = 0
        soln = [0 for _ in nums]
        for i, n in enumerate(nums):
            curr += delta[i]
            soln[i] = n + curr
        return soln



def test_1():
    nums = [7, 3, 1, -10, 3]
    operations = [
        [0, 0, 3],
        [1, 3, 2],
        [2, 3, 5]
    ]
    expected = [10, 5, 8, -3, 3]
    assert Solution().solve(nums, operations) == expected


