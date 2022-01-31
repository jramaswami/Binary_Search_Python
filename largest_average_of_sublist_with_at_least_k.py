"""
binarysearch.com :: Largest Average of Sublist with Length at Least K
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, nums, k):
        sums = [-math.inf for _ in nums]
        counts = [0 for _ in nums]
        sums[k-1] = sum(nums[:k])
        counts[k-1] = k
        solns = [None for _ in nums]
        prefix = sums[k-1]
        window = collections.deque(nums[:k])
        solns[k-1] = collections.deque(window)
        assert len(window) == k
        for i, _ in enumerate(nums[k:], start=k):
            prefix -= window[0]
            window.popleft()
            prefix += nums[i]
            window.append(nums[i])
            assert len(window) == k
            sums[i] = prefix
            counts[i] = k
            solns[i] = collections.deque(window)
            print(f"{i=} {window=} {sums[i]=} {sums[i] / counts[i]}")

            # Can I increase the average ending at i by adding
            # nums[i] to the best average ending at i-1?
            if counts[i-1] + 1 >= k and (nums[i] + sums[i-1]) / (counts[i-1] + 1) > sums[i] / counts[i]:
                sums[i] = nums[i] + sums[i-1]
                counts[i] = counts[i-1] + 1
                solns[i] = collections.deque(solns[i-1])
                solns[i].append(nums[i])
                print(f"adding {nums[i]} -> {solns[i]} {sums[i]=} {sums[i] / counts[i]}")


        print(f"{prefix=}")
        print(f"{sums=}")
        print(f"{counts=}")
        print(f"{[s / c for s, c in zip(sums, counts) if c > 0]}")
        print(f"{solns=}")

        soln = max(s / c for s, c in zip(sums, counts) if c > 0)
        return soln


#
# Testing
#

import random


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


# def test_random():
#     for _ in range(100):
#         nums = [random.randint(-100, 100) for _ in range(10)]
#         k = random.randint(1, len(nums))
#         expected = brute(nums, k)
#         if not (expected - EPS <= Solution().solve(nums, k) <= expected + EPS):
#             print(nums, k)
#         assert expected - EPS <= Solution().solve(nums, k) <= expected + EPS


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
