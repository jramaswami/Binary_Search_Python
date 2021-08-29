"""
binarysearch.com :: Eat Bananas in K Hours
jramaswami
"""


import heapq


class Solution:

    def solve(self, piles, hours):
        def can_eat(r, ps, hs):
            """
            Return true if you can eat all bananas in hs hours by eating
            r bananas per hour.
            """
            for _ in range(hs):
                if ps:
                    bs = -heapq.heappop(ps)
                    if bs - r > 0:
                        heapq.heappush(ps, -(bs - r))

            return len(ps) == 0

        # Heapify the piles in a max heap.
        piles0 = [-p for p in piles]
        heapq.heapify(piles0)

        # Binary search for the answer.
        lo = 0
        hi = max(piles)
        soln = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            piles1 = list(piles0)
            if can_eat(mid, piles1, hours):
                # You can eat all bananas mid per hour.
                soln = min(soln, mid)
                # Try eating less bananas per hour.
                hi = mid - 1
            else:
                # You cannot eat all the bananas mid per hour so try
                # a higher number than mid.
                lo = mid + 1

        return soln


def test_1():
    piles = [6, 4, 3]
    k = 5
    assert Solution().solve(piles, k) == 3
