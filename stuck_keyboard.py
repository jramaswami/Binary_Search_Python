"""
binarysearch.com :: Stuck Keyboard
jramaswami
"""
class Solution:
    def solve(self, typed, target):
        stack = []
        for c in typed:
            if stack and stack[-1] == c:
                pass
            else:
                stack.append(c)
        return "".join(stack) == target


def test_1():
    typed = "aaabcccc"
    target = "abc"
    assert Solution().solve(typed, target) == True

def test_2():
    typed = "abc"
    target = "ab"
    assert Solution().solve(typed, target) == False

def test_3():
    typed = "bb"
    target = "bb"
    assert Solution().solve(typed, target) == True
