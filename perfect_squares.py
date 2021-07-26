"""
binarysearch.com :: Perfect Squares
jramaswami
"""

class Solution:
    def solve(self, n):
        # Lagrange's four-square theorem states that all natural numbers can
        # be expressed as the sum of four perfect squares.  So, our maximum
        # solution is 4.

        # Get a list of perfect squares <= 1
        # There are 317 squares less than or equal to 100,000, the maximum n.
        i = 1
        squares = set()
        while i * i <= n:
            squares.add(i * i)
            i += 1

        # If n is in our set of squares, the solution is 1.
        if n in squares:
            print('n is a perfect square')
            return 1

        # Get the sum of two squares.  This is a most O(317^2) approx 100,500.
        sum_of_squares = set()
        for a in squares:
            for b in squares:
                sum_of_squares.add(a + b)
                # If a + b is n then the answer is 2.
                if a + b == n:
                    return 2

        for a_plus_b in sum_of_squares:
            # if n is the sum of three squares then
            # a + b + c = n
            # c = n - (a + b)
            # If n - (a + b) or c is in our set of squares, then the
            # solution is 3.
                if n - a_plus_b in squares:
                    return 3
        # We have exausted the possibilities of 1, 2, or 3 squares summing
        # to n, so by Lagrange's theorem, the answer is 4.
        return 4


def test_1():
    assert Solution().solve(4) == 1


def test_2():
    assert Solution().solve(17) == 2


def test_3():
    assert Solution().solve(18) == 2


def test_4():
    assert Solution().solve(100000) == 2