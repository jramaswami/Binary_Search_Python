"""
binarysearch.com :: Unique Characters of Every Substring
jramaswami
"""


import collections


MOD = pow(10, 9) + 7


class Solution:

    def solve(self, S):
        def count_unique_chars(l, r):
            freqs = collections.Counter(S[l:r+1])
            return sum(1 if v == 1 else 0 for v in freqs.values())

        soln = 0
        for l, _ in enumerate(S):
            for r, _ in enumerate(S[l:], start=l):
                soln = (soln + count_unique_chars(l, r)) % MOD
        return soln



def test_1():
    s = "aab"
    expected = 6
    assert Solution().solve(s) == expected


def test_2():
    "TLE"
    s = "amhjlzxrafkttezhlxiodvcoqultfdpqhisqvzqshfbnqpawsrwktdgwfjoapdntevcqudvsafmialicdtitciufkeqlebbwiahsbtgayvgahaqwwvlefybzswrnmgugjngnthurtfhrgkdmbbkshphektiddijnqbzlvufccfcfxdqsvyednhesvtgfzrtyvhbqpnbzqbpsmjuqmhpuypicllmhacijsoelsleymntxkotllmengyvnhuvbolcbwcjzxjxhplazkzzpfgftumaqqpoqolihnooetsmuhafcjcmjvmlbftzbtkxvhggszzutaxipeeqmifgirukpwcxjacxquknysjhnfiprsoniuumecrceoivibzgtfnclthaogxvdjndreacjmwccohscfqmpkofvtbfqkkgbrgpokkqwmcctvzsdgvwbpomwkfvnxrlrfnkxfieoogjudonmmkjzhpyhqkpznycoghwltvnyxexvwrwldieycbpgmkmwimvbjbqyhbpagbbcmatewcaieskdmmjixuqmwirijrhnpjbytvmhkdvvcffczbwdjzsfxazfkcntsoonfvfhjamflilmyuqugsyqbuirrlonjzuzkllyjztvgxpplobxboaphanyaldzslqqowtfripepetzemrbiktpvbuqnwjazerdfxqdxpayvtscvkyizfdrqmvchtephzqxpqwvvisxkrdeqypwzxkuyrdvagfjovciytg"
    expected = 457278
    assert Solution().solve(s) == expected
