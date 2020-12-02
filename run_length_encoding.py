"""
binarysearch.com :: Run-Length Encoding
https://binarysearch.com/problems/Run-Length-Encoding
"""
class Solution:
    def solve(self, s):
        encoding = []
        prev = s[0]
        curr_length = 0
        for c in s:
            if c == prev:
                curr_length += 1
            else:
                encoding.append(str(curr_length))
                encoding.append(prev)
                prev = c
                curr_length = 1

        encoding.append(str(curr_length))
        encoding.append(prev)
        return "".join(encoding)

def test_1():
    s = "AAAABBBCCDAA"
    solver = Solution()
    assert solver.solve(s) == "4A3B2C1D2A"

def test_2():
    s = "ABCDE"
    solver = Solution()
    assert solver.solve(s) == "1A1B1C1D1E"

def test_3():
    s = "AABBA"
    solver = Solution()
    assert solver.solve(s) == "2A2B1A"

def test_4():
    s = "AAAAAAAAAA"
    solver = Solution()
    assert solver.solve(s) == "10A"
