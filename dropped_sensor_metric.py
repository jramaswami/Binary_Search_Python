"""
binarysearch.com :: Dropped Sensor Metric
jramaswami
"""
class Solution:
    def solve(self, A, B):
        # First, find where A and B differ.
        delta = 0
        for i, (a, b) in enumerate(zip(A, B)):
            if a != b:
                delta = i
                break
        # From here see if A[delta:-1] is the same as B[delta+1:]
        if A[delta:-1] == B[delta+1:]:
            return B[delta]
        else:
            return A[delta]


def test_1():
    A = [1, 2, 3]
    B = [2, 3, 5]
    assert Solution().solve(A, B) == 1

def test_2():
    A = [5, 4, 2, 1, 6]
    B = [5, 4, 3, 2, 1]
    assert Solution().solve(A, B) == 3
