"""
binarysearch.com :: Weekly Contest 41 :: Window Limits
jramaswami
"""
import heapq

class Solution:
    def solve(self, nums, window, limit):
        max_heap = [(-n, i) for i, n in enumerate(nums[:window])]
        min_heap = [(n, i) for i, n in enumerate(nums[:window])]
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        if abs(min_heap[0][0] + max_heap[0][0]) > limit:
            return False

        for i in range(window, len(nums)):
            # Remove any items should be removed.
            while max_heap and max_heap[0][1] <= i - window:
                heapq.heappop(max_heap)
            while min_heap and min_heap[0][1] <= i - window:
                heapq.heappop(min_heap)

            # Adding nums[i]
            heapq.heappush(max_heap, (-nums[i], i))
            heapq.heappush(min_heap, (nums[i], i))

            if abs(min_heap[0][0] + max_heap[0][0]) > limit:
                return False

        return True


def test_1():
    nums = [1, 3, 7, 5]
    window = 2
    limit = 4
    assert Solution().solve(nums, window, limit) == True

def test_2():
    nums = [1, 3, 7, 5]
    window = 3
    limit = 4
    assert Solution().solve(nums, window, limit) == False
