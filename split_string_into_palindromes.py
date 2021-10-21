"""
binarysearch.com :: Split String Into Palindromes
jramaswami
"""

import sys
sys.setrecursionlimit(pow(10, 9))


class Solution:

    def solve(self, S):

        def is_palindrome(i, j):
            """Return True if S[i:j+1] is a palindrome."""
            while i < j:
                if S[i] != S[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Corner case.
        if not S:
            return True


        # The most cuts possible for any S is 999 since this is how many
        # cuts to divide into 1000 separate palindromes.
        cache = [[1000 for _ in S] for _ in S]
        has_cache = [[False for _ in S] for _ in S]

        def minimum_cuts(i, j):
            if i > j:
                return 0

            if has_cache[i][j]:
                return cache[i][j]

            if i == j:
                cache[i][j] = 0
                return 0

            if is_palindrome(i, j):
                cache[i][j] = 0
                return 0

            for k in range(i, j):
                # Avoid overhead of recursive call if possible.
                if has_cache[i][k]:
                    left_min = cache[i][k]
                else:
                    left_min = minimum_cuts(i, k)
                if has_cache[k+1][j]:
                    right_min = cache[k+1][j]
                else:
                    right_min = minimum_cuts(k+1, j)
                cache[i][j] = min(cache[i][j], left_min + 1 + right_min)

            has_cache[i][j] = True
            return cache[i][j]


        return minimum_cuts(0, len(S)-1) + 1


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
