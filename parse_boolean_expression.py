"""
binarysearch.com :: Parse Boolean Expression
jramaswami
"""


import collections


class Solution:

    def solve(self, s):
        # Use shunting-yard algorithm to convert to RPN.
        tokens = collections.deque(s.split())
        output_stack = []
        operator_stack = []
        while tokens:
            t = tokens.popleft()
            # Fix tokens.
            if len(t) > 1 and t[0] == '(':
                tokens.appendleft(t[1:])
                tokens.appendleft('(')
            elif len(t) > 1 and t[-1] == ')':
                tokens.appendleft(')')
                tokens.appendleft(t[:-1])
            # Operator
            elif (t == 'and' or t == 'or'):
                while operator_stack and operator_stack[-1] != '(':
                    output_stack.append(operator_stack.pop())
                operator_stack.append(t)
            # Value
            elif (t == 'false' or t == 'true'):
                output_stack.append(t)
            # (
            elif t == '(':
                operator_stack.append('(')
            elif t == ')':
                assert operator_stack
                while operator_stack[-1] != '(':
                    output_stack.append(operator_stack.pop())
                assert operator_stack and operator_stack[-1] == '('
                operator_stack.pop()
        while operator_stack:
            assert operator_stack[-1] != '('
            output_stack.append(operator_stack.pop())

        # Evaluate RPN
        rpn_stack = []
        for t in output_stack:
            if t == 'false':
                rpn_stack.append(False)
            elif t == 'true':
                rpn_stack.append(True)
            elif t == 'and':
                a = rpn_stack.pop()
                b = rpn_stack.pop()
                rpn_stack.append(a and b)
            elif t == 'or':
                a = rpn_stack.pop()
                b = rpn_stack.pop()
                rpn_stack.append(a or b)
        assert len(rpn_stack) == 1
        return rpn_stack[-1]


def test_1():
    s = "true and (false or true)"
    expected = True
    assert Solution().solve(s) == expected


def test_2():
    s = "(false or false)"
    expected = False
    assert Solution().solve(s) == expected