"""
binarysearch.com :: Majority Vote
jramaswami
"""

class Solution:

    def solve(self, nums):

        majority_winner = nums[0]
        count = 1
        for n in nums[1:]:
            if n == majority_winner:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority_winner = n
                count = 1

        majority_votes = sum(1 if n == majority_winner else 0 for n in nums)
        if majority_votes > len(nums) // 2:
            return majority_winner
        return -1


def test_1():
    nums = [5, 5, 1, 1, 2, 2, 2, 2, 2]
    expected = 2
    assert Solution().solve(nums) == expected


def test_2():
    nums = [3, 3, 4, 4]
    expected = -1
    assert Solution().solve(nums) == expected
