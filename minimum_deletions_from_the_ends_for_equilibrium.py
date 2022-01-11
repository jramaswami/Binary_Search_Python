"""
binarysearch.com :: Minimum Deletions From the Ends for Equilibrium
jramaswami
"""


class Solution:

    def solve(self, nums):
        curr_sum = 0
        prev_sums = dict()
        soln = 0
        for i, n in enumerate(nums):
            if n:
                curr_sum += 1
            else:
                curr_sum -= 1

            if curr_sum == 0:
                soln = max(soln, i + 1)

            if curr_sum in prev_sums:
                soln = max(soln, i - prev_sums[curr_sum])
            else:
                prev_sums[curr_sum] = i

        return len(nums) - soln


def test_1():
    nums = [1, 1, 1, 1, 0, 0]
    assert Solution().solve(nums) == 2


def test_2():
    nums = [0, 1, 1, 0]
    assert Solution().solve(nums) == 0
