"""
binarysearch.com :: Subsequence Match Target
jramaswami
"""


class Solution:
    def solve(self, words, s):
        ptr = [0 for _ in words]

        for i, c in enumerate(s):
            for j, _ in enumerate(words):
                p = ptr[j]
                w = words[j]
                if p < len(w) and w[p] == c:
                    ptr[j] += 1

        return sum(p == len(w) for p, w in zip(ptr, words))




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
