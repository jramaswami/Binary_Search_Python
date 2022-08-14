"""
binarysearch.com :: Smallest Sublist Sum at Least Target
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, nums, target):

        def check(k):
            """
            Return True if there are any k-length sublists that sum greater
            than or equal to target.
            """
            window = collections.deque(nums[:k])
            window_sum = sum(window)
            if window_sum >= target:
                return True
            for n in nums[k:]:
                window_sum -= window[0]
                window.popleft()
                window.append(n)
                window_sum += window[-1]
                if window_sum >= target:
                    return True
            return False

        lo = 1
        hi = len(nums)
        soln = len(nums) + 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = min(soln, mid)
                hi =  mid - 1
            else:
                lo = mid + 1
        return soln if soln <= len(nums) else -1


def test_1():
    nums = [1, 10, -5, 15, 3]
    target = 17
    expected = 2
    assert Solution().solve(nums, target) == 2