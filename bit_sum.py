"""
binarysearch.com :: Bit Sum
jramaswami
"""
import heapq


MOD = pow(10, 9) + 7


def is_bit_set(n, offset):
    """Set the offset-th bit."""
    mask = 1 << offset
    return n & mask


def set_bit(n, offset):
    """Return True if the offset-th bit is set in n."""
    mask = 1 << offset
    return n | mask


def first_zero_bit(n):
    """Return the index of the first zero bit."""
    for i in range(64):
        if not is_bit_set(n, i):
            return i

class Solution:
    def solve(self, nums, k):
        queue = []
        for i, n in enumerate(nums):
            fzb = first_zero_bit(n)
            heapq.heappush(queue, (fzb, i))

        for _ in range(k):
            fzb, i = heapq.heappop(queue)
            nums[i] = set_bit(nums[i], fzb)
            fzb = first_zero_bit(nums[i])
            heapq.heappush(queue, (fzb, i))

        soln = 0
        for n in nums:
            soln = (soln + n) % MOD
        return soln


def test_1():
    nums = [3, 7, 3]
    k = 2
    assert Solution().solve(nums, k) == 21

def test_2():
    nums = [5, 3]
    k = 1
    assert Solution().solve(nums, k) == 10
