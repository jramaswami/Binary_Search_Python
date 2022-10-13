"""
binarysearch.com :: Integer to Roman Numeral
jramaswami
"""


class Solution:
    def solve(self, n):
        numbers = [1,   4,    5,   9,   10,  40,   50,  90,   100, 400,  500, 900,  1000]
        romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        soln = []
        while num > 0:
            if num >= numbers[-1]:
                num -= numbers[-1]
                soln.append(romans[-1])
            else:
                numbers.pop()
                romans.pop()
        return "".join(soln)