"""
binarysearch.com :: Roman Numeral to Integer
jramaswami
"""


class Solution:
    def solve(self, numeral):
        # First, eliminate 6 cases where lower precedes higher.
        cases = (
            ("CM", "CCCCCCCCC"), ("CD", "CCCC"),
            ("XC", "XXXXXXXXX"), ("XL", "XXXX"),
            ("IX", "IIIIIIIII"), ("IV", "IIII")
        )
        for a, b in cases:
            numeral = numeral.replace(a, b)

        values = {
            "I": 1, "V": 5, "X": 10, "L" : 50,
            "C": 100, "D": 500, "M": 1000
        }
        return sum(values[c] for c in numeral)


def test_1():
    assert Solution().solve("XII") == 12


def test_2():
    assert Solution().solve("XIV") == 14


def test_3():
    assert Solution().solve("IX") == 9


def test_4():
    assert Solution().solve("LVIII") == 58


def test_5():
    assert Solution().solve("MCMXCIV") == 1994
