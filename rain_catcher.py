"""
binarysearch.com :: Rain Catcher
jramaswami
"""
class Solution:
    def solve(self, nums):
        prefix = list(nums)
        suffix = list(nums)
        curr_max = 0
        for i, v in enumerate(nums):
            curr_max = max(curr_max, v)
            prefix[i] = curr_max

        curr_max = 0
        for negi, v in enumerate(reversed(nums), start=1):
            i = len(nums) - negi
            curr_max = max(curr_max, v)
            suffix[i] = curr_max

        soln = 0
        for i, v in enumerate(nums):
            if i - 1 < 0:
                left = v
            else:
                left = prefix[i-1]
            if i + 1 >= len(nums):
                right = v
            else:
                right = suffix[i+1]

            if min(left, right) > v:
                soln += min(left, right) - v

        return soln


def test_1():
    nums = [2, 5, 2, 0, 5, 8, 8]
    assert Solution().solve(nums) == 8


def test_2():
    nums = [2, 1, 2]
    assert Solution().solve(nums) == 1


def test_3():
    nums = [3, 0, 1, 3, 0, 5]
    assert Solution().solve(nums) == 8
