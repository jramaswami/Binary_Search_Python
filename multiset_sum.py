"""
binarysearch.com :: Multiset Sum
jramaswami
"""
class Solution:
    def solve(self, nums, k):
        def solve0(index, acc):
            """Recursive solution."""
            # Base case
            if index >= len(nums):
                if acc == k:
                    return 1
                return 0
            
            # You can use none of nums[index]
            without_me = solve0(index + 1, acc)
            # You can use as many num[index] until acc is greater than target.
            with_me = 0
            while acc + nums[index] <= k:
                acc += nums[index]
                with_me += solve0(index + 1, acc)

            return with_me + without_me

        return solve0(0, 0)


def test_1():
    nums = [1, 2, 3]
    k = 2
    assert Solution().solve(nums, k) == 2
