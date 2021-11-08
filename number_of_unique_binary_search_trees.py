"""
binarysearch.com :: Number of Unique Binary Search Trees
jramaswami

The number of Unique BST's is the Catalan number:

C(n) = (2n choose n) / (n + 1) = (2n)! / [(n+1)! * n!]
"""


MOD = pow(10, 9) + 7
MAXN = 1000


def mod_inverse(k):
    """Modular inverse using Euler's Theorem."""
    return pow(k, MOD-2, MOD)


class Solution:
    def __init__(self):
        self.factorials = [1, 1]
        for k in range(2, (2 * MAXN) + 1):
            self.factorials.append((self.factorials[-1] * k) % MOD)

    def solve(self, n):
        numerator = self.factorials[2 * n]
        denominator = (self.factorials[n + 1] * self.factorials[n]) % MOD
        return (numerator * mod_inverse(denominator)) % MOD


def test_1():
    assert Solution().solve(3) == 5
