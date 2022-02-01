"""
binarysearch.com :: Largest Average of Sublist with Length at Least K
jramaswami

Given a sublist of length k [a1, a2, a3, ... ak], the average will be:

(a1 + a2 + a3 + ... + ak) / k = avg.
a1 + a2 + a3 + ... + ak = k * avg
a1 + a2 + a3 + ... + ak = avg + avg + avg + ... avg   (k times)
(a1 - avg) + (a2 - avg) - ... - (ak - avg) = 0

So if we subtract the target average from each element of the sublist and take
the sum, then the sublist will have an average of at least the target average
if that sum is greater than or equal to zero.

Rather than try every sublist we can use prefix sums to check for every sublist
ending at a given index. Suppose we are at index i.  Then our total list will
be [a1, a2, ..., ai].  For a given index j, we can compute the sum of our
sublist [aj+1, ..., ai] by taking the sum of [a1 ... ai] and subtracting the
sum of [a0 ... aj].

We want our sublist to have a sum greater than or equal to zero so we want:
sum([a0 ... ai]) - sum([a0 ... aj]) >= 0.  In order to see if that is possible,
we will keep track of the minimum sum([a0 ... aj]).  Any time the total sum
ending at index, i, less than minimum sum of any sublist ending between 0 and j
is greater than or equal to zero, there is a sublist with an average equal to
or greater than our target average.
"""


class Solution:

    def solve(self, nums, k):

        def check(target_avg, k):
            """
            Check if there is a sublist with an average >= target_avg.
            """
            prev_sum = curr_sum = min_prev_sum = 0
            for i, n in enumerate(nums):
                curr_sum += (n - target_avg)
                if i >= k:
                    prev_sum += (nums[i-k] - target_avg)
                    min_prev_sum = min(min_prev_sum, prev_sum)
                if i >= k - 1 and curr_sum >= min_prev_sum:
                    return True
            return False

        # Binary search limits.
        eps = 0.000001
        low, high = min(nums), max(nums)
        soln = low
        while abs(high - low) > eps:
            mid = (low + high) / 2
            if check(mid, k):
                soln = max(soln,  mid)
                low = mid
            else:
                high = mid
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
