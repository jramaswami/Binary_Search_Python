"""
binarysearch.com :: Manipulate Bits To Zero
jramaswami
"""


from collections import deque


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
        visited = set()
        queue = deque()
        queue.append((num, 0))
        visited.add(num)
        while queue:
            n, ops = queue[0]
            n = op1(n)
            if n == 0:
                return ops + 1

            if n not in visited:
                queue.append((n, ops + 1))
                visited.add(n)

            n, ops = queue[0]
            n = op2(n)
            if n == 0:
                return ops + 1

            if n not in visited:
                queue.append((n, ops + 1))
                visited.add(n)
            # Remove n from queue
            queue.popleft()


def test_1():
    assert Solution().solve(6) == 4


def test_2():
    assert Solution().solve(3) == 2


def test_3():
    assert Solution().solve(174781) == 209705


# def test_4():
#     """TLE"""
#     n = 2147483647
#     assert Solution().solve(n) == 209705
