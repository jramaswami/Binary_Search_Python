"""
binarysearch.com :: Cut Ribbons of Same Length
jramaswami
"""
from math import inf


def binary_search(ribbons, k):
    """Binary search for the answer."""
    low = 1
    high = ribbons[-1]
    soln = -inf
    Z = 0
    while low <= high:
        Z += 1
        if Z > 100:
            break
        mid = low + ((high - low) // 2)
        rs = sum(r // mid for r in ribbons)
        if rs >= k:
            soln = max(soln, mid)
            low = mid + 1
        else:
            high = mid - 1
    return soln


class Solution:
    def solve(self, ribbons, k):
        ribbons.sort()
        soln = binary_search(ribbons, k)
        return -1 if soln == -inf else soln


def test_1():
    ribbons = [1, 2, 3, 4, 9]
    k = 5
    assert Solution().solve(ribbons, k) == 3


def test_2():
    ribbons = [8]
    k = 4
    assert Solution().solve(ribbons, k) == 2


def test_3():
    ribbons = [3]
    k = 1
    assert Solution().solve(ribbons, k) == 3


def main():
    """Main method to do some testing of very large arrays."""
    import random
    N = 100000
    ribbons = [random.randint(1, 100000) for _ in range(N)]
    k = random.randint(1, 100000)
    print(Solution().solve(ribbons, k))

    ribbons = [1] * 100000
    k = 100005
    print(Solution().solve(ribbons, k))


if __name__ == '__main__':
    main()
