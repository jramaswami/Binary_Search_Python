"""
binarysearch.com :: Target Number with Operations Sequel
jramaswami
"""


class Solution:

    def solve(self, start, end):
        ops = 0
        n = end
        while n > start:
            ops += 1
            if n % 2:
                n = n + 1
            else:
                n = n // 2
        return ops + (start - n)


def test_1():
    start = 5
    end = 9
    expected = 2
    assert Solution().solve(start, end) == expected


def test_2():
    start = 26
    end = 48
    expected = 3
    assert Solution().solve(start, end) == expected


def test_3():
    "TLE"
    start = 19489024
    end = 79601032
    expected = 9538898
    assert Solution().solve(start, end) == expected
