"""
binarysearch.com :: Connect Sticks
jramaswami


Problem statement not really clear!!!
"""


import collections


Stick = collections.namedtuple('Stick', ['left', 'right', 'length'])


class Solution:

    def solve(self, sticks):

        def match(a, b):
            return (
                a.left == b.left or
                a.left == b.right or
                a.right == b.left or
                a.right == b.right
            )

        def combine(a, b):
            if a.left == b.left:
                return Stick(a.right, b.right, a.length + 1)
            elif a.left == b.right:
                return Stick(a.left, b.left, a.length + 1)
            elif a.right == b.left:
                return Stick(a.right, b.left, a.length + 1)
            elif a.right == b.right:
                return Stick(a.right, b.right, a.length + 1)

        def solve0(a, sticks0):
            result = a.length
            for i, b in enumerate(sticks0):
                if match(a, b):
                    a0 = combine(a, b)
                    sticks0[i], sticks0[-1] = sticks0[-1], sticks0[i]
                    t = sticks0.pop()
                    result = max(result, solve0(a0, sticks0))
                    sticks0.append(t)
                    sticks0[i], sticks0[-1] = sticks0[-1], sticks0[i]
            return result

        sticks0 = [Stick(l, r, 1) for l, r in sticks]
        soln = 0
        for i, s in enumerate(sticks0):
            sticks0[i], sticks0[-1] = sticks0[-1], sticks0[i]
            a = sticks0.pop()
            soln = max(soln, solve0(a, sticks0))
            sticks0.append(a)
            sticks0[i], sticks0[-1] = sticks0[-1], sticks0[i]
        return soln


def test_1():
    sticks = [ [1, 2], [1, 3], [2, 4], [6, 6] ]
    expected = 3
    assert Solution().solve(sticks) == expected


def test_2():
    sticks = []
    expected = 0
    assert Solution().solve(sticks) == expected


def test_3():
    sticks = [ [1, 2] ]
    expected = 1
    assert Solution().solve(sticks) == expected


def test_4():
    "WA"
    sticks = [[2,1],[4,1],[6,4]]
    expected = 3
    assert Solution().solve(sticks) == expected