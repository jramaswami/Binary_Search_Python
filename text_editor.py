"""
binarysearch.com :: Text Editor
jramaswami
"""


class Solution:
    def solve(self, s):
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '<' and i + 1 < len(s) and s[i+1] == "-":
                if stack:
                    stack.pop()
                i += 2
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)


def test_1():
    s = "abc<-z"
    assert Solution().solve(s) == "abz"


def test_2():
    s = "<-x<-z<-"
    assert Solution().solve(s) == ""


def test_3():
    """WA"""
    s = "<"
    assert Solution().solve(s) == "<"