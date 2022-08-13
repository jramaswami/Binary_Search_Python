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
        sign = ""
        if numerator < 0 and denominator > 0:
            sign = "-"
        elif numerator > 0 and denominator < 0:
            sign = "-"
        numerator, denominator = abs(numerator), abs(denominator)
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
        d = len(str(numerator // denominator))
        return (
            sign + "".join(soln[0:d]) +
            "." + "".join(soln[d:j+1]) +
            "(" + "".join(soln[j+1:]) + ")"
        )


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


def test_5():
    numerator = 10
    denominator = 3
    expected = "3.(3)"
    assert Solution().solve(numerator, denominator) == expected

def test_6():
    "WA"
    numerator = 768
    denominator = 150
    expected = "5.12"
    assert Solution().solve(numerator, denominator) == expected
