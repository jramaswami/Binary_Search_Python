"""
binarysearch.com :: Equivalent Product Pairs
jramaswami

Choose any two pairs of numbers that multiply to X.
There are eight ways to arrange each of those pairs to product(a * b == c * d).
nC2 = 1 + 2 + ... + n-1 = (n-1)(n-1+1) / 2 = n(n-1) / 2
"""

from collections import defaultdict

class Solution:

    def solve(self, nums):
        products = defaultdict(int)
        for i, a in enumerate(nums):
            for b in nums[i+1:]:
                products[a*b] += 1

        soln = 0
        for prod, freq in products.items():
            if freq >= 2:
                nC2 = ((freq - 1) * (freq)) // 2
                soln += 8 * nC2
        return soln


def test_1():
    nums = [2,3,4,6]
    assert Solution().solve(nums) == 8
