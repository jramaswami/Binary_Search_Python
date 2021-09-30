"""
binarysearch.com :: K-Partitionable List
jramaswami
"""


from functools import lru_cache


class Solution:

    def solve(self, nums, k):
        # Corner case: if k is 1 the answer is always true.
        if k == 1:
            return True

        # Corner case: to divide nums into k parts there must be at least
        # k elements in nums.
        if len(nums) < k:
            return False

        # We are dividing the array in k *equal* parts so the sum of all the
        # parts must be divisible by k.
        target, remainder = divmod(sum(nums), k)
        if remainder > 0:
            return False

        # Corner case: target is zero.  Since we have already established
        # that we have enough elements, and that the sum is divisible by
        # the target, a zero target is a list of zeros.
        if target == 0:
            return True

        # First, get all the possible subsets (as bitmasks).
        possible_subsets = []
        for mask in range(1 << len(nums)):
            subset_sum = sum(n for i, n in enumerate(nums) if mask & (1 << i))
            if subset_sum == target:
                possible_subsets.append(mask)

        @lru_cache(maxsize=None)
        def solve0(available):
            """Recursive search for equal disjoint subsets."""

            # If we have used all numbers, we have a solution.
            if available == 0:
                return True

            for pmask in possible_subsets:
                if (pmask & available) == pmask:
                    # If all elements in pmask subset are available, recurse
                    # after removing the elements from available.
                    if solve0(available ^ pmask):
                        return True
            return False

        return solve0((1 << len(nums)) - 1)


def test_1():
    nums = [3, 1, 5, 4, 1, 5, 2]
    k = 3
    expected = True
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1,2,3,4]
    k = 3
    expected = False
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [4535, 1759, 3903, 1939, 9637, 9822, 254, 5237, 8474, 9188, 5095, 3277, 1191, 5012, 7605, 8457]
    k = 4
    expected = False
    assert Solution().solve(nums, k) == expected


def test_4():
    nums = [4535, 1759, 3903, 1939, 9637, 9822, 254, 5237, 8474, 9188, 5095, 3277, 1191, 5012, 7605, 8457]
    k = 2
    expected = False
    assert Solution().solve(nums, k) == expected


def test_5():
    """TLE"""
    nums = [98,102,9,36,57,44,30,35,28,9851,90,29,9751,44,66,9652]
    k = 8
    expected = False
    assert Solution().solve(nums, k) == expected


def test_6():
    """TLE"""
    nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908]
    k = 4
    expected = True
    assert Solution().solve(nums, k) == expected


def test_7():
    """WA"""
    nums = [2,2,2,2,3,4,5]
    k = 4
    expected = False
    assert Solution().solve(nums, k) == expected


def test_8():
    """RTE"""
    nums = [0, 0]
    k = 2
    expected = True
    assert Solution().solve(nums, k) == expected
