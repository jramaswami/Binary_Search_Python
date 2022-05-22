"""
binarysearch.com :: K-Distinct Groups
jramaswami
"""


class Solution:
    def solve(self, counts, k):

        def check(groups):
            r = groups * k
            for x in counts:
                r -= min(x, groups, r)
                if r == 0:
                    return True
            return False

        soln = 0
        lo, hi = 0, sum(counts)
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = max(mid, soln)
                lo = mid + 1
            else:
                hi = mid - 1
        return soln


def test_1():
    counts = [3, 3, 2, 5]
    k = 2
    expected = 6
    assert Solution().solve(counts, k) == expected


def test_2():
    counts = [3, 2, 4]
    k = 3
    expected = 2
    assert Solution().solve(counts, k) == expected


def test_3():
    "WA"
    counts = [1, 0]
    k = 1
    expected = 1
    assert Solution().solve(counts, k) == expected
