"""
binarysearch.com :: Cut Rods For Profit
jramaswami
"""

import math

class Solution:
    def solve(self, rod_lens, profit_per_len, cost_per_cut):

        soln = 0
        if rod_lens:
            stop = 1 + max(rod_lens)

            for rl in range(1, stop):
                result = 0
                for rod in rod_lens:
                    q, r = divmod(rod, rl)
                    if r:
                        cuts = rods = q
                    else:
                        cuts = q - 1
                        rods = q
                    cost = cuts * cost_per_cut
                    gross = rods * profit_per_len * rl
                    profit = gross - cost
                    result += max(0, profit)
                soln = max(result, soln)

        return soln


def test_1():
    rod_lens = [5, 8]
    profit_per_len = 6
    cost_per_cut = 4
    assert Solution().solve(rod_lens, profit_per_len, cost_per_cut) == 64
