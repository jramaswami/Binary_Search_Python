"""
binarysearch.com :: Non-Decreasing Digits
jramaswami
"""


def number_to_rev_list(n):
    """Return numbers as a reversed list of digits."""
    result = []
    while n:
        n, d = divmod(n, 10)
        result.append(d)
    return result


def rev_list_to_number(A):
    """Return reverse list of digits as a number."""
    m = 1
    result = 0
    for k in A:
        result += (m * k)
        m *= 10
    return result


def is_non_increasing(A):
    """Return True if A is non-decreasing."""
    return all(a >= b for a, b in zip(A[:-1], A[1:]))


class Solution:
    def solve(self, n):
        A = number_to_rev_list(n)

        if is_non_increasing(A):
            return n

        B = list(A)
        for i, _ in enumerate(B):
            B[i] -= 1
            # Use non-increasing since we have reversed the number.
            if is_non_increasing(B):
                m = rev_list_to_number(B)
                if m < n:
                    return m
            B[i] = 9


def test_1():
    assert Solution().solve(332) == 299


def test_2():
    assert Solution().solve(9876) == 8999


def test_3():
    assert Solution().solve(9999) == 9999


def test_4():
    assert Solution().solve(9998) == 8999


def test_5():
    assert Solution().solve(1) == 1
