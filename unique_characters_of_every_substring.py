"""
binarysearch.com :: Unique Characters of Every Substring
jramaswami
"""


import string


MOD = pow(10, 9) + 7


class Solution:

    def solve(self, S):
        soln = 0
        dp = [[] for _ in range(len(S) + 1)]
        dp[-1] = [0 for _ in range(26)]

        for r, c in enumerate(S):
            # Initialize curr dp.
            dp[r] = list(dp[r-1])
            dp[r][ord(c) - ord('a')] += 1
            for l, _ in enumerate(S[:r+1]):
                unique_chars = sum(dp[r][j] - dp[l-1][j] == 1 for j in range(26))
                soln = (soln + unique_chars) % MOD
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
