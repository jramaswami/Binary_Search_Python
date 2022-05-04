"""
binarysearch.com :: Unique Characters of Every Substring
jramaswami


REF: https://www.youtube.com/watch?v=eN8zATT702M
"""


import string


MOD = pow(10, 9) + 7


class Solution:

    def solve(self, S):
        # Record the indexes (1-based) for every letter.
        # Include 0 for the left and the end of the array for the right.
        dp = {c: [0] for c in string.ascii_lowercase}
        for i, c in enumerate(S):
            dp[c].append(i+1)
        for c in string.ascii_lowercase:
            dp[c].append(len(S)+1)

        # For each index, determine the number of substrings for which it
        # will be the only occurrence.  The is the same as the number of
        # substrings between the previous occurrence and next ocurrence.
        # (Or start or end of the array if there isn't a previous or next
        # occurrence).
        soln = 0
        for c in string.ascii_lowercase:
            if len(dp[c]) > 2:
                for i in range(1, len(dp[c])-1):
                    k = ((dp[c][i] - dp[c][i-1]) * (dp[c][i+1]- dp[c][i])) % MOD
                    soln = (soln + k) % MOD
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


def test_3():
    "TLE"
    s = "aufohslfhlbzekgzshgjrycraeuqakddlwzauassvrjsebafjtsyftqhxyauviwmqytjkkcbynjfdxzbuoltrapvtpjniqsqvdqvkfwvusilbointpcjqlkanbjdtnwvsgximmnqarxmglbtenusdkhxcwgpcliqfrhtogygynfbmxqqlakiozzcggefsczsspahggyipulqrcfmbnjhzulomluqmpzdybnurakwnketbgfdwojjbcstamgcxlhjsptbgjotjdmbcoodmxqejqttoumollbxurvanlsyrznqtypwimxfcxlzglhszvuswzrciqwizmaevqhuktaenwavcoxyatdakqlqkehuxyhixgypvxiufcagzujzhtbvqsssjdtsfwouccxzivduysshswnhcpceaczflprixnpusmuwuovceqgnnbuzzurerxhanmyvcudovypwhpjdrlsuknkuczjehocnyggoqljyvsvezopghhxsvcchjmtifqxvggnlqiicmkgbhvineidycgvdcztmkhewhcdqdmnmdoghumavxxesrijmzkxgwiutlunderfjogjfadlisrgvbhwgtuwyavvqricsiduthpixipltzogbwvqopocivpannlayriobeoisqnbyzcliobqvhnjwmtonmwznhecfotuanbuhotnmggbbufwehaivwlbyyvuaywnnolirlehcyjgkafolirjpdqolmslmwrtrxswoprtaqmpxyegcwwamnvohomdaihtjuphzhrbfaqzfuunybkwcxsbsnwqondglnmhkgzabivmfessnwxntixnukxalitaxrfwyljlefzrcjmprekesqmhskpauglihmglbggbjctrzsskeluwymmhebzcfdjojhvxnmvhvqoesrxnsvhnvvwmpxkn"
    expected = 603477
    assert Solution().solve(s) == expected


def test_4():
    s = "aaabbb"
    expected = 12
    assert Solution().solve(s) == expected
