"""
binarysearch.com :: Bunnyhopping
jramaswami
"""

import heapq
from collections import namedtuple


QItem = namedtuple('QItem', ['cost', 'index'])


class Solution:

    def solve(self, nums, k):
        Q = [QItem(nums[0], 0)]
        cost = [0 for _ in nums]
        for i, n in enumerate(nums[1:], start=1):
            # Remove any items outside the window
            while Q and Q[0].index < i - k:
                cost[Q[0].index] = Q[0].cost
                heapq.heappop(Q)
            # Add shortest path to current index.
            heapq.heappush(Q, QItem(n + Q[0].cost, i))

        while Q:
            cost[Q[0].index] = Q[0].cost
            heapq.heappop(Q)

        return cost[-1]


def test_1():
    nums = [1, 2, 3, 4, 5]
    k = 2
    expected = 9
    assert Solution().solve(nums, k) == expected


def main():
    """Timing"""
    import random
    nums = [random.randint(1, 1000) for _ in range(100000)]
    k = random.randint(1, len(nums))
    print(Solution().solve(nums, k))


if __name__ == "__main__":
    main()
