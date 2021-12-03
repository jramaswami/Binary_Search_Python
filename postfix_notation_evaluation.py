"""
binarysearch.com :: Postfix Notation Evaluation
jramaswami
"""


import operator


class Solution:

    def solve(self, exp):
        # Assumes exp contains valid expression.
        stack = []
        operators = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                # "Integer division" is not equivalent to Python's // operator.
                "/": lambda l, r: int(l / r)
        }
        for token in exp:
            if token in operators:
                right = stack.pop()
                left = stack.pop()
                result = operators[token](left, right)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[-1]


def test_1():
    exp = ["9", "3", "+", "2", "/"]
    expected = 6
    assert Solution().solve(exp) == expected


def test_2():
    exp = ["3", "9", "-", "4", "/"]
    expected = -1
    assert Solution().solve(exp) == expected
