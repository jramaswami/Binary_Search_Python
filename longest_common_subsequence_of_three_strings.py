"""
binarysearch.com :: Longest Common Subsequence of Three Strings
jramaswami
"""


import functools


class Solution:

    def solve(self, A, B, C):

        @functools.cache
        def solve0(i, j, k):
            if i < 0 or j < 0 or k < 0:
                return 0

            if A[i] == B[j] == C[k]:
                return 1 + solve0(i-1, j-1, k-1)

            return max (
                solve0(i-1, j, k),
                solve0(i, j-1, k),
                solve0(i, j, k-1),
                solve0(i-1, j-1, k),
                solve0(i, j-1, k-1),
                solve0(i-1, j, k-1)
            )

        return solve0(len(A)-1, len(B)-1, len(C)-1)


def test_1():
    a = "epidemiologist"
    b = "refrigeration"
    c = "supercalifragilisticexpialodocious"
    expected = 5
    assert Solution().solve(a, b, c) == expected
