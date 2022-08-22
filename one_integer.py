"""
binarysearch.com :: One Integer
jramaswami
"""


import heapq


class Solution:
    def solve(self, nums):
        # Intuition: the earlier you choose a number, the more times it
        # will contribute to the final cost, therefore you should always
        # choose the smallest two numbers when combining to remove them.
        # Overall, O(n log n) solution with no extra space required.

        # Sort nums into a min heap.
        # O(n) according to Python docs.
        heapq.heapify(nums)
        total_cost = 0

        # Iterate over nums, choosing removing smallest two numbers and
        # then adding the sum to the heapq.
        # O(n log n)
        while len(nums) > 1:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            t = a + b
            total_cost += t
            heapq.heappush(nums, t)
        return total_cost


def test_1():
    nums = [1, 2, 3, 4, 5]
    expected = 33
    assert Solution().solve(nums) == expected