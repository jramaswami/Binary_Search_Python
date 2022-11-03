"""
binarysearch.com :: Edit Distance Sequel
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, source, target):
        dp = [[math.inf for _ in range(len(source)+1)] for _ in range(len(target)+1)]
        dp[0][0] = 0
        for c, s in enumerate(source):
            for r, t in enumerate(target):
                # Characters are the same, advance both pointers.
                if s == t:
                    dp[r+1][c+1] = min(dp[r+1][c+1], dp[r][c])
                else:
                    # You can insert the character at t.
                    dp[r+1][c] = min(dp[r+1][c], dp[r][c] + 1)
                    # You can delete the character at s.
                    dp[r][c+1] = min(dp[r][c+1], dp[r][c] + 1)

        for r, _ in enumerate(target[:-1]):
            dp[r+1][-1] = min(dp[r+1][-1], dp[r][-1] + 1)
        for c, _ in enumerate(dp[-1][:-1]):
            dp[-1][c+1] = min(dp[-1][c+1], dp[-1][c] + 1)


        for row in dp:
            print(row)

        soln = []
        r, c = len(dp) - 1, len(dp[-1]) - 1
        while r > 0 or c > 0:
            if r - 1 >= 0 and c - 1 >= 0:
                if dp[r-1][c] < dp[r][c]:
                    soln.append(f"+{target[r-1]}")
                    r, c = r-1, c
                elif dp[r-1][c-1] == dp[r][c]:
                    soln.append(source[c-1])
                    r, c = r-1, c-1
                elif dp[r][c-1] < dp[r][c]:
                    soln.append(f"-{source[c-1]}")
                    r, c = r, c-1
                else:
                    raise Exception(f"There is no move from {r}, {c}")
            elif r - 1 < 0:
                soln.append(f"-{source[c-1]}")
                r, c = r, c-1

            elif c - 1 < 0:
                soln.append(f"+{target[r-1]}")
                r, c = r-1, c
        return soln[::-1]

def test_1():
    source = "aab"
    target = "abb"
    expected = ["a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_2():
    source = "aaab"
    target = "aabb"
    expected = ["a", "a", "-a", "b", "+b"]
    result = Solution().solve(source, target)
    assert result == expected


def test_3():
    source = "abc"
    target = "cba"
    expected = ["-a", "-b", "c", "+b", "+a"]
    result = Solution().solve(source, target)
    assert result == expected


def test_4():
    source = "bcd"
    target = "acd"
    expected = ["-b", "+a", "c", "d"]
    result = Solution().solve(source, target)
    assert result == expected


def test_5():
    "WA"
    source = "aa"
    target= "ba"
    expected = ['-a', '+b', 'a']
    result = Solution().solve(source, target)
    assert result == expected


def test_6():
    "WA"
    source = "acc"
    target = "ba"
    expected = ["+b", "a", "-c", "-c"]
    result = Solution().solve(source, target)
    assert result == expected

# def test_x():
#     source = 'gqhdausadyfsozuerncognjgsbazlfbnwyutaxhwbusxpfgpsjpfgqayemzzwbchaamqfyxllsbgbkuevqgkliimruqhkldjonenmtfnwxvjfuofobfwjgmbcsukpfzputjektrafkqfkidnwtwahwqgkznmqftowhpxlcafsnzycphhgknieqrjrnueqmeagmtneecrzljonmuymvsbcacwhqdcxzooyksrthmctjcolkjeivhngctxclbfxldiqjsagamsgmygehhrawonryyrkppptmgamwmxbgeywrlzxktshllneifspcqseditfflozhprlnlhdgtmtzclgxsaxlhayrrzfgrgkzfstaftoewrrtgbsrwmjnlboobgudebvtufjltchewhshlwpnksdkgjnolavujhstmrtgddopixwezsxypebxpqwviricvfngazhealbjjfbfucfrxyktlznyzsgtqslewxcjiakuboxllx'
#     target = 'ehcotggthvxzcwyjgqsisocwwwlamqjfnyfjxzmctgkdswftzytnzhnlnqoyjlrqwiganwwbgdufrbwjkyhydcgqwpwfspglxvsfrphoyznlfuacqvastsjqvwpprjxmgaqphamtkgbuwjbyvvadwuworfhzecydzzlljwmxubrftbfiybsidoxexzqfidxufpgbhtfvggsskwndbiaslrwhehlabscdghjuqhapcecndkfqtjnwuitgydopmarwcxaytrazqhraqstnwoxfjitddgsbkvlbutgxqlamirsfohopjazqktlhzhozboacvtknnnguscydtihechmrelmxwamoroihfxdoogktggmjybmzwahzwvyuzuhwuvethlfspphuhimoousrbjcetarhwmxgnbowdwpncoxehwsrbxjrzcxxxpammtttuohmtgryzqdqefcjyunobivcjpthvqiplzomdwdhafzwqxaamsfovugm'
#     expected = ["-b", "+a", "c", "d"]
#     result = Solution().solve(source, target)
#     assert result == expected
