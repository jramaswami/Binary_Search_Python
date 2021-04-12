"""
binarysearch.com :: Sum of Four Numbers Less Than Target
jramaswami
"""
class Solution:
    def solve(self, A, B, C, D, target):
        """Brute force.  Probably too slow."""
        soln = 0
        for a in A:
            for b in B:
                for c in C:
                    for d in D:
                        if a + b + c + d <= target:
                            soln += 1
        return soln


def test_1():
    A = [2, 3]
    B = [5, 2]
    C = [0]
    D = [1, 2]
    target = 6
    assert Solution().solve(A, B, C, D, target) == 3


def test_2():
    A = [1, 1]
    B = [0]
    C = [0]
    D = [0]
    target = 1
    assert Solution().solve(A, B, C, D, target) == 2

