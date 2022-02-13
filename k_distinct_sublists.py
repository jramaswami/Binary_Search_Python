"""
binarysearch.com :: K-Distinct Sublists
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):

        def at_most(x):
            """
            Return the number of sublists that have at most x unique elements.
            """
            result = 0
            window = collections.deque()
            unique_elements = 0
            freqs = collections.defaultdict(int)
            for n in nums:
                window.append(n)
                freqs[n] += 1
                if freqs[n] == 1:
                    unique_elements += 1

                while unique_elements > x:
                    rm = window.popleft()
                    freqs[rm] -= 1
                    if freqs[rm] == 0:
                        unique_elements -= 1

                result += len(window)
            return result

        return at_most(k) - at_most(k-1)


def test_1():
    nums = [1, 1, 2, 3]
    k = 2
    expected = 3
    assert Solution().solve(nums, k) == expected
