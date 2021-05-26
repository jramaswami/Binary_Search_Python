"""
binarysearch.com :: Pair Sums to Power of Two
jramaswami
"""


from collections import Counter


class Solution:
    def solve(self, nums):
        if nums == []:
            return 0

        limit = 2 * max(nums)
        ctr = Counter(nums)

        soln = 0
        for n, freq_n in ctr.items():
            p = 1
            while p <= limit:
                if n <= p:
                    r = p - n
                    if r == n:
                        # Same as freq_n choose 2 = (1/2) * (freq_n - 1) * freq_n
                        soln += (freq_n * (freq_n - 1)) // 2
                    elif r < n:
                        freq_r = ctr.get(r, 0)
                        soln += (freq_n * freq_r)
                p *= 2
        return soln



def test_1():
    nums = [1, 1, 3, 5]
    assert Solution().solve(nums) == 4


def test_2():
    nums = [26, 4, 21, 26, 25, 15, 13, 7, 28, 12, 8, 3, 2, 30, 27, 11, 23, 19, 5, 24]
    assert Solution().solve(nums) == 11


def test_3():
    nums = [15, 2, 19, 10, 11, 18, 11, 19, 1, 2, 16, 17, 11, 16, 8, 11, 4, 5,
            12, 10, 4, 19, 12, 5, 1, 14, 9, 20, 1, 8, 17, 1, 9, 3, 3, 11, 13,
            20, 19, 19, 8, 7, 20, 8, 19, 9, 12, 7, 9, 9, 1, 20, 1, 5, 3, 10,
            16, 9, 3, 10, 2, 14, 1, 2, 13, 8, 16, 20, 5, 13, 13, 5, 20, 8, 3,
            18, 19, 7, 6, 6, 6, 6, 12, 3, 8, 5, 7, 1, 10, 9, 11, 13, 9, 9, 19,
            20, 15, 19, 13, 5]
    assert Solution().solve(nums) == 456


def test_4():
    """WA"""
    nums = [2, 0]
    assert Solution().solve(nums) == 1


def test_5():
    """WA"""
    nums = []
    assert Solution().solve(nums) == 0


def test_6():
    nums = [14, 9, 1, 1, 18, 18, 11, 0, 17, 16, 8, 12, 6, 15, 14, 15, 14, 12,
            4, 13, 20, 19, 15, 19, 7, 6, 8, 2, 14, 13, 20, 2, 20, 14, 20, 16,
            5, 3, 7, 5, 8, 10, 2, 10, 3, 7, 10, 13, 14, 1, 6, 12, 14, 18, 1, 8,
            18, 19, 13, 2, 5, 13, 14, 2, 12, 3, 20, 2, 18, 13, 12, 3, 20, 3,
            18, 11, 15, 6, 13, 16, 17, 16, 4, 20, 11, 14, 4, 2, 2, 17, 14, 19,
            1, 14, 15, 9, 15, 10, 0, 5]
    assert Solution().solve(nums) == 542