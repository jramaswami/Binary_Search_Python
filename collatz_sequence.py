"""
binarysearch.com :: Collatz Sequence
jramaswami
"""


class Solution:
    def solve(self, n):
        soln = 1
        while n != 1:
            soln += 1
            if n % 2:
                n = 3 * n + 1
            else:
                n = n // 2
        return soln
