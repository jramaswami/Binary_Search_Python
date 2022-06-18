"""
binarysearch.com :: Kth Pair Distance
jramaswami
"""


class Solution:

    def solve(self, nums, k):
        nums.sort()

        def find_possible(smallest=True):
            # print(f"find_possible({smallest=})")
            lo = min(b - a for a, b in zip(nums[:-1], nums[1:]))
            hi = nums[-1] - nums[0]
            result = lo
            if smallest:
                result = hi

            while lo <= hi:
                # Guess a number, x.
                x = lo + ((hi - lo) // 2)
                # How many pair diffs are less than x.
                lt = 0
                # How many pair diffs are less than or equal to x.
                lte = 0

                lt_i = 0
                lte_i = 0
                for i, _ in enumerate(nums):
                    # m - n < x
                    # m < x + n
                    while lt_i < len(nums) and nums[lt_i] - nums[i] < x:
                        lt_i += 1
                    while lte_i < len(nums) and  nums[lte_i] - nums[i] <= x:
                        lte_i += 1

                    # le_i now points to the first j such that nums[i] + any nums[i+1:j] < x
                    # lte_i now points to the first j such that nums[i] + any nums[i+1:j] <= x
                    lt += lt_i - i - 1
                    lte += lte_i - i - 1

                # If lt <= k < lte then our guess, x, produces the right
                # number of pairs sums to that x is the k-th pair sum.
                if lt <= k < lte:
                    if smallest:
                        hi = x - 1
                        result = min(result, x)
                    else:
                        lo = x + 1
                        result = max(result, x)
                # If k < lt, there are too many pairs sums that are less than
                # k for our given guess.  We need a smaller guess to reduce the
                # the number of pair sums less than x. Otherwise, increase the
                # guess.
                elif k < lt:
                    hi = x - 1
                else:
                    lo = x + 1
            return result

        def difference_exists(x):
            lt_i = 0
            for i, _ in enumerate(nums):
                # m - n < x
                # m < x + n
                while lt_i < len(nums) and nums[lt_i] - nums[i] < x:
                    lt_i += 1
                # le_i now points to the first j such that nums[i] + any nums[i+1:j] < x
                # lte_i now points to the first j such that nums[i] + any nums[i+1:j] <= x
                if lt_i < len(nums) and nums[lt_i] - nums[i] == x:
                    return True
            return False

        smallest_possible = find_possible(smallest=True)
        largest_possible = find_possible(smallest=False)
        for d in range(smallest_possible, largest_possible+1):
            if difference_exists(d):
                return d


def test_1():
    nums = [1, 5, 3, 2]
    k = 3
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 3, 1]
    k = 1
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [1, 1, 1]
    k = 2
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_4():
    nums = [1, 6, 1]
    k = 2
    expected = 5
    assert Solution().solve(nums, k) == expected


def test_5():
    "WA"
    nums = [0, 1]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected


def test_6():
    "WA"
    nums = [1, 1, 2]
    k = 1
    expected = 1
    assert Solution().solve(nums, k) == expected
