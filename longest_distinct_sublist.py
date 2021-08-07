"""
binarysearch.com :: Longest Distinct Sublist
jramaswami
"""


import collections


class Solution:
    def solve(self, nums):
        # This can be done with two pointers, but is a little simpler using
        # the deque.
        Q = collections.deque()
        freqs = collections.defaultdict(int)
        soln = 0
        for n in nums:
            freqs[n] += 1
            Q.append(n)
            while freqs[n] > 1:
                r = Q.popleft()
                freqs[r] -= 1
            soln = max(soln, len(Q))
        return soln



def test_1():
    nums = [5, 1, 3, 5, 2, 3, 4, 1]
    expected = 5
    assert Solution().solve(nums) == expected
