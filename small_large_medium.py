"""
binarysearch.com :: Small Large Medium
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        T = collections.deque()
        for n in reversed(nums):
            if len(T) > 1 and n < T[0]:
                return True
            if not T or n > T[-1]:
                T.append(n)
            while len(T) > 2:
                T.popleft()
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
