"""
binarysearch.com :: Bunnyhopping
jramaswami
"""

import heapq
from math import inf


class Solution:

    def solve(self, nums, k):
        dist = [inf for _ in nums]
        dist[0] = nums[0]
        Q = []
        heapq.heappush(Q, (dist[0], 0))
        while Q:
            d, i = heapq.heappop(Q)
            if dist[i] != d:
                continue
            for off in range(1, k+1):
                j = i + off
                if j < len(nums) and dist[i] + nums[j] < dist[j]:
                    dist[j] = dist[i] + nums[j]
                    heapq.heappush(Q, (dist[j], j))
        return dist[-1]



def test_1():
    nums = [1, 2, 3, 4, 5]
    k = 2
    expected = 9
    assert Solution().solve(nums, k) == expected


def main():
    import random
    nums = [random.randint(1, 1000) for _ in range(100000)]
    k = random.randint(1, len(nums))
    print(Solution().solve(nums, k))


if __name__ == "__main__":
    main()
