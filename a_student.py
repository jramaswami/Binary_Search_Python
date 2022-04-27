"""
binarysearch.com :: A Student
jramaswami
"""


import heapq


class Solution:

    def solve(self, deadlines, credits):
        classes = [(d, c) for d, c in zip(deadlines, credits)]
        classes.sort(key=lambda t: (t[0], -t[1]))
        completed = []
        for d, c in classes:
            if len(completed) <= d:
                heapq.heappush(completed, c)
            elif completed[0] < c:
                heapq.heappop(completed)
                heapq.heappush(completed, c)
        return sum(completed)


def test_1():
    deadlines = [0, 1]
    credits = [3, 2]
    expected = 5
    assert Solution().solve(deadlines, credits) == expected


def test_2():
    deadlines = [1, 2, 2, 2]
    credits = [3, 4, 5, 6]
    expected = 15
    assert Solution().solve(deadlines, credits) == expected


def test_3():
    deadlines = []
    credits = []
    expected = 0
    assert Solution().solve(deadlines, credits) == expected
