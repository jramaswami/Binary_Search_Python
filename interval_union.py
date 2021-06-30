"""
binarysearch.com :: Interval Union
jramaswami
"""


class Solution:
    def solve(self, intervals):
        soln = []
        if intervals:
            # Sort the intervals by left ascending and right descending.
            # O(N log N)
            intervals.sort(key=lambda t: (t[0], -t[1]))

            # For each interval in the sorted list.
            # O(N)
            l1, r1 = intervals[0]
            for l2, r2 in intervals[1:]:
                if max(l1, l2) <= min(r1, r2):
                    # If the new interval overlaps with the running interval,
                    # then extend the running interval to include the new
                    # interval.
                    l1 = min(l1, l2)
                    r1 = max(r1, r2)
                else:
                    # If the new interval does not overlap, then append the
                    # current interval to the solution list and start a new
                    # current interval.
                    soln.append([l1, r1])
                    l1, r1 = l2, r2

            # Append last interval
            soln.append([l1, r1])

        return soln


def test_1():
    intervals = [[0, 5], [4, 6]]
    expected = [[0, 6]]
    assert Solution().solve(intervals) == expected
