"""
binarysearch.com :: Lego Towers
jramaswami
"""
from collections import deque


class Solution:
    def solve(self, heights, k):
        # Base case
        if k == 1:
            return 0

        heights0 = sorted(heights)

        towers = deque(heights0[:k])
        soln = sum(towers[-1] - t for t in towers)
        curr = soln
        for i in range(k, len(heights0)):
            # Remove the delta from the first tower
            curr -= (towers[-1] - towers[0])
            # Remove the tower
            towers.popleft()
            # We are going to add the tower at index i. So, we need to add
            # the difference for each tower still towers.
            curr += (k - 1) * (heights0[i] - towers[-1])
            # Now put the new tower in the towers.
            towers.append(heights0[i])
            soln = min(soln, curr)
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

def test_4():
    heights = [6799, 5653, 1728, 3800, 3540, 9034, 8398, 3351, 392, 4580, 3363, 8415, 860, 9797, 9542, 8414, 8312, 5472, 1176, 3565, 1407, 8480, 2098, 9984, 7470, 5542, 853, 9656, 758, 2131, 9067]
    k = 3
    assert Solution().solve(heights, k) == 18

def test_5():
    heights = [2, 2]
    k = 1
    assert Solution().solve(heights, k) == 0
