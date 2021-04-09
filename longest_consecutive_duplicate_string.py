"""
binarysearch.com :: Longest Consecutive Duplicate String
jramaswami
"""
class Solution:
    def solve(self, s):
        longest = 0
        curr_char = ''
        curr_streak = 0
        for c in s:
            if curr_char == c:
                curr_streak += 1
                longest = max(curr_streak, longest)
            else:
                curr_streak = 1
                curr_char = c
        return longest


def test_1():
    assert Solution().solve("abbbba") == 4

def test_2():
    assert Solution().solve("aaabbb") == 3

def test_3():
    """WA"""
    assert Solution().solve("a") == 3

