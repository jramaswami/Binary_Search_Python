"""
binarysearch.com :: Rotation of Another String
https://binarysearch.com/problems/Rotation-of-Another-String
"""
class Solution:
    def solve(self, s0, s1):
        if s0 == "" and s1 == "":
            return True
        s2 = s0 + s0
        for i, _ in enumerate(s2):
            if s2[i:i+len(s0)] == s1:
                return True
        return False

def test_1():
    s0 = "Cattywampus"
    s1 = "sCattywampu"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_2():
    s0 = "Gardyloo"
    s1 = "dylooGar"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_3():
    s0 = "Taradiddle"
    s1 = "diddleTara"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_4():
    s0 = "Snickersnee"
    s1 = "Snickersnee"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_5():
    s0 = ""
    s1 = ""
    solver = Solution()
    assert solver.solve(s0, s1) == True
