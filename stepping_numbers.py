"""
binarysearch.com :: Stepping Numbers
jramaswami
"""
from functools import reduce


MOD = pow(10, 9) + 7


class Solution:
    def solve(self, N):
        if N == 1:
            return 10

        # Can start number with digits 1-9
        prev_row = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        curr_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for row in range(1, N):
            for digit in range(10):
                # -1
                if digit - 1 >= 0:
                    curr_row[digit - 1] = (curr_row[digit - 1] + prev_row[digit]) % MOD
                # +1
                if digit + 1 <= 9:
                    curr_row[digit + 1] = (curr_row[digit + 1] + prev_row[digit]) % MOD
            prev_row, curr_row = curr_row, prev_row
            # Reset curr_row
            for i in range(10):
                curr_row[i] = 0


        return reduce(lambda a, x: (a + x) % MOD, prev_row, 0)



def test_1():
    assert Solution().solve(2) == 17

def test_2():
    assert Solution().solve(100000) == 875922579

def test_3():
    assert Solution().solve(1) == 10
