"""
binarysearch.com :: 5-Star Review Percentage
jramaswami
"""
from math import ceil
from fractions import Fraction
class Solution:
    def solve(self, reviews, threshold):
        x = 0
        y = 0
        for a, b in reviews:
            x += a
            y += b

        if threshold == 100 and x == y:
            return 0

        x0 = Fraction(x, 1)
        y0 = Fraction(y, 1)
        t0 = Fraction(threshold, 100)
        k = ((t0 * y0) - x) / (Fraction(1, 1) - t0)
        return max(0, ceil(k))
   
def test_1():
    reviews = [
        [4, 4],
        [1, 2],
        [3, 6]
    ]
    threshold = 77
    assert Solution().solve(reviews, threshold) == 6

def test_2():
    reviews = [
        [10, 20]
    ]
    threshold = 50
    assert Solution().solve(reviews, threshold) == 0

def test_3():
    reviews = [
        [1, 1]
    ]
    threshold = 100
    assert Solution().solve(reviews, threshold) == 0

def test_4():
    reviews = [
        [1, 2],
        [2, 5],
        [2, 5],
        [0, 1]
    ]
    threshold = 0
    assert Solution().solve(reviews, threshold) == 0

