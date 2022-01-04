"""
binarysearch.com :: Bus Stop
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        queue = collections.deque(nums)
        new_queue = collections.deque()
        soln = 0
        while queue:
            curr = 0
            soln += 1
            for bus in queue:
                if bus > curr:
                    curr = bus
                else:
                    new_queue.append(bus)
            queue, new_queue = new_queue, collections.deque()
        return soln


def test_1():
    nums = [1, 2, 7, 9, 3, 4]
    assert Solution().solve(nums) == 2


def test_2():
    nums = [5, 5]
    assert Solution().solve(nums) == 2
