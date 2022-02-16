"""
binarysearch.com :: Largest Equivalent Set of Pairs
jramaswami
"""


class Solution:

    def solve(self, nums):
        # double knapsack
        max_sum = sum(nums) // 2

        # dp[index][w1][w2]
        curr = set()
        prev = set()
        prev.add((nums[0], 0))
        prev.add((0, nums[0]))
        prev.add((0, 0))
        for i, n in enumerate(nums[1:], start=1):
            for w1, w2 in prev:
                # Can I add it to w1?
                if w1 + n <= max_sum:
                    curr.add((w1+n, w2))
                # Can I add it to w2?
                if w2 + n <= max_sum:
                    curr.add((w1, w2+n))
                # I can always chuck n!
                curr.add((w1, w2))
            prev, curr = curr, prev
        return max(w for w in range(max_sum+1) if (w, w) in prev)


def test_1():
    nums = [1, 4, 3, 5]
    expected = 5
    assert Solution().solve(nums) == expected


def test_2():
    nums = list(range(1, 31))
    expected = 232
    assert Solution().solve(nums) == expected


def test_3():
    "Would be TLE"
    nums = [21, 64, 99, 36, 45, 40, 34, 78, 57, 19, 85, 92, 54, 94, 41, 59, 25, 70, 61, 69, 67, 41, 25, 29, 63, 38, 80, 87, 91, 63]
    expected = 854
    assert Solution().solve(nums) == expected
