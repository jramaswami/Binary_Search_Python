"""
binarysearch.com :: Subsequence Strings
"""
class Solution:
    def solve(self, s1, s2):
        s1_ptr = 0
        for _, c in enumerate(s2):
            if s1_ptr >= len(s1):
                break
            if s1[s1_ptr] == c:
                s1_ptr += 1

        return s1_ptr >= len(s1)

def test_1():
    s1 = "ppl"
    s2 = "apple"
    solver = Solution()
    solver.solve(s1, s2) == True

def test_2():
    s1 = "ale"
    s2 = "apple"
    solver = Solution()
    solver.solve(s1, s2) == True

def test_2():
    s1 = "elppa"
    s2 = "apple"
    solver = Solution()
    solver.solve(s1, s2) == False
