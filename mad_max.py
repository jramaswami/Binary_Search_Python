"""
binarysearch.io :: Mad Max
https://binarysearch.com/problems/Mad-Max
"""
import heapq

class Solution:
    def solve(self, nums, k):
        left = 0
        right = k-1
        heap = [(-n, i) for i , n in enumerate(nums[:k])]
        heapq.heapify(heap)
        left = 0
        soln = []
        while right < len(nums):
            heapq.heappush(heap, (-nums[right], right))
            while heap[0][1] < left:
                heapq.heappop(heap)
            soln.append(-heap[0][0])
            left += 1
            right += 1
        return soln

def test_1():
    nums = [10, 5, 2, 7, 8, 7]
    k = 3
    solver = Solution()
    assert solver.solve(nums, k) == [10, 7, 8, 8]

def test_2():
    nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    k = 3
    solver = Solution()
    assert solver.solve(nums, k) == [3, 4, 5, 5, 5, 4, 3]

def test_3():
    nums = [3, 2, 1, 2, 3]
    k = 2
    solver = Solution()
    assert solver.solve(nums, k) == [3, 2, 2, 3]

def test_4():
    nums = [3, 2, 1, 2, 3]
    k = 5
    solver = Solution()
    assert solver.solve(nums, k) == [3]
