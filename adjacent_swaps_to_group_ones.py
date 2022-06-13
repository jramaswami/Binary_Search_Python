"""
binarysearch.com :: Adjacent Swaps to Group Ones
jramaswami
"""


class Solution:
    def solve(self, s):
        # Count how many ones a zero would have to swap with if it goes
        # left or if it goes right and choose the minimum.
        curr_ones = 0
        prefix = [0 for _ in s]
        for i, _ in enumerate(s):
            if s[i] == '1':
                curr_ones += 1
            prefix[i] = curr_ones
        curr_ones = 0
        suffix = [0 for _ in s]
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                curr_ones += 1
            suffix[i] = curr_ones

        soln = 0
        for c, left, right in zip(s, prefix, suffix):
            if c == '0':
                soln += min(left, right)
        return soln



def test_1():
    s = "0110010"
    expected = 2
    assert Solution().solve(s) == expected
