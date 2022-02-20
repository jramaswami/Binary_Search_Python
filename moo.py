"""
binarysearch.com :: Moo
jramaswami
"""


import math


class Solution:

    def solve(self, cows):
        left = [0 for _ in cows]
        right = [0 for _ in cows]

        curr_left = math.inf
        for i in range(len(cows) - 1, -1, -1):
            cow = cows[i]
            if cow == 'L':
                curr_left = 0
            elif cow == 'R':
                curr_left = math.inf
            else:
                curr_left += 1
            left[i] = curr_left

        curr_right = math.inf
        for i, cow in enumerate(cows):
            if cow == 'R':
                curr_right = 0
            elif cow == 'L':
                curr_right = math.inf
            else:
                curr_right += 1
            right[i] = curr_right

        cows0 = list(cows)
        for i, _ in enumerate(cows0):
            if left[i] == right[i]:
                cows0[i] = '@'
            elif left[i] < right[i]:
                cows0[i] = 'L'
            elif right[i] < left[i]:
                cows0[i] = 'R'

        return "".join(cows0)


def test_1():
    cows = "@L@R@@@@L"
    expected = "LL@RRRLLL"
    assert Solution().solve(cows) == expected


def test_2():
    cows = "@@R@@@L@L"
    expected = "@@RR@LLLL"
    assert Solution().solve(cows) == expected
