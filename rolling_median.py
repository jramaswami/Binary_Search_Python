"""
binarysearch.com :: Rolling Median
jramaswami
"""


import heapq


class MaxPQ:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def top(self):
        return -self.heap[0]

    def pop(self):
        return -(heapq.heappop(self.heap))

    def empty(self):
        return self.heap == []

    def __len__(self):
        return len(self.heap)


class MinPQ:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, value)

    def top(self):
        return self.heap[0]

    def pop(self):
        return (heapq.heappop(self.heap))

    def empty(self):
        return self.heap == []

    def __len__(self):
        return len(self.heap)


class RollingMedian:
    def __init__(self):
        self.left = MaxPQ()
        self.right = MinPQ()
        self.curr_median = 0
        self.length = 0

    def add(self, val):
        self.length += 1

        if not self.left or val < self.curr_median:
            self.left.push(val)
        else:
            self.right.push(val)

        delta = self.length % 2
        while abs(len(self.left) - len(self.right)) > delta:
            if len(self.left) > len(self.right):
                self.right.push(self.left.pop())
            else:
                self.left.push(self.right.pop())

        if self.length % 2:
            assert abs(len(self.left) - len(self.right)) == 1
        else:
            assert len(self.left) == len(self.right)

        if self.length % 2:
            if len(self.left) > len(self.right):
                self.curr_median = self.left.top()
            else:
                self.curr_median = self.right.top()
        else:
            self.curr_median = (self.right.top() + self.left.top()) / 2

        return None

    def median(self):
        return self.curr_median


def test_1():
    arguments = [[], [1], [2], [3], [], [4], []]
    rm = RollingMedian()
    expected = [None, None, None, None, 2, None, 2.5]
    for args,exp in zip(arguments[1:], expected[1:]):
        if args:
            result = rm.add(*args)
        else:
            result = rm.median()
        assert exp == result


def test_2():
    rm = RollingMedian()
    assert rm.add(3) == None
    assert rm.add(6) == None
    assert rm.median() == 4.5
    assert rm.add(4) == None
    assert rm.add(9) == None
    assert rm.median() == 5.0
    assert rm.median() == 5.0
    assert rm.add(-6) == None
    assert rm.median() == 4
    assert rm.add(-7) == None
    assert rm.median() == 3.5
    assert rm.add(6) == None
    assert rm.median() == 4
    assert rm.add(-3) == None
    assert rm.add(4) == None
    assert rm.median() == 4


def main():
    """Check by hand."""
    import random
    calls = [random.randint(0, 1) for _ in range(20)]
    arguments = [random.randint(-10, 10) for _ in range(20)]
    rm = RollingMedian()
    for call, arg in zip(calls, arguments):
        if call:
            result = rm.add(arg)
            print(f"rm.add({arg}) = {result}")
        else:
            result = rm.median()
            print(f"rm.median() = {result}")


if __name__ == '__main__':
    main()
