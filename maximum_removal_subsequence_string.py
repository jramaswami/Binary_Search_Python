"""
binarysearch.com :: Maximum Removal Subsequence String
jramaswami
"""


class Solution:
    def solve(self, S, T):
        prefix = [-1 for _ in T]
        j = 0
        for i, c in enumerate(S):
            if c == T[j]:
                prefix[j] = i
                j += 1
            if j >= len(T):
                break
        suffix = [-1 for _ in T]
        j = len(T) - 1
        for i in range(len(S)-1, -1, -1):
            c = S[i]
            if c == T[j]:
                suffix[j] = i
                j -= 1
            if j < 0:
                break

        soln = max(suffix[0], len(T) - prefix[-1])
        soln = max(soln, max(b - a for a, b in zip(prefix[:-1], suffix[1:])))
        return (soln - 1)


def test_1():
    s = "abcabac"
    t = "bc"
    assert Solution().solve(s, t) == 4


def test_2():
    s = "abcaaskjhdfaksjdfhaksdfagksdfgaksjfdgbac"
    t = "bcasdkjhakj"
    assert Solution().solve(s, t) == 13
