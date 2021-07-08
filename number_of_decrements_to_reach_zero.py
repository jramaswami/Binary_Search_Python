"""
binarysearch.com :: Number of Decrements to Reach Zero
jramaswami

x = n - n/2
2x = 2n - n
2x = n
x = n / 2

x = n - 2n / 3
3x = 3n - 2n
3x = n
x = n / 3
"""


from collections import defaultdict
from math import inf
import heapq


class Solution:
    def solve(self, n):
        Q = [-n]
        dist = defaultdict(lambda: inf)
        dist[n] = 0
        visited = set()
        visited.add(n)
        while Q:
            k = -heapq.heappop(Q)
            if not k:
                continue

            # Distance to zero by 1.
            dist[0] = min(dist[0], dist[k] + k)

            # Distance to nearest even number.
            k2, r2 = divmod(k, 2)
            d2 = dist[k] + r2 + 1
            dist[k2] = min(dist[k2], d2)
            if k2 not in visited:
                heapq.heappush(Q, -k2)
                visited.add(k2)

            # Distance to nearest number divisible by 3.
            k3, r3 = divmod(k, 3)
            d3 = dist[k] + r3 + 1
            dist[k3] = min(dist[k3], d3)
            if k3 not in visited:
                heapq.heappush(Q, -k3)
                visited.add(k3)

        return dist[0]


def test_1():
    assert Solution().solve(15) == 5


def test_2():
    assert Solution().solve(100) == 8


def test_3():
    assert Solution().solve(1000000000) == 31
