"""
binarysearch.com :: Largest Sum of Non-Adjacent Numbers
https://binarysearch.com/problems/Largest-Sum-of-Non-Adjacent-Numbers
"""
class Solution:
    def solve(self, nums):
        max_including_me = [0 for _ in nums]
        max_excluding_me = [0 for _ in nums]
        for i, me in enumerate(nums):
            if i == 0:
                max_including_me[0] += me
            else:
                max_including_me[i] = max_excluding_me[i-1] + me
                max_excluding_me[i] = max(max_excluding_me[i-1], max_including_me[i-1])
        return max(max_including_me[-1], max_excluding_me[-1])


def test_1():
    solver = Solution()
    nums = [2, 4, 6, 2, 5]
    assert solver.solve(nums) == 13

def test_2():
    solver = Solution()
    nums = [5, 1, 1, 5]
    assert solver.solve(nums) == 10

def test_3():
    solver = Solution()
    nums = [-10, -22, -18, -3, -100]
    assert solver.solve(nums) == 0
