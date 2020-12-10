"""
binarysearch.com :: Packing Boxes
https://binarysearch.com/problems/Packing-Boxes
"""
class Solution:
    def solve(self, nums):
        if not nums:
            return []
        boxes = [[nums[0]]]
        for n in nums[1:]:
            if boxes[-1][-1] == n:
                boxes[-1].append(n)
            else:
                boxes.append([n])
        return boxes


def test_1():
    nums = [4, 4, 1, 6, 6, 6, 1, 1, 1, 1]
    expected = [
        [4, 4],
        [1],
        [6, 6, 6],
        [1, 1, 1, 1]
    ]
    solver = Solution()
    assert solver.solve(nums) == expected

def test_2():
    nums = [5, 5, 5, 5, 5, 5, 5, 5]
    expected = [
        [5, 5, 5, 5, 5, 5, 5, 5]
    ]
    solver = Solution()
    assert solver.solve(nums) == expected

def test_3():
    nums = [1]
    expected = [
        [1]
    ]
    solver = Solution()
    assert solver.solve(nums) == expected

def test_4():
    nums = []
    expected = []
    solver = Solution()
    assert solver.solve(nums) == expected