"""
binarysearch.com :: Half Monotonous String
https://binarysearch.com/problems/Half-Monotonous-String
"""
from itertools import accumulate
from math import inf


class Solution:
    def solve(self, s):
        # Frequency of each character in the half strings.
        lower_half = [0 for _ in range(27)]
        upper_half = [0 for _ in range(27)]
        for i, c in enumerate(s):
            if i < len(s) // 2:
                lower_half[ord(c) - ord('a') + 1] += 1
            else:
                upper_half[ord(c) - ord('a') + 1] += 1

        # Prefix sums to quickly determine number of characters greater than
        # or less than a given character.
        lower_half_prefix = list(accumulate(lower_half))
        upper_half_prefix = list(accumulate(upper_half))

        best_soln = inf
        half_len = len(s) // 2
        for i in range(1, 27):
            # We can:
            # (1) make all lower_half <= i, all upper half > i
            # How many characters in lower half are >= i?  We must
            # change all of them.
            soln1 = (half_len - lower_half_prefix[i])
            # How many characters in upper half are < i?  We must
            # change all of them.
            soln1 += upper_half_prefix[i]
            best_soln = min(best_soln, soln1)
            # (2) make all upper_half > i, all lower half <= i
            # How many characters in upper half are >= i?  We must
            # change all of them.
            soln2 = (half_len - upper_half_prefix[i])
            # How many characters in upper half are < i?  We must
            # change all of them.
            soln2 += lower_half_prefix[i]
            best_soln = min(best_soln, soln2)
            # (3) make all lower_half and upper half == i
            # How many characters in lower half are not i?  We must
            # change all of them.
            soln3 = (half_len - lower_half[i])
            # How many characters in upper half are not i?  We must
            # change all of them.
            soln3 += (half_len - upper_half[i])
            best_soln = min(best_soln, soln3)

        return best_soln


def test_1():
    s = "aa"
    solver = Solution()
    assert solver.solve(s) == 0

def test_2():
    s = "aaabba"
    solver = Solution()
    assert solver.solve(s) == 1

def test_3():
    s = "bccbba"
    solver = Solution()
    assert solver.solve(s) == 1

def test_4():
    s = ""
    solver = Solution()
    assert solver.solve(s) == 0