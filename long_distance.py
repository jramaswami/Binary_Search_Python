"""
binarysearch.com :: Long Distance
jramaswami
"""


class Solution:

    def solve(self, nums):

        nums0 = [(v, i) for i, v in enumerate(nums)]
        aux = list(nums)
        soln = [0 for _ in nums]

        def merge(lo, mid, hi):
            i = lo
            j = mid + 1
            k = lo

            inversions = 0
            while i <= mid and j <= hi:
                if nums0[i][0] <= nums0[j][0]:
                    aux[k] = nums0[i]
                    soln[nums0[i][1]] += inversions
                    i += 1
                    k += 1
                else:
                    # This is an inversion for every item still in the left.
                    inversions += 1
                    aux[k] = nums0[j]
                    j += 1
                    k += 1

            while i <= mid:
                soln[nums0[i][1]] += inversions
                aux[k] = nums0[i]
                i += 1
                k += 1

            while j <= hi:
                aux[k] = nums0[j]
                j += 1
                k += 1

            for k in range(lo, hi+1):
                nums0[k] = aux[k]

        def merge_sort(lo, hi):
            if lo >= hi:
                return
            mid = lo + ((hi - lo) // 2)
            merge_sort(lo, mid)
            merge_sort(mid + 1, hi)
            merge(lo, mid, hi)

        merge_sort(0, len(nums)-1)
        return soln


def test_1():
    nums = [3, 4, 9, 6, 1]
    expected = [1, 1, 2, 1, 0]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().solve(nums) == expected


def test_3():
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert Solution().solve(nums) == expected


def test_5():
    nums = list(reversed(range(100000)))
    expected = list(reversed(range(100000)))
    assert Solution().solve(nums) == expected


def test_6():
    """WA"""
    nums = [0, 0]
    expected = [0, 0]
    assert Solution().solve(nums) == expected
