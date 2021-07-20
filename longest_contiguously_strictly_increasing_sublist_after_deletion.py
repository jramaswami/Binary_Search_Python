"""
binarysearch.com :: Longest Contiguously Strictly Increasing Sublist After Deletion
jramaswami
"""


class Solution:
    def solve(self, nums):
        no_del_start = [0 for _ in nums]
        del_start = [0 for _ in nums]
        del_next = [-1 for _ in nums]

        soln = 0
        for i, _ in enumerate(nums[1:], start=1):
            if nums[i] <= nums[i-1]:
                # Non-increasing
                no_del_start[i] = i
                del_start[i] = del_next[i-1] + 1
                del_next[i] = i-1
            else:
                no_del_start[i] = no_del_start[i-1]
                del_start[i] = del_start[i-1]
                del_next[i] = del_next[i-1]
            soln = max(soln, (i - del_start[i]), (i - no_del_start[i] + 1))

        return soln


def test_1():
    nums = [30, 1, 2, 3, 4, 5, 8, 7, 22]
    expected = 7
    assert Solution().solve(nums) == expected


def test_2():
    nums = [8, 3, 10, 9, 3, 6, 10, 4, 6, 5]
    expected = 4
    assert Solution().solve(nums) == expected


def test_3():
    nums = list(range(1, 11))
    expected = 10
    assert Solution().solve(nums) == expected


def test_4():
    nums = [1, 2, 3, 4, 5, 11, 6, 7, 8, 9, 10]
    expected = 10
    assert Solution().solve(nums) == expected


def test_5():
    nums = [6, 5, 4, 3, 2, 1]
    expected = 1
    assert Solution().solve(nums) == expected


def test_6():
    nums = [6, 6, 6, 6, 6, 6]
    expected = 1
    assert Solution().solve(nums) == expected


def test_7():
    nums = [6, 6, 6, 6, 7, 6]
    expected = 2
    assert Solution().solve(nums) == expected


def test_8():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected


def test_9():
    """WA"""
    nums = [1]
    expected = 1
    assert Solution().solve(nums) == expected
