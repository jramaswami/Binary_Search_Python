"""
binarysearch.com :: Kth Smallest Element
jramaswami
"""


import random


class Solution:
    def solve(self, nums0, k):
        # Do not mutate original list.
        nums = list(nums0)

        # Shuffle nums to reduce probability of O(n^2).
        random.shuffle(nums)

        def lomuto_partition(lo, hi):
            gte = lo - 1
            for i in range(lo, hi):
                if nums[i] < nums[hi]:
                    gte += 1
                    nums[gte], nums[i] = nums[i], nums[gte]
            nums[gte + 1], nums[hi] = nums[hi], nums[gte + 1]

            return gte + 1

        # Quickselect
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            p = lomuto_partition(lo, hi)
            if p == k:
                return nums[k]
            elif p < k:
                lo = p + 1
            elif p > k:
                hi = p - 1
        return -1


def test_1():
    nums = [5, 3, 8, 2, 0]
    k = 2
    assert Solution().solve(nums, k) == 3


def test_2():
    nums= [-293, 771, 268, 703, 478, 134, 476, -355, 99, -402]
    k=8
    result = Solution().solve(nums, k)
    assert result == sorted(nums)[k]


def test_3():
    nums = [-402, 134, -355, 478, 476, 99, 703, -293, 268, 771]
    k=8
    result = Solution().solve(nums, k)
    assert result == sorted(nums)[k]


def test_4():
    nums=[396, 192, 149, 607, 304, -293, -784, -231, -756, 71]
    k=8
    result = Solution().solve(nums, k)
    assert result == sorted(nums)[k]


def test_random():
    T = 10
    M = 1000
    N = 1000
    for _ in range(T):
        nums = [random.randint(-M, M) for _ in range(N)]
        k = random.randint(0, N-1)
        print(f"{nums=} {k=}")
        result = Solution().solve(nums, k)
        assert result == sorted(nums)[k]


if __name__ == '__main__':
    main()
