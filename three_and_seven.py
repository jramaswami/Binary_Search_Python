"""
binarysearch.com :: 3 and 7
https://binarysearch.com/problems/3-and-7
"""
class Solution:
    def solve(self, n):
        k = 0
        while k <= n:
            if (n - k) == 0:
                return True
            elif (n - k) % 3 == 0:
                return True

            k += 7

        return False

def test_1():
    assert Solution().solve(13) == True

def test_2():
    assert Solution().solve(9) == True

def test_3():
    assert Solution().solve(7) == True


