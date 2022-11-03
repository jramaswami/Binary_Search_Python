"""
binarysearch.com :: Weekly Contest 35 :: Reverse Equivalent Pairs
"""
from collections import defaultdict


MOD = pow(10, 9) + 7
INV2 = pow(2, MOD-2, MOD)


def reverse_number(n):
    k = 0
    while n:
        k *= 10
        n, r = divmod(n, 10)
        k += r
    return k


class Solution:
    def solve(self, nums):
        frequencies = defaultdict(int)
        for n in nums:
            rev_n = reverse_number(n)
            frequencies[n - rev_n] += 1 
        soln = 0
        for _, v in frequencies.items():
            soln = (soln + (((v * (v + 1)) % MOD) * INV2) % MOD) % MOD
        return soln % MOD


def test_1():
    nums = [1, 20, 2, 11]
    solver = Solution()
    assert solver.solve(nums) == 7


def test_2():
    nums = [2, 2]
    solver = Solution()
    assert solver.solve(nums) == 3
