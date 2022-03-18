"""
binarysearch.com :: Repeating Numbers
jramaswmai
"""


import math


class Solution:

    def solve(self, N):
        # Boundary case: there are no repeated digit numbers < 10
        if N < 10:
            return 0

        no_repeats = 0
        # How many digits is N?
        digit_count = len(str(N))
        # Sum the number of numbers *without* repeated digits with less
        # digits than N.
        for d in range(1, digit_count):
            if d == 1:
                # There are ten single digit numbers including zero.
                no_repeats += 10
            else:
                # There are a choice of nine digits for the first digit.
                k = 9
                for i in range(1, d):
                    # For the remaining digits you have a choice of ten digits
                    # less the number of digits already set.
                    k *= (10 - i)
                no_repeats += k
        # Count the numbers *without* repeated digits with the same number
        # of digits as N.
        digits = [int(i) for i in str(N)]
        # Figure out how many digits to the left of the j-th digit are less
        # than the j-th digit.  Also figure out if the digit has been repeated.
        lt = [0 for _ in digits]
        rp = [False for _ in digits]
        for i, a in enumerate(digits):
            for j, b in enumerate(digits[i+1:], start=i+1):
                if a < b:
                    lt[j] += 1
                elif a == b:
                    rp[j] = True

        for d in range(digit_count):
            k = 1
            # How many less than the d-th digit?
            if d == 0:
                # If it is the first digit you can choose from 1 to d-1.
                k *= max(0, (digits[d] - 1))
            else:
                # If it isn't the first digit you can choose 0 to d-1 less
                # the number of set digits that are less than digits[d].
                k *= max(0, (digits[d] - lt[d]))

            for i in range(d+1, digit_count):
                # For the remaining places you can choose 0 to 9 less then
                # number of set digits.
                k *= (10 - i)

            no_repeats += k

            # If setting the d-th digit creates a repeat, stop counting.
            if rp[d]:
                break

        # Finally, is N a non-repeater?
        if (len(set(digits)) == len(digits)):
            no_repeats += 1

        return N - no_repeats + 1


def test_1():
    assert Solution().solve(35) == 3


def test_2():
    assert Solution().solve(111) == 13


def test_3():
    assert Solution().solve(1000) == 262


def test_4():
    N = 72376
    assert Solution().solve(N) == 48172


def test_5():
    N = 0
    assert Solution().solve(N) == 0


def test_6():
    N = 9
    assert Solution().solve(N) == 0


def test_7():
    N = 10
    assert Solution().solve(N) == 0
