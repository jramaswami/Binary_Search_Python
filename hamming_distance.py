"""
binarysearch.com :: Hamming Distance
jramaswami
"""
class Solution:
    def solve(self, x, y):
        def popcount(n):
            bits = 0
            while n:
                if n & 1:
                    bits += 1
                n = n >> 1
            return bits
        return popcount(x ^ y)


def test_1():
    assert Solution().solve(9, 5) == 2
