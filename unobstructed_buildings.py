"""
binarysearch.com :: Unobstructed Buildings
jramaswami
"""
class Solution:
    def solve(self, heights):
        max_height = 0
        soln = []
        for i in range(len(heights)-1, -1, -1):
            h = heights[i]
            if h > max_height:
                soln.append(i)
            max_height = max(max_height, h)
        return soln[::-1]

def test_1():
    heights = [1, 5, 5, 2, 3]
    assert Solution().solve(heights) == [2, 4]

def test_2():
    heights = [5, 4, 3, 2, 1]
    assert Solution().solve(heights) == [0, 1, 2, 3, 4]
