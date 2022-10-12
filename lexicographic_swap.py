"""
binarysearch.com :: Lexicographic Swap
jramaswami
"""


class Solution:

    def solve(self, s):
        # Find first non-a character.
        x = len(s)
        a = 'z'
        for i, c in enumerate(s):
            if c != 'a':
                x = i
                a = c
                break
        # Find the next smallest letter.
        y = len(s)
        for i, c in enumerate(s[x+1:], start=x+1):
            if ord(c) < ord(a):
                y = i
                a = c
        if y == len(s):
            return s
        # Swap these two.
        t = list(s)
        t[x], t[y] = t[y], t[x]
        return "".join(t)



def test_1():
    s = "cbca"
    expected = "abcc"
    assert Solution().solve(s) == expected


def test_2():
    s = "aaaaa"
    expected = s
    assert Solution().solve(s) == expected


def test_3():
    s = "aaaab"
    expected = s
    assert Solution().solve(s) == expected


def test_4():
    s = "zxxxaxxxx"
    expected = "axxxzxxxx"
    assert Solution().solve(s) == expected

def test_5():
    "WA"
    s = "yxxwvttnnhffedaa"
    expected = "axxwvttnnhffeday"
    assert Solution().solve(s) == expected