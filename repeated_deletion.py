"""
binarysearch.com :: Repeated Deletion
jramaswami
"""
class Solution:
    def solve(self, s):
        stack = []
        should_delete = False
        i = 0
        while i < len(s):
            c = s[i]
            if stack:
                if stack[-1] != c and should_delete:
                    should_delete = False
                    stack.pop()
                elif stack[-1] == c:
                    should_delete = True
                    i += 1
                else:
                    stack.append(c)
                    i += 1
            else:
                stack.append(c)
                i += 1
        if should_delete:
            stack.pop()

        return "".join(stack)


def test_1():
    s = "abbbaac"
    assert Solution().solve(s) == "c"

def test_2():
    s = "aabbac"
    assert Solution().solve(s) == "ac"

def test_3():
    s = "abbccaacddc"
    assert Solution().solve(s) == ""

