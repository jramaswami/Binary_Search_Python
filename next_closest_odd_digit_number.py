"""
binarysearch.com :: Next Closest Odd Digit Number
jramaswami
"""


class Solution:

    def solve(self, n):
        # Special case:
        if n == 0:
            return 1

        digits = list(int(i) for i in str(n))
        soln_a = [1 for _ in digits]
        soln_b = [9 for _ in digits]
        for i, d in enumerate(digits):
            if d % 2:
                soln_a[i] = d
                soln_b[i] = d
            else:
                soln_a[i] = d + 1
                soln_b[i] = d - 1
                break

        # Fix any negatives.
        for off, _ in enumerate(soln_b):
            i = len(soln_b) - off - 1
            if i == 0:
                if soln_b[i] < 0:
                    soln_b[i] = 0
            else:
                if soln_b[i] < 0:
                    soln_b[i-1] -= 2
                    soln_b[i] = 9

        soln_a = int("".join(str(d) for d in soln_a))
        soln_b = int("".join(str(d) for d in soln_b))
        delta_a = soln_a - n
        delta_b = n - soln_b
        if delta_b < delta_a:
            return soln_b
        return soln_a


def test_1():
    n = 130
    assert Solution().solve(n) == 131


def test_2():
    n = 110
    assert Solution().solve(n) == 111
