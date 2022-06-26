"""
binarysearch.com :: Sum of Sublist Range Sum
jramaswami
"""


import heapq


class Solution:
    def solve(self, nums, i, j):
        A = []
        B = [(n, p, p) for p, n in enumerate(nums)]
        heapq.heapify(B)
        while len(A) <= j:
            # Pop the smallest current sublist sum off the heap.
            x, l, r = heapq.heappop(B)
            A.append(x)
            # Extend right by 1.
            if r + 1 < len(nums):
                y = x + nums[r+1]
                heapq.heappush(B, (y, l, r+1))
        return sum(A[i:j+1])


def test_1():
    nums = [1, 2, 3, 4]
    i = 2
    j = 3
    expected = 6
    assert Solution().solve(nums, i, j) == expected
