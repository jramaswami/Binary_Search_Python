"""
binarysearch.com :: Longest Palindromic Substring
jramaswami
"""


import collections


class Solution:
    def solve(self, S):

        # Corner case: empty string.
        if S == "":
            return 0

        def is_palindrome(i, j):
            while i <= j:
                if S[i] != S[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Get index of each character.
        indexes = collections.defaultdict(list)
        for i, c in enumerate(S):
            indexes[c].append(i)

        # A single letter is a palindrome
        soln = 1
        for c in indexes:
            for i in range(len(indexes[c])):
                for j in range(len(indexes[c]) - 1, i, -1):
                    # Only look at indexes where it will yield a palindrome
                    # longer than the current solution.
                    L = 1 + indexes[c][j] - indexes[c][i]
                    if L <= soln:
                        break
                    if is_palindrome(indexes[c][i], indexes[c][j]):
                        soln = max(soln, L)
        return soln


def test_1():
    s = "mactacocatbook"
    expected = 7
    assert Solution().solve(s) == expected


def test_2():
    s = "a" * 1000
    expected = 1000
    assert Solution().solve(s) == expected
