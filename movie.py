"""
binarysearch.com :: Weekly Contest 43 :: View Over People
jramaswami
"""
import heapq


class Solution:
    def solve(self, heights, k):
        tallest = []
        i = 1
        while i < len(heights) and len(tallest) < k:
            heapq.heappush(tallest, (-heights[i], i))
            i += 1

        soln = []
        for i, h in enumerate(heights):

            while tallest and tallest[0][1] <= i:
                heapq.heappop(tallest)

            if not tallest or -tallest[0][0] < h:
                soln.append(i)

            if i + k + 1 < len(heights):
                heapq.heappush(tallest, (-heights[i + k + 1], i + k + 1))

        return soln


def test_1():
    heights = [9, 8, 7, 7, 4, 9]
    k = 2
    assert Solution().solve(heights, k) == [0, 1, 5]

def test_2():
    heights = [5, 5, 5, 5]
    k = 3
    assert Solution().solve(heights, k) == [3]

def test_3():
    heights = [1]
    k = 1
    assert Solution().solve(heights, k) == [0]
