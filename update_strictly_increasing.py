"""
binarysearch.com :: Update List to Make It Strictly Increasing
jramaswami
"""
from math import inf


class Solution:
    def solve(self, A, B):
        B.sort()
        dp = [[inf for _ in A] for _ in range(len(B) + 1)]

        # The invariant we will keep is that A[i-1] < A[i].

        # You can always replace A[0] with B[i]
        for i in range(len(B)):
            dp[i][0] = 1
        # You can leave A[0] the same.
        dp[-1][0] = 0

        for i, a in enumerate(A):
            # We already did the column.
            if i == 0:
                continue

            min_b_ops = inf
            for j, b in enumerate(B):
                # To keep our invariant, we can replace A[i] with B[j] 
                # if A[i-1] < B[j].

                # If we are going to replace A[i] with B[j]:
                # Looking back, if we replaced A[i-1] with some B, we can
                # replace A[i] with B[j] if A[i-1] is a B that is less then j.
                # We sorted B, so this is true for all B[k] where k < j if
                # B[k] < B[j].
                if B[j-1] < B[j]:
                    # Carry forward the minimum number of ops to replace
                    # A[i] with B[j].  This will be the minimum ops 
                    # for dp[0:j][i] + 1 op for the change to B[j].
                    dp[j][i] = min(dp[j][i], min_b_ops + 1)
                min_b_ops = min(min_b_ops, dp[j][i-1])

                # We can replace A[i] with B[j] if we left A[i-1] unchanged and
                # A[i-1] < B[j].
                if A[i-1] < B[j]:
                    dp[j][i] = min(dp[j][i], dp[len(B)][i-1] + 1)

                # If we are going to leave A[i] unchanged.
                # If A[i] is less than B[j] then we could have replaced
                # A[i-1] with B[j].  So we should carry forward that number
                # of ops + 0 to leaving A[i] unchanged, if A[i] is > B[j]
                if A[i] > B[j]:
                    dp[len(B)][i] = min(dp[len(B)][i], dp[j][i-1])

            # Finally if we left A[i-1] unchanged, we should carry that
            # forward if A[i] > A[i-1]
            if A[i] > A[i-1]:
                dp[len(B)][i] = min(dp[len(B)][i], dp[len(B)][i-1])

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

def test_3():
    a = [1, 0]
    b = [0, 0]
    assert Solution().solve(a, b) == -1 

def test_4():
    a = [1, 0]
    b = [1, 0]
    assert Solution().solve(a, b) == 2

def test_5():
    a = [2, 1, 0]
    b = [1, 0]
    assert Solution().solve(a, b) == -1
