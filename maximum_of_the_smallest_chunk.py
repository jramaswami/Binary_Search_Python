"""
binarysearch.com :: Maximum of the Smallest Chunk
jramaswami
"""


class Solution:

    def solve(self, nums, k):

        def check(max_sum):
            chunks = 0
            curr_sum = 0
            for n in nums:
                if curr_sum + n > max_sum:
                    chunks += 1
                    curr_sum = n
                else:
                    curr_sum += n
            return chunks + 1 <= k

        lo = min(nums)
        hi = sum(nums)
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                hi = mid - 1
                soln = min(soln, mid)
            else:
                lo = mid + 1
        return mid



def test_1():
    nums = [1, 5, 3, 4, 7]
    k = 3
    expected = 6
    assert Solution().solve(nums, k) == expected


def test_2():
    "WA"
    nums = [1, 2, 1]
    k = 2
    expected = 1
    assert Solution().solve(nums, k) == expected
