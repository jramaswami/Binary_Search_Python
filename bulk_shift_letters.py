"""
binarysearch.com :: Bulk Shift Letters
jramaswami
"""
from itertools import accumulate


class Solution():
    def solve(self, s, shifts):
        ord_a = ord('a')
        s0 = [ord(c) - ord_a for c in s]

        for i, shift in enumerate(list(accumulate(reversed(shifts)))[::-1]):
            s0[i] = (s0[i] + shift) % 26

        return "".join(chr(ord_a + c) for c in s0)


def test_1():
    s = "afz"
    shifts = [1, 2, 1]
    assert Solution().solve(s, shifts) == "eia"


def test_2():
    s = "yftozvlzgzwcwjjiixqdcapwowqxyu"
    shifts = [13, 8, 2, 13, 13, 20, 10, 13, 4, 19, 17, 5, 11, 18, 14, 16, 12, 2, 9, 16, 8, 3, 15, 1, 8, 9, 10, 1, 8, 3]
    assert Solution().solve(s, shifts) == "nhngenjnhwapegozjmdhqgskbbmjjx"


def main():
    """Generate random test case."""
    import string
    import random
    N = 30
    s = "".join(random.choice(string.ascii_lowercase) for _ in range(N))
    shifts = [random.randint(1, 20) for _ in range(N)]
    print(s)
    print(shifts)


if __name__ == '__main__':
    main()
