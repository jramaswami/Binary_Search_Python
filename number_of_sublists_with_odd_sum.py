"""
binarysearch.com :: Number of Sublists With Odd Sum
jramaswami
"""


class Solution:

    def solve(self, nums):
        MOD = pow(10, 9) + 7
        even_prefixes = 1   # empty list
        odd_prefixes = 0
        curr_sum = 0
        soln = 0
        for n in nums:
            curr_sum += n
            if curr_sum % 2:
                # Odd sum requires subtracting even sum prefix.
                soln = (soln + even_prefixes) % MOD
                odd_prefixes = (odd_prefixes + 1) % MOD
            else:
                # Even sum requires subtracting an odd sum prefix.
                soln = (soln + odd_prefixes) % MOD
                even_prefixes = (even_prefixes + 1) % MOD
        return soln % MOD


def test_1():
    nums = [2, 3, 1, 5]
    assert Solution().solve(nums) == 6