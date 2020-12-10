"""
binarysearch.comm :: Find the Largest Number in a Rotated List
https://binarysearch.com/problems/Find-the-Largest-Number-in-a-Rotated-List
"""
class Solution:
    def solve(self, arr):
        # Binary search for rotation point.
        low = 0
        high = len(arr) - 1
        rot = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > arr[-1]:
                # If the current number is greater than the last number in
                # the array then the rotation point is to the right.
                low = mid + 1
            else:
                # If the current number is less than the last number then
                # the rotation point is here or to the left.
                rot = min(rot, mid)
                high = mid - 1
        # The highest number will be to the left (or wrapped around) of
        # the rotation point.
        return arr[rot - 1]

def test_1():
    arr = [6, 7, 8, 1, 4]
    solver = Solution()
    assert solver.solve(arr) == 8

def test_2():
    arr = [1, 2, 3]
    solver = Solution()
    assert solver.solve(arr) == 3

def test_3():
    arr = [1]
    solver = Solution()
    assert solver.solve(arr) == 1

def test_4():
    arr = [10, 1, 2, 3, 4, 7]
    solver = Solution()
    assert solver.solve(arr) == 10