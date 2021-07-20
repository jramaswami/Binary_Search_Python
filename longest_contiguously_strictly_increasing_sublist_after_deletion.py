"""
binarysearch.com :: Longest Contiguously Strictly Increasing Sublist After Deletion
jramaswami
"""


class Solution:
    def solve(self, nums):

        # Base case if there are 0 or 1 items in the array.
        if len(nums) < 2:
            return len(nums)

        longest_l2r = [1 for _ in nums]
        longest_r2l = [1 for _ in nums]

        # Find the longest increasing sequence that ends at each index, going
        # from left to right.  O(N)
        soln = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                longest_l2r[i] = longest_l2r[i-1] + 1
            soln = max(soln, longest_l2r[i])

        # Find the longest increasing sequence that ends at the index but go
        # from right to left for each index.  O(N)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                longest_r2l[i] = longest_r2l[i+1] + 1
            soln = max(soln, longest_r2l[i])

        # Find the longest sequence you can put together if you skip the
        # element at index i.  Note that nums[i-1] must be less than nums[i]
        # to join the left and right sequences. O(N)
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i+1]:
                left = longest_l2r[i-1]
                right = longest_r2l[i+1]
                soln = max(soln, left + right)

        # Overall 3*O(N) = O(N)
        return soln


def test_1():
    nums = [30, 1, 2, 3, 4, 5, 8, 7, 22]
    expected = 7
    assert Solution().solve(nums) == expected


def test_2():
    nums = [8, 3, 10, 9, 3, 6, 10, 4, 6, 5]
    expected = 3
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


def test_10():
    """WA"""
    nums = [1, 2, 0, 1]
    expected = 2
    assert Solution().solve(nums) == expected
