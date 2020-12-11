"""
binarysearch.com :: Weekly Contest 33 :: Unique String Split
"""
class Solution:
    def solve(self, s):
        soln = 0
        for b in range(1, len(s)-1):
            for c in range(b+1, len(s)):
                A = s[:c]
                B = s[b:]
                C = s[c:] + s[:b]
                if A != B and B != C and A != C:
                    soln += 1
        return soln


def test_1():
    s = "abba"
    solver = Solution()
    assert solver.solve(s) == 3


def test_2():
    s = "aaaa"
    solver = Solution()
    assert solver.solve(s) == 0
