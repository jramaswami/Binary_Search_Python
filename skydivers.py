"""
binarysearch.com :: Skydivers
jramaswami
"""


class Solution:

    def solve(self, nums, k):

        def check(plane_capacity):
            curr_sum = 0
            curr_days = 0
            for n in nums:
                if curr_sum + n > plane_capacity:
                    curr_sum = n
                    curr_days += 1
                else:
                    curr_sum += n
            if curr_sum:
                curr_days += 1
            return curr_days <= k

        # Binary search for the answer.
        lo = 0
        hi = sum(nums)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln


def test_1():
    nums = [13, 17, 30, 15, 17]
    k = 3
    expected = 32
    assert Solution().solve(nums, k) == expected


def test_2():
    "WA"
    nums = [909]
    k = 2
    expected = 909
    assert Solution().solve(nums, k) == expected
