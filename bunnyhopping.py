"""
binarysearch.com :: Bunnyhopping
jramaswami
"""


from math import inf


class Solution:

    def solve(self, nums, k):

        cache = [None for _ in nums]
        cache[0] = nums[0]
        has_cache = [False for _ in nums]
        has_cache[0] = True

        def solve0(i, k):
            """Recursive solution, using memoization."""
            if not has_cache[i]:
                t = inf
                for off in range(1, k+1):
                    j = i - off
                    if j < 0:
                        break
                    s = solve0(j, k)
                    t = min(t, nums[i] + s)
                cache[i] = t
                has_cache[i] = True
            return cache[i]

        soln = solve0(len(nums) - 1, k)
        return soln



def test_1():
    nums = [1, 2, 3, 4, 5]
    k = 2
    expected = 9
    assert Solution().solve(nums, k) == expected
