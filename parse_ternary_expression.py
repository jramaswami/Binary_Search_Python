"""
binarysearch.com :: Parse Ternary Expression
jramaswami
"""


class Solution:

    def solve(self, expr):
        tokens = [t.strip() for t in expr.split()]
        stack = []
        for t in reversed(tokens):
            if stack and stack[-1] == '?':
                stack.pop() # Pop ?
                lhs = stack[-1]
                stack.pop() # Pop lhs
                stack.pop() # Pop :
                rhs = stack[-1]
                stack.pop() # Pop rhs
                if t == 'true':
                    stack.append(lhs)
                else:
                    stack.append(rhs)
            else:
                stack.append(t)
        assert len(stack) == 1
        return True if stack[-1] == 'true' else False


def test_1():
    s = "true ? true : false"
    expected = True
    assert Solution().solve(s) == expected


def test_2():
    s = "true ? true ? false : true : true"
    expected = False
    assert Solution().solve(s) == expected


def test_3():
    "RTE"
    s = "true ? true ? true : true : true ? true : true"
    expected = True
    assert Solution().solve(s) == expected
