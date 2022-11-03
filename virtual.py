"""
binarysearch.com :: Weekly Contest 38 :: Virtual Array
https://binarysearch.com/room/Weekly-Contest-38-CNs3hGBp9j?questionsetIndex=3
"""
import bisect


class VirtualArray:
    def __init__(self):
        self.intervals = []
        
    def set(self, start, end):
        """Set the values in the array from [start, end] inclusive to True."""
        i = bisect.bisect_left(self.intervals, (start, end))
        if i > 0:
            prev_start, prev_end = self.intervals[i-1]
            # Do not insert if previous interval covers this one.
            if prev_start <= start and prev_end >= end:
                return
            # Extend the previous interval if there is an overlap.
            elif prev_start <= start and start <= prev_end and end > prev_end:
                j = i
                while j < len(self.intervals):
                    next_start, next_end = self.intervals[j]
                    if next_start > end:
                        break
                    elif next_start >= prev_start and next_end <= end:
                        # It it is covered, delete it
                        del self.intervals[j]
                    elif next_start >= prev_start and next_start <= end and next_end > end:
                        # Extend interval
                        end = next_end
                self.intervals[i-1] = (prev_start, end)
                return
        else:
            prev_start, prev_end = start, end
            j = 0
            while j < len(self.intervals):
                next_start, next_end = self.intervals[j]
                if next_start > end:
                    break
                elif next_start >= prev_start and next_end <= end:
                    # It it is covered, delete it
                    del self.intervals[j]
                elif next_start >= prev_start and next_start <= end and next_end > end:
                    # Extend interval
                    end = next_end
        bisect.insort_left(self.intervals, (start, end))

    def get(self, idx):
        """Returns True if it is set, otherwise False."""
        i = bisect.bisect_left(self.intervals, (idx, idx))
        if i < len(self.intervals) and self.intervals[i][0] <= idx and idx <= self.intervals[i][1]:
            return True
        if i > 0 and self.intervals[i-1][0] <= idx and idx <= self.intervals[i-1][1]:
            return True
        return False


def test_1():
    va = VirtualArray()
    va.set(2, 5)
    assert va.get(4) == True
    va.set(8, 9)
    assert va.get(6) == False
    assert va.get(8) == True

def test_2():
    va = VirtualArray()
    va.set(10, 100)
    va.set(6, 100)
    assert va.get(9) == True

def test_3():
    va = VirtualArray()
    va.set(2, 2)
    va.set(0, 4)
    assert va.get(3) == True
    assert va.get(4) == True
