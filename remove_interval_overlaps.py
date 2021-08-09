"""
binarysearch.com :: Remove Interval Overlaps
jramaswami
"""


class Solution:
    def solve(self, intervals):
        # Corner case: empty intervals
        if intervals == []:
            return 0

        def overlaps(L1, R1, L2, R2):
            """Return True if intervals overlap."""
            return max(L1, L2) < min(R1, R2)

        intervals.sort()
        dp = [1 for _ in intervals]
        for i, (L1, R1) in enumerate(intervals):
            for j, (L2, R2) in enumerate(intervals[:i]):
                if not overlaps(L1, R1, L2, R2):
                    dp[i] = max(dp[i], dp[j] + 1)

        return len(intervals) - max(dp)



def test_1():
    intervals = [
        [7, 9],
        [2, 4],
        [5, 8]
    ]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [
        [1, 5],
        [1, 5],
        [1, 5]
    ]
    expected = 2
    assert Solution().solve(intervals) == expected


def test_3():
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_4():
    intervals = [[1,2],[2,3]]
    expected = 0
    assert Solution().solve(intervals) == expected


def test_5():
    """RTE"""
    intervals = []
    expected = 0
    assert Solution().solve(intervals) == expected
