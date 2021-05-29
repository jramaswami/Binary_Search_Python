"""
binarysearch.com :: Manipulate Bits To Zero
jramaswami
"""


from collections import deque
from math import inf


def op1(n):
    """Op 1: Set the rightmost bit to either 0 or 1"""
    if n & 1:
        # Set rightmost bit to 0
        n = n & (~1)
    else:
        # Set rightmost bit to 1
        n = n | 1
    return n


def get_lsb(n):
    """Return index of least significant bit."""
    return (n & -n).bit_length() - 1


def op2(n):
    """
    Op 2: Set an ith bit if (i - 1)st bit is 1 and (i - 2)nd to 0th
    bits are all set to 0.
    """
    lsb = get_lsb(n)
    mask = 1 << (lsb + 1)
    if n & mask:
        # right_bit + 1 is set, turn it off
        n = n & (~mask)
    else:
        # right_bit + 1 is not set, turn it on
        n = n | mask
    return n


class Solution:
    def solve(self, num):
        pow2 = set([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,
                    16384,32768,65536,131072,262144,524288,1048576,
                    2097152,4194304,8388608,16777216,33554432,
                    67108864,134217728,268435456,536870912,1073741824,
                    2147483648,4294967296,8589934592])
        visited = set()
        queue = deque()
        queue.append((num, 0))
        visited.add(num)
        soln = inf
        while queue:
            n0, ops = queue.popleft()
            if ops > soln:
                pass
            elif n0 == 0:
                soln = min(soln, ops + 1)
            elif n0 in pow2:
                soln = min(soln, ops + ((2 * n0) - 1))
            else:
                n = n0
                n = op1(n)
                if n not in visited:
                    queue.append((n, ops + 1))
                    visited.add(n)

                n = n0
                n = op2(n)
                if n not in visited:
                    queue.append((n, ops + 1))
                    visited.add(n)

        return soln


def test_1():
    assert Solution().solve(6) == 4


def test_2():
    assert Solution().solve(3) == 2


def test_3():
    assert Solution().solve(174781) == 209705


def test_4():
    """TLE"""
    n = 2147483647
    assert Solution().solve(n) == 209705
