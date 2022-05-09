"""
binarysearch.com :: Sublists Containing Maximum and Minimum
jramaswami
"""


import heapq
import collections


class Solution:

    def solve(self, nums):

        def count_subarrays(mn, mx, arr):
            mx_freq = mn_freq = result = 0
            window = collections.deque()
            for i, n in enumerate(arr):
                window.append((n, i))
                if n == mx:
                    mx_freq += 1
                if n == mn:
                    mn_freq += 1

                while window and mx_freq > 0 and mn_freq > 0:
                    # Every subarray from the index of the first element
                    # in the window to the end of the array contains both
                    # mn and mx.
                    _, j = window[-1]
                    k, _ = window.popleft()
                    result += len(arr) - j
                    if k == mx:
                        mx_freq -= 1
                    if k == mn:
                        mn_freq -= 1
            return result

        if len(nums) < 2:
            return len(nums)

        min_q = [-nums[0]]
        max_q = [nums[0]]
        for i, n in enumerate(nums[1:], start=1):
            heapq.heappush(min_q, -n)
            heapq.heappush(max_q, n)
            while len(min_q) > 2:
                heapq.heappop(min_q)
            while len(max_q) > 2:
                heapq.heappop(max_q)

        # Count of subarrays.
        mn, mn2 = -min_q[1], -min_q[0]
        mx, mx2 = max_q[1], max_q[0]
        soln = count_subarrays(mn, mx, nums)
        if mx != mx2:
            t = count_subarrays(mn, mx2, [n for n in nums if n != mx])
            soln = max(soln, t)
        if mn != mn2:
            t = count_subarrays(mn2, mx, [n for n in nums if n != mn])
            soln = max(soln, t)
        return soln


def test_1():
    nums = [2, 1, 5, 1, 3, 9]
    expected = 8
    assert Solution().solve(nums) == expected


def test_2():
    nums = [5, 5]
    expected = 3
    assert Solution().solve(nums) == expected


def test_3():
    nums = [1]
    expected = 1
    assert Solution().solve(nums) == expected


def test_4():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected


def test_5():
    "WA"
    nums = [2, 2, 0]
    expected = 3
    assert Solution().solve(nums) == expected