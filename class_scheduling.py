"""
binarysearch.com :: Class Scheduling
jramaswami
"""


class Solution:

    def solve(self, times):
        times.sort(key=lambda t: (t[1], t[0]))
        curr_stop = -1
        soln = 0
        for start, stop in times:
            if start > curr_stop:
                curr_stop = stop
                soln += 1
        return soln


def test_1():
    times = [
        [2, 5],
        [5, 8],
        [6, 7],
        [8, 10]
    ]
    expected = 3
    assert Solution().solve(times) == expected


def test_2():
    times = []
    expected = 0
    assert Solution().solve(times) == expected
