"""
binarysearch.com :: A Unique String
https://binarysearch.com/problems/A-Unique-String
"""
class Solution:
    def solve(self, s):
        visited = set()
        for c in s:
            if c in visited:
                return False
            visited.add(c)
        return True


def test_1():
    s = "abcde"
    solver = Solution()
    assert solver.solve(s) ==  True

def test_2():
    s = "aab"
    solver = Solution()
    assert solver.solve(s) ==  False

def test_3():
    s = ""
    solver = Solution()
    assert solver.solve(s) ==  True

