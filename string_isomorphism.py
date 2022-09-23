"""
binarysearch.com :: String Isomorphism
jramaswami
"""


import string


class Solution:

    def solve(self, s, t):
        s_map = {c: None for c in string.ascii_lowercase}
        t_map = {c: None for c in string.ascii_lowercase}
        for x, y in zip(s, t):
            if s_map[x] is None and t_map[y] is None:
                s_map[x] = y
                t_map[y] = x
            elif s_map[x] != y or t_map[y] != x:
                return False
        return True


def test_1():
    s = "coco"
    t = "kaka"
    expected = True
    assert Solution().solve(s, t) == expected


def test_2():
    s = "cat"
    t = "foo"
    expected = False
    assert Solution().solve(s, t) == expected


def test_3():
    s = "hello"
    t = "hello"
    expected = True
    assert Solution().solve(s, t) == expected