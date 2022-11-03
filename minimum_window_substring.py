"""
binarysearch.com :: Minimum Window Substring
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, A, B):
        reqd = collections.defaultdict(int)
        for c in B:
            reqd[c] += 1

        freqs = collections.defaultdict(int)
        window = collections.deque()
        soln = math.inf
        for c in A:
            freqs[c] += 1
            window.append(c)

            while window and freqs[window[0]] > reqd[window[0]]:
                freqs[window[0]] -= 1
                window.popleft()

            if all(freqs[x] >= reqd[x] for x in reqd):
                soln = min(soln, len(window))

        return -1 if soln == math.inf else soln


def test_1():
    a = "qthequickbrownfox"
    b = "qown"
    expected = 10
    assert Solution().solve(a, b) == expected
