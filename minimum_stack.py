"""
binarysearch.com :: Minimum Stack
jramaswami
"""


import math


class MinimumStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def append(self, val):
        self.stack.append(val)
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

    def pop(self):
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()
