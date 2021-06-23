"""
binarysearch.com :: Longest Inequality Alternating Sublist
jramaswami
"""


class Solution:
    def solve(self, nums0):
        def sign(n):
            if n < 0:
                return -1
            elif n > 0:
                return 1
            else:
                return 0

        if nums0 == []:
            return 0

        # Remove zero signs
        nums = [nums0[0]]
        for n in nums0[1:]:
            if n != nums[-1]:
                nums.append(n)

        if len(nums) < 2:
            return len(nums)


        signs = [sign(a - b) for a, b in zip(nums[:-1], nums[1:])]
        print(signs)

        prev_sign = signs[0]
        curr_len = 2
        soln = 1
        if prev_sign != 0:
            soln = 2
        index = 1
        while index < len(signs):
            curr_sign = signs[index]
            if curr_sign == 0:
                if index + 1 < len(signs):
                    prev_sign = signs[index + 1]
                    curr_len = 1
                index += 2
            elif curr_sign != prev_sign:
                curr_len += 1
                soln = max(soln, curr_len)
                prev_sign = curr_sign
                index += 1
            else:
                curr_len = 2
                prev_sign = curr_sign
                index += 1
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
