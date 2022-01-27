"""
binarysearch.com :: Max XOR of Two Integers
jramaswmai
"""


class TrieNode:

    def __init__(self):
        self.one = None
        self.zero = None

    def add_one(self):
        self.one = TrieNode()

    def add_zero(self):
        self.zero = TrieNode()


class Solution:

    def solve(self, nums):

        # Build Trie.
        root = TrieNode()
        for n in nums:
            curr = root
            for bit in range(32, -1, -1):
                mask = 1 << bit
                if n & mask:
                    if curr.one is None:
                        curr.add_one()
                    curr = curr.one
                else:
                    if curr.zero is None:
                        curr.add_zero()
                    curr = curr.zero

        # Find solution.
        soln = 0
        for n in nums:
            curr = root
            m = 0
            for bit in range(32, -1, -1):
                mask = 1 << bit
                if n & mask:
                    if curr.zero is None:
                        curr = curr.one
                        m |= mask
                    else:
                        curr = curr.zero
                else:
                    if curr.one is None:
                        curr = curr.zero
                    else:
                        curr = curr.one
                        m |= mask
            soln = max(soln, n ^ m)
        return soln


def test_1():
    nums = [1, 2, 3, 7]
    expected = 6
    assert Solution().solve(nums) == expected


def test_2():
    nums = [3,10,5,25,2,8]
    expected = 28
    assert Solution().solve(nums) == expected


def test_3():
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    expected = 127
    assert Solution().solve(nums) == expected


def test_4():
    nums = [8]
    expected = 0
    assert Solution().solve(nums) == expected
