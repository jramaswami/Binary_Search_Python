"""
binarysearch.com :: Furthest from Origin
jramaswami
"""
class Solution:
    def solve(self, s):
        posn = 0
        qns = 0
        for c in s:
            if c == 'L':
                posn -= 1
            elif c == 'R':
                posn += 1
            elif c == '?':
                qns += 1

        return abs(posn) + qns


def test_1():
    assert Solution().solve(s = "LLRRR??") == 3
