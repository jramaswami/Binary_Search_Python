"""
binarysearch.com :: Stack Sequence
jramaswami
"""


class Solution:

    def solve(self, pushes, pops):
        stack = []
        push_i = pop_i = 0
        while push_i < len(pushes) or pop_i < len(pops):
            while (not stack) or (stack[-1] != pops[pop_i]):
                if push_i >= len(pushes):
                    break
                stack.append(pushes[push_i])
                push_i += 1

            if stack[-1] != pops[pop_i]:
                return False

            stack.pop()
            pop_i += 1

        return not stack


def test_1():
    pushes = [0, 1, 4, 6, 8]
    pops = [1, 0, 8, 6, 4]
    assert Solution().solve(pushes, pops) == True


def test_2():
    pushes = [1, 2, 3, 4]
    pops = [4, 1, 2, 3]
    assert Solution().solve(pushes, pops) == False
