"""
binarysearch.com :: Lego Towers
jramaswami
"""
from collections import deque


class Solution:
    def solve(self, heights, k):
        heights0 = sorted(heights)

        towers = deque(heights0[:k])
        soln = sum(towers[-1] - t for t in towers)
        for i in range(k, len(heights0)):
            towers.popleft()
            towers.append(heights0[i])
            soln = min(soln, sum(towers[-1] - t for t in towers))
        return soln



def test_1():
    heights = [4, 7, 31, 14, 40]
    k = 3
    assert Solution().solve(heights, k) == 17

def test_2():
    heights = [4, 4, 2, 4, 4]
    k = 5
    assert Solution().solve(heights, k) == 2

def test_3():
    heights = [986, 74, 865, 856, 654, 965, 1239]
    k = 3
    assert Solution().solve(heights, k) == 142
