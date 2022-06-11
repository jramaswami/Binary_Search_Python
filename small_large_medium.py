"""
binarysearch.com :: Small Large Medium
jramaswami
"""


class Solution:

    def solve(self, nums):
        T = []
        for n in reversed(nums):
            if len(T) < 2:
                while T and T[-1] >= n:
                    T.pop()
                T.append(n)
            else:
                if T[0] < n < T[-1]:
                    return True
                if n > T[0]:
                    T.append(n)
        return False



def test_1():
    nums = [1, 10, 0, 3, 3]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 2, 3, 4, 5, 6]
    expected = False
    assert Solution().solve(nums) == expected


def test_3():
    nums = [6, 5, 4, 3, 2, 1]
    expected = False
    assert Solution().solve(nums) == expected


def test_5():
    nums = [1, 2, 3, 3, 3, 4, 5]
    expected = False
    assert Solution().solve(nums) == expected


def test_6():
    "WA"
    nums = [1, 2, 0]
    expected = False
    assert Solution().solve(nums) == expected
