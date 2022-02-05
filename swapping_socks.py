"""
binarysearch.com :: Swapping Socks
jramaswami
"""


class Socks:

    def __init__(self, row):
        self.row = row
        self.loc = [0 for _ in row]
        for i, n in enumerate(row):
            self.loc[n] = i

    def swap(self, left, right):
        "Swap the element at index left with element at index right."
        left_val = self.row[left]
        right_val = self.row[right]
        # Swap the row values.
        self.row[left], self.row[right] = self.row[right], self.row[left]
        # Update locations.
        self.loc[left_val] = right
        self.loc[right_val] = left

    def find(self, value):
        "Return the index of the given value."
        return self.loc[value]

    def __getitem__(self, key):
        return self.row[key]

    def is_pair(self, left):
        "Return True if row[left] and row[left+1] are a pair."
        a = min(self.row[left], self.row[left+1])
        b = max(self.row[left], self.row[left+1])
        return a + 1 == b and b % 2

    def __len__(self):
        return len(self.row)


class Solution:

    def solve(self, row):

        def solve0(socks, boundary):
            "Recursive solution."
            if boundary >= len(socks):
                return 0

            if socks.is_pair(boundary):
                return solve0(socks, boundary+2)

            # Make a pair with socks[boundary]
            a = socks[boundary]
            b = a + 1
            if a % 2:
                b = a - 1
            i = socks.find(b)
            socks.swap(boundary+1, i)
            result0 = 1 + solve0(socks, boundary+2)
            socks.swap(boundary+1, i)

            # Make a pair with socks[boundary+1]
            a = socks[boundary+1]
            b = a + 1
            if a % 2:
                b = a - 1
            i = socks.find(b)
            socks.swap(boundary, i)

            result1 = 1 + solve0(socks, boundary + 2)
            socks.swap(boundary, i)
            return min(result0, result1)

        socks = Socks(row)
        return solve0(socks, 0)


def test_1():
    row = [0, 4, 1, 3, 2, 5]
    expected = 2
    assert Solution().solve(row) == expected


def test_2():
    row = [1, 0, 3, 2]
    expected = 0
    assert Solution().solve(row) == expected


def test_3():
    "TLE"
    row = [45, 33, 36, 9, 34, 72, 17, 60, 89, 3, 6, 90, 32, 66, 44, 70, 26, 98, 68, 28, 81, 76, 74, 22, 65, 11, 51, 62, 59, 52, 20, 78, 94, 82, 79, 57, 42, 86, 91, 39, 87, 85, 29, 41, 71, 99, 35, 80, 25, 92, 38, 55, 0, 67, 47, 13, 23, 37, 2, 46, 56, 15, 54, 63, 97, 96, 31, 16, 8, 48, 61, 75, 73, 53, 40, 69, 27, 7, 84, 1, 49, 24, 58, 77, 4, 88, 14, 64, 12, 93, 83, 18, 21, 43, 5, 95, 50, 10, 19, 30]
    expected = 45
    assert Solution().solve(row) == expected
