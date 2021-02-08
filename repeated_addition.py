"""
binarysearch.com :: Repeated Addition
jramaswami
"""
def digit_sum(n):
    t = 0
    while n:
        n, r = divmod(n, 10)
        t += r
    return t


class Solution:
    def solve(self, n):
        while n > 10:
            n = digit_sum(n)
        return n

def test_1():
    assert Solution().solve(8835) == 6

def test_2():
    assert Solution().solve(10) == 1
