"""
Binary Search :: Weekly Contest 26 :: Win After Last Round
"""

class Solution:
    def solve(self, nums):
        soln = 0
        if nums:
            N = len(nums)
            nums.sort(reverse=True)
            K = max(a + p for a, p in zip(nums, range(1, N+1)))
            for i in range(N):
                M = nums[i] + N
                if M >= K:
                    soln += 1
        return soln


def test_1():
    solver = Solution()
    assert 3 == solver.solve([8, 7, 10, 11])

def test_2():
    solver = Solution()
    assert 0 == solver.solve([])

def test_3():
    solver = Solution()
    assert 1 == solver.solve([1])

def test_4():
    solver = Solution()
    assert 2 == solver.solve([0, 0])

def test_5():
    solver = Solution()
    assert 2 == solver.solve([0, 2, 2])

def test_6():
    solver = Solution()
    assert 3 == solver.solve([0, 2, 2, 3])