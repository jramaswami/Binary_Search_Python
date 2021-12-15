"""
binarysearch.com :: Median of Two Sorted Lists
jramaswami
"""


import operator


class Solution:

    def solve(self, nums0, nums1):

        def binsearch(A, t, op):
            "Return the index of the rightmost element less than t."
            lo = 0
            hi = len(A) - 1
            soln = -1
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if op(A[mid], t):
                    soln = max(mid, soln)
                    lo = mid + 1
                else:
                    hi = mid - 1
            return soln

        def solve0():
            median_index = (len(nums0) + len(nums1)) // 2
            lo = 0
            hi = len(nums0) - 1
            while lo <= hi:
                mid = lo + ((hi - lo)) // 2
                lt = binsearch(nums1, nums0[mid], operator.lt)
                le = binsearch(nums1, nums0[mid], operator.le)
                left = mid + lt + 1
                right= mid + le + 1
                if left <= median_index <= right:
                    return nums0[mid]
                elif median_index < left:
                    hi = mid - 1
                else:
                    lo = mid + 1

        soln = solve0()
        if not soln:
            nums0, nums1 = nums1, nums0
            return solve0()
        return soln



def test_1():
    nums0 = [1, 2, 5]
    nums1 = [3, 6, 7]
    expected = 5
    assert Solution().solve(nums0, nums1) == expected


def test_2():
    nums0 = [1, 2]
    nums1 = [3, 6, 7]
    expected = 3
    assert Solution().solve(nums0, nums1) == expected


def test_3():
    nums0 = [1, 1, 1, 1]
    nums1 = [1, 1]
    expected = 1
    assert Solution().solve(nums0, nums1) == expected


def test_4():
    nums0 = [1, 2, 3, 5, 7]
    nums1 = []
    expected = 3
    assert Solution().solve(nums0, nums1) == expected


def test_5():
    nums0 = []
    nums1 = [1, 2, 3, 5, 7]
    expected = 3
    assert Solution().solve(nums0, nums1) == expected


def test_random():
    import random
    for _ in range(100):
        A = [random.randint(0, 10000) for _ in range(10000)]
        B = [random.randint(0, 10000) for _ in range(10000)]
        A.sort()
        B.sort()
        C = A + B
        C.sort()
        median_index = len(C) // 2
        expected = C[median_index]
        # print(C)
        # print(expected)
        assert Solution().solve(A, B) == expected


def test_6():
    "WA"
    nums0 = [0]
    nums1 = []
    expected = 0
    assert Solution().solve(nums0, nums1) == expected
