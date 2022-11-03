"""
binarysearch.com :: Shortest Window Substring in Order
"""
from math import inf


class Solution:
    def solve(self, s):
        ord_a = ord('a')
        last = [-1 for _ in range(26)]
        soln = inf
        for i, c in enumerate(s):
            if c == 'a':
                last[0] = i
            elif c == 'z':
                if last[ord(c) - ord_a - 1] >= 0:
                    soln = min(soln, i - last[ord(c) - ord_a - 1] + 1)
            else:
                if last[ord(c) - ord_a - 1] >= 0:
                    last[ord(c) - ord_a] = last[ord(c) - ord_a - 1]

        if soln == inf:
            return -1
        else:
            return soln

def test_1():
    assert Solution().solve("aaaaabbbcdefghijklmnopqrstuvwxyzzz") == 28

def test_2():
    assert Solution().solve("zyxwvutsrqponmlkjihgfedcba") == -1
