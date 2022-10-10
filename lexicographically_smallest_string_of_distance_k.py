"""
binarysearch.com :: Lexicographically Smallest String of Distance K
jramaswami
"""


class Solution:

    def solve(self, n, k):
        soln = ['a' for _ in range(k)]
        dist = k
        i = k - 1
        while dist < n:
            if n - dist > 25:
                soln[i] = 'z'
                dist += 25
            else:
                soln[i] = chr(ord('a') + (n - dist))
                dist = n
            i -= 1
        return "".join(soln)


def test_1():
    n = 30
    k = 4
    expected = "aabz"
    assert Solution().solve(n, k) == expected