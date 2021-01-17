"""
binarysearch.com :: Ugly Number
jramaswami
"""

class Solution:
    def solve(self, n):
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1

def test_1():
    assert Solution().solve(10) == True

def test_2():
    assert Solution().solve(14) == False
        
