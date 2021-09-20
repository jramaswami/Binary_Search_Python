"""
binarysearch.com :: Set Bits
jramaswami
"""


class Solution:
    def solve(self, n):
        total_bits_set = 0
        for bit in range(32):
            period = pow(2, bit + 1)
            bits_set_per_period = period // 2
            periods_covered, remainder = divmod(n + 1, period)
            bits_set_this_period = ((periods_covered * bits_set_per_period) +
                                     max(0, remainder - bits_set_per_period))
            total_bits_set += bits_set_this_period
            if periods_covered == 0:
                break
        return total_bits_set


def bits(n):
    result = 0
    while n:
        if n & 1:
            result += 1
        n = n >> 1
    return result


def brute_force(n):
    return sum(bits(k) for k in range(n+1))


def test_1():
    assert Solution().solve(5) == 7


def test_2():
    assert Solution().solve(53) == 147


def test_random():
    import random
    for _ in range(1000):
        n = random.randint(0, pow(2, 10))
        assert brute_force(n) == Solution().solve(n)
