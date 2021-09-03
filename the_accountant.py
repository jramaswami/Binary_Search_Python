"""
binarysearch.com :: The Accountant
jramaswami

REF: https://www.geeksforgeeks.org/find-excel-column-name-given-number/
"""


class Solution:

    def solve(self, n):
        ord_A = ord('A')
        soln = []
        while n:
            r = n % 26
            if r == 0:
                soln.append('Z')
                n = (n // 26) - 1
            else:
                c = chr((r - 1) + ord_A)
                soln.append(c)
                n = n // 26
        return "".join(reversed(soln))


def test_1():
    assert Solution().solve(1) == 'A'


def test_2():
    assert Solution().solve(2) == 'B'


def test_3():
    assert Solution().solve(26) == 'Z'


def test_4():
    assert Solution().solve(27) == 'AA'
