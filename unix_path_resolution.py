"""
binarysearch.com :: Unix Path Resolution
jramaswami
"""


class Solution:
    def solve(self, path):
        stack = []
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                pass
            else:
                stack.append(p)

        return stack


def test_1():
    path = ["usr", "..", "usr", ".", "local", "bin", "docker"]
    expected = ["usr", "local", "bin", "docker"]
    assert Solution().solve(path) == expected


def test_2():
    path = ["bin", "..", ".."]
    expected = []
    assert Solution().solve(path) == expected
