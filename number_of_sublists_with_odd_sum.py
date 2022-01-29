"""
binarysearch.com :: Number of Sublists With Odd Sum
jramaswami
"""


class Solution:

    def solve(self, nums):
        MOD = pow(10, 9)

        # Even/odd sublists ending at given index.
        even_sublists = [0 for _ in nums]
        odd_sublists = [0 for _ in nums]

        soln = 0
        for i, n in enumerate(nums):
            # n can begin an entirely new sublist.
            if n % 2:
                odd_sublists[i] = 1
            else:
                even_sublists[i] = 1

            # n can attach to any previous sublist ending at i - 1.
            if i > 0:
                if n % 2:
                    odd_sublists[i] = (odd_sublists[i] + even_sublists[i-1]) % MOD
                    even_sublists[i] = (even_sublists[i] + odd_sublists[i-1]) % MOD
                else:
                    even_sublists[i] = (even_sublists[i] + even_sublists[i-1]) % MOD
                    odd_sublists[i] = (odd_sublists[i] + odd_sublists[i-1]) % MOD

            soln = (soln + odd_sublists[i]) % MOD

        return soln


def test_1():
    nums = [2, 3, 1, 5]
    assert Solution().solve(nums) == 6
