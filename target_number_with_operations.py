"""
binarysearch.com :: Target Number with Operations
jramaswami
"""


class Solution:

    def solve(self, start, end):
        soln = 0
        while end != start:
            if end // 2 >= start:
                soln += 1
                if end % 2 == 0:
                    end //= 2
                else:
                    end -= 1
            else:
                soln += (end - start)
                end = start
        return soln


def test_1():
    start = 2
    end = 9
    expected = 3
    assert Solution().solve(start, end) == expected


def test_2():
    "TLE"
    start = 500000001
    end = 1000000000
    expected = 499999999
    assert Solution().solve(start, end) == expected