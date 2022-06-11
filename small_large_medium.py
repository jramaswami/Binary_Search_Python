"""
binarysearch.com :: Small Large Medium
jramaswami
"""


import math


class Solution:

    def solve(self, nums):
        T = []
        curr_second_max = -math.inf
        for n in reversed(nums):
            # If n < curr_second_max then this implies
            # n < curr_second_max < unrecorded first max.
            if n < curr_second_max:
                return True
            # Find the highest number < n.
            while T and n > T[-1]:
                curr_second_max = max(curr_second_max, T[-1])
                T.pop()
            T.append(n)
        return False



def test_1():
    nums = [1, 10, 0, 3, 3]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 2, 3, 4, 5, 6]
    expected = False
    assert Solution().solve(nums) == expected


def test_3():
    nums = [6, 5, 4, 3, 2, 1]
    expected = False
    assert Solution().solve(nums) == expected


def test_5():
    nums = [1, 2, 3, 3, 3, 4, 5]
    expected = False
    assert Solution().solve(nums) == expected


def test_6():
    "WA"
    nums = [1, 2, 0]
    expected = False
    assert Solution().solve(nums) == expected


def test_7():
    "WA"
    nums = [0,3,2,0]
    expected = True
    assert Solution().solve(nums) == expected


def test_8():
    "WA"
    nums = [1,3,2,3]
    expected = True
    assert Solution().solve(nums) == expected
