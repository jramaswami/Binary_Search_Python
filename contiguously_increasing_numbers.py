"""
binarysearch.com :: Contiguously Increasing Numbers
jramaswami
"""

class Solution:
    def solve(self, start, end):

        def next_number(i):
            return (10 * i) + ((i % 10) + 1)

        MAX_NUM = 123456789

        A = list(range(1, 10))
        soln = list(A)
        while soln[-1] < MAX_NUM:
            B = [next_number(i) for i in A[:-1]]
            soln.extend(B)
            A = B
        return [i for i in soln if i >= start and i <= end]

def test_1():
    start = 0
    end = 100
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89]
    result = Solution().solve(start, end)
    print(result)
    print(expected)
    assert result == expected


def test_2():
    start = 0
    end = pow(2, 31)
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
    result = Solution().solve(start, end)
    assert result == expected
