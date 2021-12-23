"""
binarysearch.com :: Parentheses Grouping
jramaswami
"""


class Solution:

    def solve(self, S):
        level = 0
        left = 0
        soln = []
        for i, c in enumerate(S):
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if level == 0:
                soln.append(S[left:i+1])
                left = i+1
        return soln


def test_1():
    s = "()()(()())"
    expected = ["()", "()", "(()())"]
    assert Solution().solve(s) == expected


def test_2():
    s = ""
    expected = []
    assert Solution().solve(s) == expected
