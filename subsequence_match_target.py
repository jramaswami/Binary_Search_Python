"""
binarysearch.com :: Subsequence Match Target
jramaswami
"""


import collections
import math


class Solution:
    def solve(self, words, s):
        alphabet = set(s)
        graph = [collections.defaultdict(lambda: math.inf) for _ in s]
        for i in range(len(s)-1, -1, -1):
            graph[i][s[i]] = i
            if i < len(s) - 1:
                for c in alphabet:
                    graph[i][c] = min(graph[i][c], graph[i+1][c])

        def is_subsequence(wd):
            curr = graph[0][wd[0]]
            for c in wd[1:]:
                curr = graph[curr][c]
                if curr == math.inf:
                    return False
            return True

        return sum(is_subsequence(wd) for wd in words)


def test_1():
    words = ["ac", "ad", "b"]
    s = "abc"
    expected = 2
    assert Solution().solve(words, s) == expected



def test_2():
    "WA"
    words = ["c"]
    s = "abb"
    expected = 0
    assert Solution().solve(words, s) == expected

