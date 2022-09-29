"""
binarysearch.com :: Vertical Cipher
jramaswami
"""


class Solution:
    def solve(self, s, k):
        soln = [[] for _ in range(k)]
        for i, c in enumerate(s):
            soln[i % k].append(c)
        return ["".join(t) for t in soln]


def test_1():
    s = "abcdefghi"
    k = 5
    expected = ["af", "bg", "ch", "di", "e"]
    assert Solution().solve(s, k) == expected