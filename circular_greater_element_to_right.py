"""
binarysearch.com :: Circular Greater Element to the Right
jramaswami
"""


class Solution:
    def solve(self, nums):
        nums0 = nums + nums
        soln = [None for _ in nums0]
        stack = []
        for i, n in enumerate(nums0):
            if i == 0:
                stack.append((n, i))
            else:
                while stack and stack[-1][0] < n:
                    m, j = stack.pop()
                    soln[j] = n
                stack.append((n, i))

        while stack:
            m, j = stack.pop()
            soln[j] = -1
        return soln[:len(nums)]


def test_1():
    nums = [3, 4, 0, 2]
    assert Solution().solve(nums) == [4, -1, 2, 3]


def test_2():
    nums = [2, 1, 0]
    assert Solution().solve(nums) == [-1, 2, 2]