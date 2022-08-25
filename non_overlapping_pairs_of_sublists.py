"""
binarysearch.com :: Non-Overlapping Pairs of Sublists
jramaswami
"""


MOD = pow(10, 9) + 7


class Solution:

    def solve(self, nums, k):
        sublists_ending_at = [0 for _ in nums]
        curr = 0
        for i, n in enumerate(nums):
            if n >= k:
                curr += 1
            else:
                curr = 0
            sublists_ending_at[i] = curr

        sublists_starting_at = [0 for _ in nums]
        curr = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= k:
                curr += 1
            else:
                curr = 0
            sublists_starting_at[i] = curr

        suffix = [0 for _ in nums]
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr += sublists_starting_at[i]
            suffix[i] = curr
        suffix.append(0)

        soln = 0
        for i, _ in enumerate(nums):
            # Pick any sublist ending at i.
            x = sublists_ending_at[i]
            # Pick any of the sublists starting anywhere after i.
            y = suffix[i+1]
            # We can pair any sublists ending at i with any suffix
            # starting anywhere after i.
            z = (x * y) % MOD
            print(f"{i=} {x=} {y=} {z=}")
            soln = (soln + z) % MOD
        return soln


def test_1():
    nums = [3, 4, 4, 9]
    k = 4
    expected = 5
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [8, 12, 6, 15, 16, 1, 12, 20, 3, 1, 6, 11, 20, 10, 11, 13, 14, 8, 9, 10]
    k = 10
    expected = 262
    assert Solution().solve(nums, k) == expected