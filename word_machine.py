"""
binarysearch.com :: Word Machine
jramaswami
"""


class Solution:

    def solve(self, ops):
        stack = []
        for op in ops:
            if op == 'POP':
                if not stack:
                    return -1
                stack.pop()
            elif op == 'DUP':
                if not stack:
                    return -1
                stack.append(stack[-1])
            elif op == '+':
                if len(stack) < 2:
                    return -1
                top = stack.pop()
                second = stack.pop()
                stack.append(top + second)
            elif op == '-':
                if len(stack) < 2:
                    return -1
                top = stack.pop()
                second = stack.pop()
                stack.append(top - second)
            else:
                try:
                    i = int(op)
                    stack.append(i)
                except:
                    return -1
        if not stack:
            return -1
        return stack[-1]


def test_1():
    ops = ["1", "5", "DUP", "3", "-"]
    expected = -2
    assert Solution().solve(ops) == expected