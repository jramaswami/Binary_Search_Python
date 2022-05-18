"""
binarysearch.com :: Substringify
jramaswami
"""


class Solution:

    def solve(self, S, T):

        def compute_changes(i):
            result = 0
            for s, t in zip(S[i:], T):
                if s != t:
                    result += 1
            return result

        soln = len(T)
        for i, _ in enumerate(S):
            if i + len(T) > len(S):
                break
            soln = min(soln, compute_changes(i))
        return soln


def test_1():
    s = "foobar"
    t = "oops"
    expected = 2
    assert Solution().solve(s, t) == expected


def test_2():
    "WA"
    s = "va"
    t = "a"
    expected = 0
    assert Solution().solve(s, t) == expected
