"""
binarysearch.com :: Compress String
https://binarysearch.com/problems/Compress-String
"""
class Solution:
    def solve(self, s):
        t = []
        for c in s:
            if not t or t[-1] != c:
                t.append(c)
        return "".join(t)


def test_1():
    s = "aaaaaabbbccccaaaaddf"
    solver = Solution()
    assert solver.solve(s) == "abcadf"

def test_2():
    s = "a"
    solver = Solution()
    assert solver.solve(s) == "a"

def test_3():
    s = ""
    solver = Solution()
    assert solver.solve(s) == ""
