"""
binarysearch.com :: Index Into an Infinite String
jramaswami
"""


class Solution:

    def solve(self, s, i, j):
        return "".join(s[x % len(s)] for x in range(i, j))