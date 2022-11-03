"""
binarysearch.com :: ASCII String to Integer
jramaswami
"""
class Solution:
    def solve(self, s):
        ssum = 0
        lsum = 0
        for c in s:
            if c.isdigit():
                lsum *= 10
                lsum += int(c)
            else:
                ssum += lsum
                lsum = 0

        ssum += lsum
        return ssum


def test_1():
    s = "11aa32bbb5"
    assert Solution().solve(s) == 48

def test_2():
    s = "abc"
    assert Solution().solve(s) == 0

def test_3():
    s = "1a2b30"
    assert Solution().solve(s) == 33
