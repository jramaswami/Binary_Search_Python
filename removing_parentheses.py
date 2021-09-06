"""
binarysearch.com :: Removing Parentheses
jramaswami
"""

class Solution:

    def solve(self, S):
        curr = 0
        soln = 0
        for p in S:
            if p == '(':
                curr += 1
            elif p == ')':
                if curr == 0:
                    soln += 1
                else:
                    curr -= 1
        return soln + curr


def test_1():
    S = "()())()"
    assert Solution().solve(S) == 1


def test_2():
    S = ")("
    assert Solution().solve(S) == 2
