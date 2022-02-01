"""
binarysearch.com :: Largest Average of Sublist with Length at Least K
jramaswami

REF: https://www.tutorialspoint.com/program-to-find-largest-average-of-sublist-whose-size-at-least-k-in-python
"""


class Solution:

    def solve(self, nums, k):
        # Binary search limits.
        low, high = min(nums), max(nums)
        # Initial solution.
        ssum = sum(nums[:k])
        soln = ssum / k

        while low <= high:
            mid = low + ((high - low) // 2)
            sum1 = ssum
            avg = ssum / k
            sum2 = cnt = 0
            # Window of elements starting at k.
            for i, _ in enumerate(nums[k:], start=k):
                # Add element to the current sum of the current window.
                sum1 += nums[i]
                # Add the trailing element to the sum of the trailing window.
                sum2 += nums[i-k]
                # Add to the number of elements over k.
                cnt += 1
                # Take the maximum average considering the current window.
                avg = max(avg, sum1 / (cnt + k))
                # If the average of the trailing window is less than or equal
                # to the current mid average then remove the trailing window.
                if sum2 / cnt <= mid:
                    sum1 -= sum2
                    sum2 = cnt = 0
                # Take the maximum average considering the current window.
                avg = max(avg, sum1 / (cnt + k))
            # Take the maximum solution considering the best average we got.
            soln = max(soln, avg)
            if avg > mid:
                low = mid + 1
            else:
                high = mid - 1
        return soln

#
# Testing
#


import random
import math


EPS = pow(10, -6)


def brute(nums, k):
    soln = -math.inf
    indexes = None
    for start, _ in enumerate(nums):
        for end in range(start + k, len(nums)+1):
            S = sum(nums[start:end])
            T = end - start
            avg = S / T
            if avg > soln:
                soln = avg
                indexes = (start, end)
            print(f"{start=} {end=} {nums[start:end]=} {S=} {T=} {avg=}")
            soln = max(soln, avg)
    print(f"brute {nums=} {soln=} {indexes=} {sum(nums[indexes[0]:indexes[1]])}")
    return soln


def test_brute():
    nums = [1, 9, -100, 3, 5, 5]
    k = 3
    expected = 4.33333333
    assert expected - EPS <= brute(nums, k) <= expected + EPS


def test_1():
    nums = [1, 9, -100, 3, 5, 5]
    k = 3
    expected = 4.33333333
    assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS


def test_random():
    for _ in range(100):
        nums = [random.randint(-100, 100) for _ in range(100)]
        k = random.randint(1, len(nums))
        expected = brute(nums, k)
        if not (expected - EPS <= Solution().solve(nums, k) <= expected + EPS):
            print(nums, k)
        assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS


def test_5():
    nums=[-43, -32, 53, -40, -33, 82, 79, 59, -42, 7]
    k=4
    expected = brute(nums, k)
    assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS


def test_6():
    nums, k = [1, -6, 81, 76, -59, -16, -51, 65, -97, -57], 9
    expected = brute(nums, k)
    assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS


def test_7():
    nums, k = [72, -77, 33, -91, 43, -39, -5, 85, -62, 82], 7
    expected = brute(nums, k)
    assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS
