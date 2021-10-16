"""
binarysearch.com :: Zipped String
jramaswami
"""

import sys
sys.setrecursionlimit(pow(10, 9))


class Solution:

    def solve(self, A, B, C):

        def solve0(i, j, k):
            # Base case.
            if k >= len(C):
                return True

            result = False
            if i < len(A) and A[i] == C[k]:
                result = result or solve0(i + 1, j, k + 1)
            if j < len(B) and B[j] == C[k]:
                result = result or solve0(i, j + 1, k + 1)
            return result


        if len(A) + len(B) != len(C):
            return False

        return solve0(0, 0, 0)


def test_1():
    a = "abc"
    b = "def"
    c = "abdefc"
    expected = True
    assert Solution().solve(a, b, c) == expected


def test_2():
    a = "ab"
    b = "cd"
    c = "abdc"
    expected = False
    assert Solution().solve(a, b, c) == expected


def test_3():
    a = "a" * 500
    b = "a" * 500
    c = "a" * 1000
    expected = True
    assert Solution().solve(a, b, c) == expected


def test_4():
    a = "a" * 5
    b = "a" * 5
    c = "a" * 5
    expected = False
    assert Solution().solve(a, b, c) == expected
