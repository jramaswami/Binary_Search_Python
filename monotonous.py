"""
binarysearch.com :: Half Monotonous String
https://binarysearch.com/room/Weekly-Contest-36-ngNTQirTtw?questionsetIndex=1
"""
from collections import defaultdict
from itertools import accumulate
from math import inf

class Solution:
    def solve(self, s):
        # Determine minium cost to change all characters to the same
        freqs = [0 for _ in range(26)]
        freqs_left = [0 for _ in range(26)]
        freqs_right = [0 for _ in range(26)]
        ord_a = ord('a')
        midpoint = len(s) // 2
        for i, c in enumerate(s):
            freqs[ord(c) - ord_a] += 1
            if i < midpoint:
                freqs_left[ord(c) - ord_a] += 1
            else:
                freqs_right[ord(c) - ord_a] += 1
        max_freq = max(freqs)
        soln = len(s) - max_freq

        left_prefix = list(accumulate(freqs_left))
        right_prefix = list(accumulate(freqs_right))
        left_suffix = list(accumulate(freqs_left[::-1]))[::-1]
        right_suffix = list(accumulate(freqs_right[::-1]))[::-1]

        print(s[:midpoint])
        print(left_prefix)
        print(left_suffix)
        less_than = inf
        for l, r in zip(left_prefix, right_prefix):
            # There are l chars less than equal to chr(i) in left string
            # There are r chars less than equal to chr(i) in right string
            # To make left string < right string we can move the right
            # string up or the left string down.

            # To make right go up, there must be left_prefix[i] > right_prefix[i].

            # To make left go down, there must be



def test_1():
    s = "aa"
    solver = Solution()
    assert solver.solve(s) == 0

def test_2():
    s = "aaabba"
    solver = Solution()
    assert solver.solve(s) == 1

def test_3():
    s = "bccbba"
    solver = Solution()
    assert solver.solve(s) == 1

def test_4():
    s = "dcca"
    solver = Solution()
    assert solver.solve(s) == 1