"""
binarysearch.com :: String Multiplication
jramaswami
"""
from itertools import zip_longest
from functools import reduce
from operator import add


class Number:
    def __init__(self, n=None):
        self.negative = False
        self.digits = []
        if n is not None:
            if n[0] == '-':
                self.negative = True
                self.digits = list(reversed(n[1:]))
            else:
                self.digits = list(reversed(n))

    def __add__(self, other):
        """
        This is incomplete!  It does not handle negative numbers because the
        problem did not require it.
        """
        soln = []
        carry = 0
        for a, b in zip_longest(self.digits, other.digits, fillvalue='0'):
            ds = carry + int(a) + int(b)
            k = ds % 10
            carry = ds // 10
            soln.append(str(k))
        if carry > 0:
            soln.append(str(carry))
        result = Number()
        result.digits = soln
        return result

    def __mul__(self, other):
        addends = []
        for i, a in enumerate(self.digits):
            addend = []
            for _ in range(i):
                addend.append('0')
            carry = 0
            for b in other.digits:
                ds = carry + (int(a) * int(b))
                k = ds % 10
                carry = ds // 10
                addend.append(k)

            if carry > 0:
                addend.append(str(carry))

            n = Number()
            n.digits = addend
            addends.append(n)

        result = reduce(add, addends, Number('0'))
        if self.negative != other.negative:
            result.negative = True
        return result

    def __repr__(self):
        if self.negative:
            return "Number(-{})".format("".join(reversed(self.digits)))
        else:
            return "Number({})".format("".join(reversed(self.digits)))

    def __str__(self):
        if self.negative:
            return "-{}".format("".join(reversed(self.digits)))
        else:
            return "{}".format("".join(reversed(self.digits)))

    def __eq__(self, other):
        return self.negative == other.negative and self.digits == other.digits


class Solution:
    def solve(self, a, b):
        return str(Number(a) * Number(b))


def test_add():
    assert Number('2') + Number('3') == Number('5')
    assert Number('8') + Number('3') == Number('11')
    assert Number('110') + Number('907') == Number('1017')

def test_mul():
    assert Number('2') * Number('3') == Number('6')
    assert Number('8') * Number('3') == Number('24')
    assert Number('110') * Number('907') == Number('99770')
    assert Number('-2') * Number('3') == Number('-6')
    assert Number('8') * Number('-3') == Number('-24')
    assert Number('-8') * Number('-3') == Number('24')

def test_1():
    assert Solution().solve("5", "4") == "20"

def test_2():
    assert Solution().solve("2", "-3") == "-6"
