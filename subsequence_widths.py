"""
binarysearch.com :: Subsequence Widths
jramaswami
"""


class Solution:

    def solve(self, nums):
        MOD = pow(10, 9) + 7
        soln = 0
        # Sort the numbers.
        nums.sort()
        print(nums)
        N = len(nums)
        for i, n in enumerate(nums):
            # n will be the maximum for all subsequences [0:i).
            k = i
            s = pow(2, k, MOD)
            t = s * n
            soln += t
            soln %= MOD
            # n will be the minimum for all subsequences [i:N).
            k = N - i - 1
            s = pow(2, k, MOD)
            t = s * -n
            if t < 0:
                t += MOD
            soln += t
            soln %= MOD
        return soln





def test_1():
    nums = [6, 3, 8]
    expected = 15
    assert Solution().solve(nums) == expected