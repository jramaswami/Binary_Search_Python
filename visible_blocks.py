"""
binarysearch.com :: Visible Blocks
jramaswami

Three states
(1) blocks used (position can be derived from this) (up to 2^15 states).
(2) count of visible blocks so far.
(3) max block so far (determines if new blocks are visible.
"""


import functools


class Solver:

    def __init__(self, block_count, required_visible_blocks):
        self.block_count = block_count
        self.required_visible_blocks = required_visible_blocks

    def solve(self):
        return self._solve(pow(2, self.block_count) - 1, 0, -1)

    @functools.cache
    def _solve(self, unused_blocks, visible_blocks, max_block):

        # If we have too many visible blocks just return 0
        if visible_blocks > self.required_visible_blocks:
            return 0

        # If we don't have enough larger blocks left, stop looking.
        possible_larger_blocks = 0
        for block in range(self.block_count - 1, -1, -1):
            mask = (1 << block)
            if unused_blocks & mask and block > max_block:
                possible_larger_blocks += 1
        if visible_blocks + possible_larger_blocks < self.required_visible_blocks:
            return 0

        if unused_blocks:
            soln = 0

            for block in range(self.block_count - 1, -1, -1):
                mask = (1 << block)
                if unused_blocks & mask:
                    soln += self._solve(
                        unused_blocks & (~mask),
                        visible_blocks + 1 if block > max_block else visible_blocks,
                        max(max_block, block)
                    )
            return soln
        else:
            return 1 if visible_blocks == self.required_visible_blocks else 0


class Solution:
    def solve(self, block_count, required_visible_blocks):
        solver = Solver(block_count, required_visible_blocks)
        return solver.solve()


def test_1():
    n = 4
    k = 2
    expected = 11
    assert Solution().solve(n, k) == expected


def test_2():
    n = 15
    k = 3
    expected = 392156797824
    assert Solution().solve(n, k) == expected


def test_3():
    "TLE"
    n = 13
    k = 1
    expected = 479001600
    assert Solution().solve(n, k) == expected


def test_4():
    "Still TLE"
    n = 13
    k = 6
    expected = 206070150
    assert Solution().solve(n, k) == expected
