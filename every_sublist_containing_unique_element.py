"""
binarysearch.com :: Every Sublist Containing Unique Element
jramaswami

REF: https://www.tutorialspoint.com/program-to-check-every-sublist-in-a-list-containing-at-least-one-unique-element-in-python
"""


import collections


class Solution:
    def solve(self, nums):
        def check(left, right):
            # Base Case.
            if left >= right:
                return True

            freqs = collections.Counter(nums[left:right+1])
            min_freq = min(freqs.values())
            if min_freq > 1:
                return False
            # Find a unique elements and check that subarrays excluding
            # those elements have a unique element.
            t = left
            for i, n in enumerate(nums[left:right+1], start=left):
                if freqs[n] == 1:
                    if not check(t, i-1):
                        return False
                    t = i + 1
            return check(t, right)

        return check(0, len(nums)-1)


def test_1():
    nums = [0, 2, 4, 2, 0]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [2, 2, 0]
    expected = False
    assert Solution().solve(nums) == expected