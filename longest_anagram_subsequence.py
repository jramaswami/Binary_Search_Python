"""
binarysearch.com :: Longest Anagram Subsequence
jramswami
"""
from collections import Counter


class Solution:
    def solve(self, A, B):
        ctr_A = Counter(A)
        ctr_B = Counter(B)
        return sum(min(ctr_A[a], ctr_B[a]) for a in ctr_A)


def test_1():
    A = "afbc"
    B = "cxba"
    assert Solution().solve(A, B) == 3
