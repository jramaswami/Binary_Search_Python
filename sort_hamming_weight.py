"""
binarysearch.com :: Sort List by Hamming Weight
jramaswami
"""
def popcount(x):
    """Return the number of bits set."""
    soln = 0
    while x:
        soln += (1 & x)
        x = (x >> 1)
    return soln
        

class Solution:
    def solve(self, nums):
        nums0 = [(popcount(x), x) for x in nums]
        nums0.sort()
        return [n for _, n in nums0]


def test_1():
    nums = [3, 1, 4, 7]
    assert Solution().solve(nums) == [1, 4, 3, 7]

def test_2():
    nums = [2, 1]
    assert Solution().solve(nums) == [1, 2]

def test_3():
    nums = [2, 8]
    assert Solution().solve(nums) == [2, 8]
