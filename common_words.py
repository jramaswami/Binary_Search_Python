"""
binarysearch.com :: Common Words
jramaswami
"""


class Solution:
    def solve(self, s0, s1):
        t0 = set(w.lower() for w in s0.split())
        t1 = set(w.lower() for w in s1.split())
        return len(t0 & t1)