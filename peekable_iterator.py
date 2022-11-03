"""
binarysearch.com :: Peekable Iterator
jramaswami
"""


class PeekableIterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def peek(self):
        return self.nums[self.index]

    def next(self):
        x = self.nums[self.index]
        self.index += 1
        return x

    def hasnext(self):
        return self.index < len(self.nums)