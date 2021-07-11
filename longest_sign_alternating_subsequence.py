"""
binarysearch.com :: Longest Sign Alternating Subsequence
jramaswami
"""


class Solution():
    def solve(self, nums):
        pos_len = 0
        neg_len = 0
        for n in nums:
            if n < 0:
                # I can add this to the positive length.  It will now end in negative.
                neg_len = max(neg_len, pos_len + 1)
            else:
                # I can add this to a negative length.  It will now end in a positive.
                pos_len = max(pos_len, neg_len + 1)
        return max(neg_len, pos_len)


def test_1():
    nums = [1, 2, -5, 3, -2]
    expected = 4
    assert Solution().solve(nums) == expected


def test_2():
    nums = [-1, -2, 5, -3, 2]
    expected = 4
    assert Solution().solve(nums) == expected


def test_3():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected
