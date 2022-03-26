"""
binarysearch.com :: 24
jramaswami
"""


import operator
import itertools


class Solution:
    def solve(self, nums):
        ops = [operator.add, operator.sub, operator.mul, lambda a, b: int(a/b)]
        for nums0 in itertools.permutations(nums):

            for ops0 in itertools.permutations(ops, 3):
                stack = list(nums0)
                for op in reversed(ops0):
                    a = stack.pop()
                    b = stack.pop()
                    if a == 0:
                        break
                    c = op(b, a)
                    stack.append(c)
                if len(stack) == 1 and stack[-1] == 24:
                    return True
        return False


def test_1():
    nums = [5, 2, 7, 8]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [7, 9, 7, 4]
    expected = True
    assert Solution().solve(nums) == expected


def test_3():
    "WA"
    nums = nums = [4,8,6,0]
    expected = False
    assert Solution().solve(nums) == expected
