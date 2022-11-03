"""
binarysearch.com :: Weekly Contest 43 :: Kth Largest Pair Product
jramaswami
"""
import heapq


class Solution:
    def solve(self, A, B, K):
        A.sort()
        B.sort()
        Q = []
        left = [0 for _ in B]
        right = [len(A) - 1 for _ in B]

        for j, b in enumerate(B):
            heapq.heappush(Q, (-(b * A[0]), 0, j, 1))
            if len(A) > 1:
                heapq.heappush(Q, (-(b * A[-1]), len(A) - 1, j, -1))

        k = 0
        soln = None
        while k <= K:
            m, i, j, dirn  = heapq.heappop(Q)
            soln = -m
            k += 1
            i += dirn
            if dirn < 0:
                # Moving from right
                right[j] = i
                if i > left[j]:
                    heapq.heappush(Q, (-(B[j] * A[i]), i, j, dirn))
            else:
                # Moving from left
                left[j] = i
                if i < right[j]:
                    heapq.heappush(Q, (-(B[j] * A[i]), i, j, dirn))
        return soln

            
def test_1():
    a = [-2, 4, 3]
    b = [5, 7]
    k = 2
    assert Solution().solve(a, b, k) == 20

def test_2():
    a = [-3, -2, -1]
    b = [3, 2, 1]
    k = 1
    assert Solution().solve(a, b, k) == -2

def test_3():
    a = [-3, 0]
    b = [3, -2, 1]
    k = 3
    assert Solution().solve(a, b, k) == 0

def test_4():
    a = [-1]
    b = [1, 2]
    k = 1
    assert Solution().solve(a, b, k) == -2

def test_5():
    a = [-2, -1]
    b = [-1, -2]
    k = 3
    assert Solution().solve(a, b, k) == 1
