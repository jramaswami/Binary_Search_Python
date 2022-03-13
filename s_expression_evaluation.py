"""
binarysearch.com :: S-Expression Evaluation
jramaswami
"""


import operator


class Solution:

    def solve(self, expr):
        # S-Expression is a prefix expression.  Evaluate in reverse.
        operators = '+-*/'
        operations = [operator.add, operator.sub, operator.mul, lambda a, b: int(a/b)]
        stack = []
        trans = expr.maketrans("", "", '()')
        expr0 = expr.translate(trans)
        for token in reversed(expr0.split()):
            if token in operators:
                a = stack.pop()
                b = stack.pop()
                f = operations[operators.find(token)]
                stack.append(f(a, b))
            else:
                stack.append(int(token))
        return stack[-1]


def test_1():
    s = "(- (+ 2 1) 4)"
    expected = -1
    assert Solution().solve(s) == expected


def test_2():
    s = "(/ -4 3)"
    expected = -1
    assert Solution().solve(s) == expected
