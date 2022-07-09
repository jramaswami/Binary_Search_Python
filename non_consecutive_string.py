"""
binarysearch.com :: Non-Consecutive String
jramaswami
"""


class Solution:

    def solve(self, n, k):
        if k >= 3 * pow(2, n-1):
            return ""

        soln = []
        x = pow(2, n-1)
        t = x
        P = 0
        for i in "012":
            if t > k:
                soln.append(i)
                P = t - x
                break
            t += x

        n -= 1
        x //= 2
        while n:
            t = x
            for i in "012":
                if i == soln[-1]:
                    continue
                if P + t > k:
                    soln.append(i)
                    P += (t - x)
                    break
                t += x
            n-= 1
            x //= 2

        return "".join(soln)


def test_1():
    n = 2
    k = 1
    expected = "02"
    assert Solution().solve(n, k) == expected


def test_2():
    n = 1
    k = 3
    expected = ""
    assert Solution().solve(n, k) == expected


def test_3():
    n = 13
    k = 1654
    expected = "0121012120210"
    assert Solution().solve(n, k) == expected
