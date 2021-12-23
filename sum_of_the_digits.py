"""
binarysearch.com :: Sum of the Digits
jramaswami
"""

class Solution:
    def solve(self, num):
        S = 0
        while num:
            num, r = divmod(num, 10)
            S += r
        return S
