"""
binarysearch.com :: Austin Powers
https://binarysearch.com/problems/Austin-Powers
"""
def count_bits(n):
    result = 0
    while n:
        if n & 1:
            result += 1
        n = n >> 1
    return result


class Solution:
    def solve(self, n):
        return count_bits(n) == 1


def test_1():
    assert Solution().solve(0) == False

def test_2():
    assert Solution().solve(1) == True

def test_3():
    assert Solution().solve(2) == True

def test_4():
    assert Solution().solve(3) == False

