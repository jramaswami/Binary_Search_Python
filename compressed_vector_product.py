"""
binarysearch.com :: Compressed Vector Product
jramaswami
"""
class Solution:
    def solve(self, a, b):
        a_ptr = 0
        b_ptr = 0

        soln = 0
        while a_ptr < len(a) and b_ptr < len(b):
            # Get the minimum amount that we can do in one chunk.
            m = min(a[a_ptr], b[b_ptr])
            # Do that one chunk which will be m * (a' * b')
            soln += m * (a[a_ptr + 1] * b[b_ptr + 1])
            # Now, subtract from the run length.
            a[a_ptr] -= m
            b[b_ptr] -= m
            # Advance any empty run lengths
            if a[a_ptr] == 0:
                a_ptr += 2
            if b[b_ptr] == 0:
                b_ptr += 2
        
        print(a_ptr, a, b_ptr, b, soln)
        return soln


def test_1():
    a = [4, 1, 5, 2]
    b = [9, 2]
    assert Solution().solve(a, b) == 28
