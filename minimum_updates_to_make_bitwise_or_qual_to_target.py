"""
binarysearch.com :: Minimum Updates to Make Bitwise OR Equal to Target
jramaswami
"""


class Solution:
    def solve(self, a, b, target):
        bits_set = [0 for _ in range(33)]
        soln = 0
        for bit in range(33):
            mask = (1 << bit)
            if mask & a:
                bits_set[bit] += 1
            if mask & b:
                bits_set[bit] += 1
            if mask & target:
                # Bit should be on.
                if bits_set[bit] == 0:
                    soln += 1
            else:
                # Bit should be off.
                soln += bits_set[bit]
        return soln


def test_1():
    a = 2
    b = 4
    target = 8
    expected = 3
    assert Solution().solve(a, b, target) == expected