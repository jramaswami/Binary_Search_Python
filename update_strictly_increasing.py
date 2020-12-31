"""
binarysearch.com :: Update List to Make It Strictly Increasing
jramaswami
"""
from math import inf
from bisect import bisect_left, bisect_right


# From Python docs.
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return i
    return None


class Solution:
    def solve(self, A, B):
        B = sorted(set(B))
        dp = [[inf for _ in A] for _ in range(len(B)+1)]
        # Col-wise index
        for curr_index in range(len(A)):
            # Row-wise index
            curr_val = A[curr_index]
            for prev_index in range(len(B)+1):
                ops = 0
                if curr_index > 0:
                    ops = dp[prev_index][curr_index-1]

                if curr_index == 0:
                    prev_val = -inf
                elif prev_index == len(B):
                    prev_val = A[curr_index-1]
                else:
                    prev_val = B[prev_index]

                if curr_val > prev_val:
                    # We do not have to change it.
                    dp[len(B)][curr_index] = min(dp[len(B)][curr_index], ops)
                # We can change it to the next highest value
                index0 = find_gt(B, prev_val)
                if index0 is not None and ops + 1 <= len(B):
                    dp[index0][curr_index] = min(dp[index0][curr_index], ops + 1)

        soln =  min(row[-1] for row in dp)
        if soln == inf: 
            return -1
        else:
            return soln


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

def test_6():
    a = [0, 2, 2]
    b = [0]
    assert Solution().solve(a, b) == -1

def test_7():
    a = [1, 2, 2]
    b = [1, 0]
    assert Solution().solve(a, b) == 2

