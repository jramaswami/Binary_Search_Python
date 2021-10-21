"""
binarysearch.com :: Split String Into Palindromes
jramaswami
"""


import functools


import sys
sys.setrecursionlimit(pow(10, 9))


class Solution:

    def solve(self, S):

        # Corner case.
        if not S:
            return True

        @functools.lru_cache(maxsize=None)
        def is_palindrome(i, j):
            """Return True if S[i:j+1] is a palindrome."""
            if i >= j:
                return True
            return S[i] == S[j] and is_palindrome(i + 1, j - 1)

        @functools.lru_cache(maxsize=None)
        def minimum_cuts(i, j):
            # If S[i:j+1] is a palindrome you do not have to cut it.
            if is_palindrome(i, j):
                return 0
            # If not, then you have to cut it at least once.  Pick an
            # arbitrary cut and get the minimum cuts for each side.
            # i k    j
            # xxx|xxxx
            return min(1 + minimum_cuts(i, k) + minimum_cuts(k+1, j) for k in range(i, j))

        return minimum_cuts(0, len(S) - 1) + 1


def test_1():
    S = "amanaplanacanalpanama"
    expected = 1
    assert Solution().solve(S) == expected


def test_2():
    S = "racecarannakayak"
    expected = 3
    assert Solution().solve(S) == expected


def test_3():
    S = "abc"
    expected = 3
    assert Solution().solve(S) == expected


def test_4():
    S = "atabatab"
    expected = 2
    assert Solution().solve(S) == expected


def test_5():
    S = "a" * 1000
    expected = 1
    assert Solution().solve(S) == expected


def test_6():
    S = "abcde" * 200
    expected = 1000
    assert Solution().solve(S) == expected


def test_7():
    """TLE"""
    S = "xonigqkwqxbnewtzwkunfirmvxdweungwglcwnrcwfsnugqpnjrnxwcqnowcrxgfcpfyyuugbmydmtxnvqjapjaplnfkrjzcmllineilttqrqprvpeostndxcdhtafonwzistyduwpuiappjm"
    expected = 136
    assert Solution().solve(S) == expected
