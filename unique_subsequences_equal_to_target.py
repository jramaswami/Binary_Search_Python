"""
binarysearch.com :: Unique Subsequences Equal to Target
jramaswami
"""


import collections
import sys


sys.setrecursionlimit(pow(10, 9))
MOD = pow(10, 9) + 7


class Solution:

    def solve(self, S, T):
        # Corner case.
        if T == "":
            return 0

        letter_indexes = collections.defaultdict(list)
        for i, c in enumerate(S):
            letter_indexes[c].append(i)

        def traverse(s_index, t_index):
            # Base case: we have reached the end of T.  This is one way
            # to do so.
            if t_index >= len(T):
                return 1

            result = 0
            c = T[t_index]
            # Go to every possible c in S such thsat the index of c is greater
            # than the current s_index.
            for s_index0 in letter_indexes[c]:
                if s_index0 > s_index:
                    result = (result + traverse(s_index0, t_index + 1)) % MOD
            return result

        return traverse(-1, 0) % MOD


def test_1():
    S = "ello"
    T = "el"
    expected = 2
    assert Solution().solve(S, T) == expected


def test_2():
    "WA"
    S = "hello"
    T = ""
    expected = 0
    assert Solution().solve(S, T) == expected