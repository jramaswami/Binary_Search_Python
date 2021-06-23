"""
binarysearch.com :: Longest Inequality Alternating Sublist
jramaswami
"""


class Solution:
    def solve(self, nums):

        def get_sign(n):
            if n < 0:
                return -1
            if n > 0:
                return 1
            return 0

        # Corner case
        if len(nums) < 2:
            return len(nums)

        soln = 0
        start = 0
        index = 1
        prev_sign = 0
        while index < len(nums):
            # Get sign of nums[index] - nums[index - 1]
            curr_sign = get_sign(nums[index] - nums[index - 1])
            if curr_sign == 0:
                # If nums[index] equals num[index-1], we must move the start
                # to the current index.
                start = index
                # nums[start:index+1] is an alternating inequality sublist
                # (of length 1)
                soln = max(soln, index + 1 - start)
            elif prev_sign == 0:
                # If the previous sign was 0, then nums[start:index+1] is an
                # alternating inequality sublist
                soln = max(soln, index + 1 - start)
            elif prev_sign != curr_sign:
                # If the signs are opposite then nums[start:index+1] is an
                # alternating inequality sublist
                soln = max(soln, index + 1 - start)
            else:
                # The signs match.  Move the start to the previous element.
                start = index - 1
                # nums[start:index+1] is an alternating inequality sublist
                # (of length 2)
                soln = max(soln, index + 1 - start)

            # Move the index
            index += 1
            # Remember sign
            prev_sign = curr_sign

        return soln



def test_1():
    nums = [0, 1, 5, 3, 4]
    assert Solution().solve(nums) == 4


def test_2():
    nums = [0, 0, 0, 0, 0]
    assert Solution().solve(nums) == 1


def test_3():
    nums = []
    assert Solution().solve(nums) == 0


def test_4():
    """WA"""
    nums = [0]
    assert Solution().solve(nums) == 1


def test_5():
    nums = [5, 7]
    assert Solution().solve(nums) == 2


def test_6():
    nums = [7, 5]
    assert Solution().solve(nums) == 2


def test_7():
    nums = [7, 7]
    assert Solution().solve(nums) == 1


def test_8():
    """WA"""
    nums = [2, 2, 0]
    assert Solution().solve(nums) == 2


def test_9():
    nums = [73, 14, 97, 38, 37, 46, 24, 75, 62, 33, 45, 66, 71, 59, 27, 53, 52, 65, 49, 89]
    assert Solution().solve(nums) == 7


def test_10():
    nums = [92, 21, 82, 75, 50, 30, 2, 11, 23, 11, 23, 79, 99, 26, 97, 63, 93, 93, 90, 11, 46, 67, 17, 17, 17, 3, 54, 31, 83, 47, 72, 45, 21, 87, 43, 63, 37, 16, 64, 41, 68, 30, 93, 8, 56, 6, 64, 86, 62, 74, 16, 42, 97, 97, 50, 82, 43, 97, 36, 88, 36, 68, 78, 68, 13, 47, 47, 17, 35, 81, 68, 60, 45, 12, 2, 100, 30, 13, 28, 86, 72, 49, 95, 52, 68, 21, 58, 82, 98, 27, 15, 84, 6, 4, 49, 13, 54, 80, 10, 27, 23, 66, 81, 10, 85, 86, 17, 66, 13, 38, 86, 62, 97, 97, 26, 5, 3, 33, 87, 82, 49, 52, 17, 11, 57, 83, 75, 13, 92, 98, 82, 61, 4, 13, 19, 30, 68, 36, 97, 7, 68, 60, 54, 3, 58, 34, 98, 73, 16, 85, 74, 40, 8, 62, 85, 78, 30, 61, 66, 51, 39, 20, 15, 9, 54, 21, 19, 78, 63, 93, 19, 20, 78, 84, 14, 42, 55, 60, 70, 49, 23, 5, 82, 97, 76, 6, 7, 3, 25, 15, 25, 12, 97, 58, 99, 22, 100, 13, 77, 15]
    assert Solution().solve(nums) == 16
