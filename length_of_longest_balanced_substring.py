"""
binarysearch.com :: Length of Longest Balanced Subsequence
jramaswami
"""


class Solution:

    def solve(self, s):
        stack = []
        soln = len(s)
        for t in s:
            if t == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    soln -= 1
        soln -= len(stack)

        return soln


def test_1():
    s = "())(()"
    expected = 4
    assert Solution().solve(s) == expected


def test_2():
    s = "))(("
    expected = 0
    assert Solution().solve(s) == expected


def test_3():
    s = "))()))()"
    expected = 4
    assert Solution().solve(s) == expected


def test_4():
    s = s = "((((())"
    expected = 4
    assert Solution().solve(s) == expected