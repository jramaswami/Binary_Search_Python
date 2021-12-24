"""
binarysearch.com :: Beer Bottles
jramaswami
"""


class Solution:
    def solve(self, full):
        drink = 0
        empty = 0
        while full:
            drink += full
            empty += full
            full, empty = divmod(empty, 3)
        return drink
