"""
binarysearch.com :: Earliest Uniques in a Stream
jramaswami
"""
from collections import deque, Counter


class EarliestUnique:
    def __init__(self, nums):
        self.nums = deque(nums)
        self.freqs = Counter(nums)

    def add(self, num):
        self.nums.append(num)
        self.freqs[num] += 1

    def earliestUnique(self):
        while self.nums and self.freqs[self.nums[0]] > 1:
            self.nums.popleft()
        return self.nums[0] if self.nums else -1


def test_1():
    methods = ["constructor", "add", "earliestUnique", "add", "earliestUnique"]
    arguments = [[[1, 2, 3]], [1], [], [2], []]
    expected = [None, None, 2, None, 3]
    eu = EarliestUnique(*arguments[0])
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        res = getattr(eu, meth)(*args)
        assert res == exp

def test_2():
    """RTE"""
    methods = ["constructor", "earliestUnique", "add", "earliestUnique"]
    arguments = [[[3, 1, 1]], [], [3], []]
    expected = [None, 3, None, -1]
    eu = EarliestUnique(*arguments[0])
    for meth, args, exp in zip(methods[1:], arguments[1:], expected[1:]):
        res = getattr(eu, meth)(*args)
        assert res == exp
