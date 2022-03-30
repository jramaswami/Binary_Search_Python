"""
binarysearch.com :: Remove Sublist to Reach Equilibrium
jramaswami
"""


class Solution:

    def solve(self, nums, k):
        def sign(n):
            if n > k:
                return 1
            if n < k:
                return -1
            return 0

        nums0 = [sign(n) for n in nums]
        delta = sum(nums0)
        if delta == 0:
            return len(nums)
        prev_sums = dict()
        prev_sums[0] = -1
        curr_sum = 0
        soln = len(nums)
        for i, n in enumerate(nums0):
            curr_sum = curr_sum + n
            look_for = curr_sum - delta
            if look_for in prev_sums:
                soln = min(soln, i - prev_sums[look_for])
            prev_sums[curr_sum] = i
        return len(nums) - soln


def test_1():
    nums = [5, 9, 7, 8, 2, 4]
    k = 5
    expected = 5
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 2, 3]
    k = 4
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [0]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected


def test_4():
    "WA"
    nums = [1,2,2,3,0]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected
