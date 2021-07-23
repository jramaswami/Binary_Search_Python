"""
binarysearch.com :: Matrix Search
jramaswami
"""


class Solution:
    def solve(self, matrix, k):
        k += 1
        r = len(matrix) - 1
        c = len(matrix[r]) - 1
        p = (r + 1) * (c + 1)
        while p != k:
            print(f"{r=} {c=} {p=}")
            # If moving to the left and up will point to p0th item.
            p0 = r * c

            if k <= p0:
                # If k <= p0 then go ahead and move up and left.
                r -= 1
                c -= 1
                p = p0
            else:
                # If k > p0 then the kth item is in this row. But it is to the
                # left.
                p -= 1
                c -= 1

        return matrix[r][c]


def test_1():
    matrix = [
        [1, 3, 30],
        [2, 3, 31],
        [5, 5, 32]
    ]
    k = 4
    expected = 5
    for row in matrix:
        print(row)
    assert Solution().solve(matrix, k) == expected


def test_2():
    matrix = [
        [1, 2, 3]
    ]
    k = 0
    expected = 1
    assert Solution().solve(matrix, k) == expected

def test_3():
    matrix = [
        [1],
        [2],
        [3]
    ]
    k = 2
    expected = 3
    assert Solution().solve(matrix, k) == expected
