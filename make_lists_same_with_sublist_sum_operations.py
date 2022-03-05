"""
binarysearch.com :: Make Lists Same with Sublist Sum Operations
jramaswami
"""


import itertools


class Solution:
    def solve(self, l0, l1):
        prefix0 = list(itertools.accumulate(l0))
        prefix1 = list(itertools.accumulate(l1))

        # prev0 = prev1 = 0
        i = j = 0
        # sublists0 = []
        # sublists1 = []

        soln = 0
        while i < len(l0) and j < len(l1):
            if prefix0[i] == prefix1[j]:
                # sublists0.append(list(l0[prev0:i+1]))
                # sublists1.append(list(l1[prev1:j+1]))
                # prev0, prev1 = i, j
                i, j = i+1, j+1
                soln += 1
            elif prefix0[i] < prefix1[j]:
                i += 1
            elif prefix0[i] > prefix1[j]:
                j += 1

        if i == len(l0) and j == len(l1):
            # assert len(sublists0) == len(sublists1)
            # assert (sum(X) == sum(Y) for X, Y in zip(sublists0, sublists1))
            return soln
        return -1



def test_1():
    l0 = [1, 4, 7, 1, 2, 10]
    l1 = [5, 6, 1, 3, 10]
    expected = 4
    assert Solution().solve(l0, l1) == expected


def test_2():
    l0 = []
    l1 = [5, 6, 1, 3, 10]
    expected = -1
    assert Solution().solve(l0, l1) == expected


def test_3():
    l0 = [5, 6, 1, 3, 10]
    l1 = []
    expected = -1
    assert Solution().solve(l0, l1) == expected


def test_4():
    l0 = [1, 4, 7, 1, 2, 10]
    l1 = [5, 6, 1, 3, 11]
    expected = -1
    assert Solution().solve(l0, l1) == expected


def test_5():
    l0 = [10, 10, 10]
    l1 = [6, 4, 2, 3, 5, 1, 9]
    expected = 3
    assert Solution().solve(l0, l1) == expected


def test_6():
    l0 = [10, 20, 10]
    l1 = [6, 4, 2, 3, 5, 1, 9, 10]
    expected = 3
    assert Solution().solve(l0, l1) == expected
