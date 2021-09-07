"""
binarysearch.com :: Remove Smallest Peaks in Order
jramaswami
"""


import heapq


class Solution:

    def solve(self, nums):
        # Use a heap to keep track of the smallest peaks.
        peaks = []

        # Use pointers to keep track next and previous elements as elements
        # are removed from the list.
        next_idx = [0 for _ in nums]
        prev_idx = [0 for _ in nums]
        p, n = -1, 1
        for i, _ in enumerate(nums):
            prev_idx[i], next_idx[i] = p, n
            p += 1
            n += 1

        def get_next_i(i):
            """Return next index or len(nums) if there isn't a next element."""
            if i < 0:
                return -1
            if i >= len(nums):
                return len(nums)
            return next_idx[i]

        def get_prev_i(i):
            """Return previous index or -1 if there isn't a previous element."""
            if i < 0:
                return -1
            if i >= len(nums):
                return len(nums)
            return prev_idx[i]

        def remove_element(i):
            """Remove element by manipulating next and previous pointers."""
            prev_i = get_prev_i(i)
            next_i = get_next_i(i)

            # My next should point to my previous
            if next_i < len(nums):
                prev_idx[next_i] = prev_i
            # My prev shluld point to my next
            if prev_i >= 0:
                next_idx[prev_i] = next_i

        def is_peak(i):
            """Return True if element is currently a peak."""
            if i < 0 or i >= len(nums):
                return False

            prev_i = get_prev_i(i)
            next_i = get_next_i(i)
            # If a list has one element, then that element is considered to be
            # a peak.
            if prev_i < 0 and next_i >= len(nums):
                return True
            elif prev_i < 0:
                return nums[i] > nums[next_i]
            elif next_i >= len(nums):
                return nums[prev_i] < nums[i]
            return nums[prev_i] < nums[i] and nums[i] > nums[next_i]

        # Find current peaks and add them to the heap
        for i, n in enumerate(nums):
            if is_peak(i):
                heapq.heappush(peaks, (n, i))

        soln = []
        while peaks:
            n, i = heapq.heappop(peaks)
            soln.append(n)
            prev_i = get_prev_i(i)
            next_i = get_next_i(i)
            # Remove the item from the list.
            remove_element(i)
            # Check if the previous or next elements have become peaks.  If
            # so, add them to the list.
            if is_peak(prev_i):
                heapq.heappush(peaks, (nums[prev_i], prev_i))
            if is_peak(next_i):
                heapq.heappush(peaks, (nums[next_i], next_i))

        return soln


def test_1():
    nums = [3, 5, 1, 4, 2]
    assert Solution().solve(nums) == [4, 2, 5, 3, 1]


def test_2():
    nums = [5, 6, 7]
    assert Solution().solve(nums) == [7, 6, 5]


def test_3():
    nums = [3, 2, 1]
    assert Solution().solve(nums) == [3, 2, 1]
