"""
binarysearch.com :: Removing Enclosed Parentheses
jramaswami
"""


class Solution:
    def solve(self, s):
        # First, find the matching parentheses
        stack = []
        match = [-1 for _ in s]
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                match[i] = stack[-1]
                match[stack[-1]] = i
                stack.pop()

        left = 0
        right = len(s) - 1
        while left < right and match[left] == right:
            left += 1
            right -= 1
        return s[left:right+1]



def test_1():
    s = "(((abc)))"
    assert Solution().solve(s) == "abc"


def test_2():
    s = "(((abc)))(d)"
    assert Solution().solve(s) == "(((abc)))(d)"


def test_3():
    s = "()"
    assert Solution().solve(s) == ""
