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
        for lf, mn in enumerate(nums):
            for rt, mx in enumerate(nums[lf:], start=lf):
                # Since the array is sorted, we know that nums[lf] is the
                # minimum in nums[lf:rt).  We also no that nums[rt] is
                # the maximum in nums[lf:rt).  So, how many subsequences
                # can we form?  We must leave in nums[lf] and nums[rt] to
                # maintain our invariants, but we can remove any of the
                # (rt-lf = n) elements in the middle.  This will be the sum
                # of nCk for k in the range [0:k], which is 2^n = s.  So
                # there are s differnt subsequences with a width of (mn - mx).
                n = max(0, rt - lf - 1)
                w = mx - mn
                s = pow(2, n, MOD)
                t = (w * s) % MOD
                print(f"{lf=} {mn=} {rt=} {mx=} {n=} {s=} {t=} {w=}")
                soln += t
                soln %= MOD
        return soln % MOD


def test_1():
    nums = [6, 3, 8]
    expected = 15
    assert Solution().solve(nums) == expected