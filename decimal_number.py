"""
binarysearch.com :: Decimal Number
jramaswami
"""


class Solution:

    def solve(self, numerator, denominator):
        remainders = dict()
        soln = []
        i = 0
        j = 0
        while 1:
            t, r = divmod(numerator, denominator)
            numerator -= (t * denominator)
            numerator *= 10
            soln.append(str(t))
            print(f"{t=} {r=} {numerator=}")
            if r in remainders:
                j = remainders[r]
                break
            remainders[r] = i
            i += 1
        return "".join(soln[0:j+1]) + ".(" + "".join(soln[j+1:]) + ")"


def test_1():
    numerator = 1
    denominator = 3
    expected = "0.(3)"
    assert Solution().solve(numerator, denominator) == expected


def test_2():
    numerator = 1
    denominator = 7
    expected = "0.(142857)"
    assert Solution().solve(numerator, denominator) == expected


def test_3():
    numerator = 1
    denominator = 11
    expected = "0.(09)"
    assert Solution().solve(numerator, denominator) == expected


def test_4():
    numerator = -279
    denominator = 390
    expected = "-0.7(153846)"
    assert Solution().solve(numerator, denominator) == expected
