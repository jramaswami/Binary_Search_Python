"""
binarysearch.com :: K Distinct Window
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):
        window = collections.deque(nums[:k])
        freqs = collections.Counter(nums[:k])
        soln = [len(freqs)]
        for n in nums[k:]:
            freqs[window[0]] -= 1
            if freqs[window[0]] == 0:
                del freqs[window[0]]
            window.popleft()
            window.append(n)
            freqs[n] += 1
            soln.append(len(freqs))
        return soln


def test_1():
    nums = [1, 1, 2, 2, 3]
    k = 2
    expected = [1, 2, 1, 2]
    assert Solution().solve(nums, k) == expected
