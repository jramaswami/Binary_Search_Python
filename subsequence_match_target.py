"""
binarysearch.com :: Subsequence Match Target
jramaswami
"""


import collections
import math


class Solution:
    def solve(self, words, s):
        alphabet = set(s)
        root = {c: math.inf for c in s}
        graph = [None for _ in range(len(s)+1)]

        for i in range(len(s)-1, -1, -1):
            graph[i+1] = root.copy()
            root[s[i]] = i+1
        graph[0] = root

        def is_subsequence(wd):
            if len(wd) > len(graph):
                return False

            curr = -1
            for i, c in enumerate(wd):
                curr = graph[i].get(c, math.inf)
                if curr == math.inf:
                    return False
            print(graph)
            print(wd, curr)
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


def test_3():
    "WA"
    words = ["cbb"]
    s = "cba"
    expected = 0
    assert Solution().solve(words, s) == expected


def test_4():
    "RTE"
    words = ["bba"]
    s = "bb"
    expected = 0
    assert Solution().solve(words, s) == expected


def test_5():
    "RTE"
    words = ["cab"]
    s = "aac"
    expected = 0
    assert Solution().solve(words, s) == expected


def test_6():
    "WA"
    words = ["b", "cc"]
    s = "bc"
    expected = 1
    assert Solution().solve(words, s) == expected

