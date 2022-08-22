"""
binarysearch.com :: Check if Number Is Perfect Square
jramaswami
"""


def binsearch(left, right, square):
    """Binary search for the answer."""
    while left <= right:
        mid = (left + right) // 2
        midsq = mid * mid
        if midsq == square:
            return mid
        elif midsq > square:
            right = mid - 1
        else:
            left = mid + 1
    return -1


class Solution:
    def solve(self, n):
        soln = binsearch(0, 2147488281, n)
        return soln >= 0


def test_1():
    assert Solution().solve(25) == True


def test_2():
    assert Solution().solve(0) == True


def test_3():
    assert Solution().solve(1) == True


def test_4():
    assert Solution().solve(13) == False