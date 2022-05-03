"""
binarysearch.com :: Run-Length Decoding
jramaswami
"""


class Solution:

    def solve(self, S):
        soln = []
        i = 0
        while i < len(S):
            # Read number.
            freq = 0
            while S[i].isdigit():
                freq = (freq * 10) + int(S[i])
                i += 1
            char = S[i]
            i += 1
            soln.append(freq * char)
        return "".join(soln)


def test_1():
    s = "4a3b2c1d2a"
    expected = "aaaabbbccdaa"
    assert Solution().solve(s) == expected


def test_2():
    s = "10a22b7c1d42e"
    expected = (10 * 'a') + (22 * 'b') + (7 * 'c') + 'd' + (42 * 'e')
    assert Solution().solve(s) == expected
