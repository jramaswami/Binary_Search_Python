"""
binarysearch.com :: Longest Concatenated String
jramaswami
"""
from collections import defaultdict


class Solution:
    def solve(self, words):
        # +----> ends with
        # |
        # |      DP matrix
        # v
        # starts with
        dp = [[0 for _ in range(26)] for _ in range(26)]
        ord_a = ord('a')
        for wd in words:
            # This word can concatenate onto any words that ends with
            # the character it starts with.
            s_index = ord(wd[0]) - ord_a
            e_index = ord(wd[-1]) - ord_a
            for s in range(26):
                if dp[s][s_index]:
                    dp[s][e_index] = max(dp[s][e_index], dp[s][s_index] + len(wd))
            # This word can also be by itself.
            dp[s_index][e_index] = max(dp[s_index][e_index], len(wd))

        # To solve this we look where the string starts and ends with the
        # same character.
        soln = 0
        for i in range(26):
            soln = max(soln, dp[i][i])
        return soln


def test_1():
    words = ["hello", "olympic", "crunch"]
    assert Solution().solve(words) == 18

def test_2():
    words = ["bc"]
    assert Solution().solve(words) == 0

def test_3():
    words = ["d"]
    assert Solution().solve(words) == 1

def test_4():
    words = ["cd", "d"]
    assert Solution().solve(words) == 1

def test_5():
    words = ["d", "da"]
    assert Solution().solve(words) == 1

def test_6():
    words = ["ac", "bca", "c", "cbab"]
    assert Solution().solve(words) == 1
