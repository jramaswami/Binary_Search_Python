"""
binarysearch.com :: Stepping Numbers
jramaswami
"""
MOD = pow(10, 9) + 7


class Solution:
    def solve(self, N):
        if N == 1:
            return 10

        matrix = [[0 for _ in range(10)] for _ in range(N)]
        # Can start number with digits 1-9
        matrix[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for row in range(1, N):
            for digit in range(10):
                # -1
                if digit - 1 >= 0:
                    matrix[row][digit - 1] = (matrix[row][digit - 1] + matrix[row-1][digit]) % MOD
                # +1
                if digit + 1 <= 9:
                    matrix[row][digit + 1] = (matrix[row][digit + 1] + matrix[row-1][digit]) % MOD

        soln = 0
        for k in matrix[-1]:
            soln = (soln + k) % MOD
        return soln


def test_1():
    assert Solution().solve(2) == 17

def test_2():
    assert Solution().solve(100000) == 875922579

def test_3():
    assert Solution().solve(1) == 10
