"""
binarysearch.com :: Guess the Root
jramaswami
"""
class Solution:
    def solve(self, n):
        """Binary search for solution."""
        soln = 0
        low = 0
        high = n
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= n:
                soln = max(soln, mid)
                low = mid + 1
            else:
                high = mid - 1
        return soln


def test_1():
    assert Solution().solve(9) == 3


def test_2():
    assert Solution().solve(26) == 5


def test_3():
    assert Solution().solve(0) == 0


def test_random():
    import random
    import math
    limit = pow(2, 31)
    for _ in range(1000):
        n = random.randint(0, limit)
        t = int(math.sqrt(n))
        assert t == Solution().solve(n)