"""
binarysearch.com :: Characters in Each Bracket Depth
jramaswami
"""
class Solution:
    def solve(self, s):
        soln_stack = []
        depth = -1
        for c in s:
            if c == '(':
                depth += 1
                while len(soln_stack) <= depth:
                    soln_stack.append(0)
            elif c == ')':
                depth -= 1
            else:
                soln_stack[depth] += 1
        return soln_stack


def test_1():
    s = "(XX(XX(X))X)"
    assert Solution().solve(s) == [3, 2, 1]

def test_2():
    s = "(())"
    assert Solution().solve(s) == [0, 0]

def test_3():
    s = "(()())"
    assert Solution().solve(s) == [0, 0]
