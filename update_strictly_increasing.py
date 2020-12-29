"""
binarysearch.com :: Update List to Make It Strictly Increasing
"""
from math import inf


class Solution:
    def solve(self, A, B):
        dp = [[inf for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
        for i in range(len(B) + 1):
            dp[i][0] = 0

        for i in range(len(dp[0])-1):
            for j in range(len(dp)):
                if i == 0:
                    curr_val = -inf
                else:
                    if j == len(B):
                        curr_val = A[i-1]
                    else:
                        curr_val = B[j]
                if dp[j][i] != inf:
                    for k in range(len(dp)):
                        if k == len(B):
                            next_val = A[i]
                            ops = 0
                        else:
                            next_val = B[k]
                            ops = 1

                        if curr_val < next_val:
                            dp[k][i+1] = min(dp[k][i+1], dp[j][i] + ops)

        soln = min(row[-1] for row in dp)
        return (soln if soln != inf else -1)


def test_1():
    a = [9, 1, 3, 6, 4]
    b = [7, 0, 3]
    assert Solution().solve(a, b) == 2

def test_2():
    a = [0, 0]
    b = [0]
    assert Solution().solve(a, b) == -1
