"""
binarysearch.com :: Boxes All the Way Down
jramaswami
"""


import collections
import operator
import math


Box = collections.namedtuple('Box', ['ht', 'wd'])


class Solution:
    def solve(self, matrix):
        boxes = [Box(a, b) for a, b in matrix]
        boxes.sort(key=operator.attrgetter('wd'))
        dp = [boxes[0]]
        for box in boxes[1:]:
            lo = 0
            hi = len(dp) - 1
            i = len(dp)
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if dp[mid].ht <= box.ht:
                    lo = mid + 1
                else:
                    i = min(i, mid)
                    hi = mid - 1
            if i == len(dp):
                dp.append(box)
            else:
                dp[i] = box
        return len(dp)


def test_1():
    matrix = [[10, 10], [9, 9], [5, 5], [4, 9]]
    expected = 3
    assert Solution().solve(matrix) == expected

def test_2():
    "WA"
    matrix = [[0, 0], [2, 0]]
    expected = 1
    assert Solution().solve(matrix) == expected