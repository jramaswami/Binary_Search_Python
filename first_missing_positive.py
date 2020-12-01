"""
binarysearch.com :: First Missing Positive
https://binarysearch.com/problems/First-Missing-Positive
"""
class Solution:
    def solve0(self, nums):
        """Original solution that sorted numbers, so is O(log n)."""
        nums0 = sorted(n for n in nums if n > 0)
        searching_for = 1
        for n in nums0:
            print(n, searching_for)
            if n > searching_for:
                return searching_for
            elif n == searching_for:
                searching_for += 1
        return searching_for


    def solve(self, nums):
        """Bettter solution that is O(n)."""
        found = [False for _ in range(len(nums)+1)]
        found[0] = True
        for n in nums:
            if n > 0 and n < len(found):
                found[n] = True

        for i, f in enumerate(found):
            if not f:
                return i
        return len(nums)+1


def test_1():
    solver = Solution()
    nums = [1, 2, 3]
    assert solver.solve(nums) == 4

def test_2():
    solver = Solution()
    nums = [3, 4, -1, 1]
    assert solver.solve(nums) == 2

def test_3():
    solver = Solution()
    nums = [1, 2, 0]
    assert solver.solve(nums) == 3

def test_4():
    solver = Solution()
    nums = [-1, -2, -3]
    assert solver.solve(nums) == 1

def test_5():
    solver = Solution()
    nums = [1, 1]
    assert solver.solve(nums) == 2
