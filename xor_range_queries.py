"""
binarysearch.com :: XOR Range Queries
jramaswami
"""


class Solution:
    def solve(self, nums, queries):
        """Use prefix xors to solve problem."""
        from itertools import accumulate
        from operator import xor
        prefix = list(accumulate(nums, xor))

        def get(left, right):
            if left - 1 < 0:
                return prefix[right]
            else:
                return prefix[right] ^ prefix[left - 1]

        return [get(left, right) for left, right in queries]


def brute_force(nums, queries):
    """Brute force solution."""
    soln = []
    for left, right in queries:
        result = 0
        for i in range(left, right+1):
            result ^= nums[i]
        soln.append(result)
    return soln


def test_brute_force():
    """Test brute force solution against sample test."""
    nums = [1, 3, 4, 2]
    queries = [
        [0, 1],
        [1, 3]
    ]
    expected = [2, 5]
    assert brute_force(nums, queries) == expected


def test_1():
    """Test Solution against sample test."""
    nums = [1, 3, 4, 2]
    queries = [
        [0, 1],
        [1, 3]
    ]
    expected = [2, 5]
    assert Solution().solve(nums, queries) == expected


def test_random():
    """Test Solution against brute force solution for random tests."""
    import random
    T = 100
    N = 1000
    K = 10000
    Q = 1000
    for _ in range(T):
        nums = [random.randint(0, K) for _ in range(N)]
        queries = []
        for _ in range(Q):
            a, b = random.randint(0, N-1), random.randint(0, N-1)
            if a > b:
                a, b = b, a
            queries.append((a, b))
        assert Solution().solve(nums, queries) == brute_force(nums, queries)
