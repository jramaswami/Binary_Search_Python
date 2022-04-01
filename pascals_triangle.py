"""
binarysearch.com :: Pascal's Triangle
jramaswami
"""


class Solution:

    def solve(self, n):
        if n == 0:
            return [1]
        if n == 1:
            return [1, 1]

        prev = [1, 1]
        curr = [1, ]
        for _ in range(2, n+1):
            for i, _ in enumerate(prev):
                if i + 1 < len(prev):
                    curr.append(prev[i] + prev[i+1])
                else:
                    curr.append(prev[i])
            prev, curr = curr, [1,]
        return prev


def test_1():
    n = 3
    expected = [1, 3, 3, 1]
    assert Solution().solve(n) == expected


def test_2():
    n = 10
    expected = [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    assert Solution().solve(n) == expected


def test_3():
    assert Solution().solve(0) == [1]


def test_4():
    assert Solution().solve(1) == [1, 1]
