"""
binarysearch.com :: Trailing Zeros
jramaswami
"""
class Solution:
    def solve(self, k):
        # Let N be the LCM of the numbers in [1..k].  We want to know how
        # many trailing zeros there are in N.  A trailing zero will occur
        # for every 5 that divides N that can be paired with a power of
        # 2 that divides N.  So let 2^a be the largest power of 2 that is
        # less than k and 5^b be the largest power of 5 that is less than N.
        # There will be b trailing zeros because b < a.
        # The maximum k is 1,000,000,000.  The maximum b such that 5^b < k
        # is 12.  A binary search for the answer would be efficient but with
        # a limit of 12 a loop is fine.
        soln = 0
        for exp in range(0, 13):
            n = pow(5, exp)
            if n <= k:
                soln = max(soln, exp)
        return soln






def test_1():
    assert Solution().solve(4) == 0


def test_2():
    assert Solution().solve(5) == 1
