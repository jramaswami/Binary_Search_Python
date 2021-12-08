"""
binarysearch.com :: Sort By Permutation
jramaswami
"""


class Solution:
    def solve(self, lst, p):
        i = 0
        while i < len(lst):
            if i == p[i]:
                i += 1
            else:
                j = p[i]
                p[i], p[j] = p[j], p[i]
                lst[i], lst[j] = lst[j], lst[i]
        return lst
