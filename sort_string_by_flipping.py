"""
binarysearch.com :: Sort String by Flipping
jramaswami
"""


class Solution:

    def solve(self, S):
        ys_left = [0 for _ in S]
        xs_right = [0 for _ in S]

        curr_ys = 0
        for i, c in enumerate(S):
            ys_left[i] = curr_ys
            if c == 'y':
                curr_ys += 1

        curr_xs = 0
        for off, c in enumerate(reversed(S)):
            i = len(S) - 1 - off
            xs_right[i] = curr_xs
            if c == 'x':
                curr_xs += 1

        soln = len(S)
        for yl, xr in zip(ys_left, xs_right):
            soln = min(soln, yl + xr)
        return soln


def test_1():
    S = "xyxxxyxyy"
    assert Solution().solve(S) == 2


def test_2():
    S = "xxxxxyxyyyxyxyxyxyxyyyxyxyxyxyxyxyxyxyxxxxyxyyyyyyxyxyxyxyyxyyxyxyxyyyyyyxyxyxyxxy"
    assert Solution().solve(S) == 32
