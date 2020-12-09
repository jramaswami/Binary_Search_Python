"""
binarysearch.com :: One Edit Distance
https://binarysearch.com/problems/One-Edit-Distance
"""
class Solution:
    def solve(self, s0, s1):
        i = 0
        j = 0
        edits = 0
        while i < len(s0) and j < len(s1):
            if s0[i] != s1[j]:
                if len(s0) == len(s1):
                    # Even length, change one character
                    edits += 1
                    # Advance both pointers
                    i += 1
                    j += 1
                elif len(s0) < len(s1):
                    # Delete the char from s1 by advancing the pointer
                    j += 1
                    edits += 1
                elif len(s1) < len(s0):
                    i += 1
                    edits += 1
            else:
                # Advance both pointers
                i += 1
                j += 1

        # Handle uneven lengths, adding/deleting to make even
        while i < len(s0):
            i += 1
            edits += 1
        while j < len(s1):
            j += 1
            edits += 1

        return edits <= 1


def test_1():
    s0 = "quicksort"
    s1 = "quicksort"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_2():
    s0 = "mergesort"
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_3():
    s0 = "mergeport"
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == False

def test_4():
    s0 = ""
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == False

def test_5():
    s0 = ""
    s1 = ""
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_6():
    s0 = "luxrwvzjexvfugmjytymnvirllgaztthzevojaceikfhapsbizntbzooagnehmyakjtkkpdqzrycyzqmiiqddwxusuawreyjeeknrhsohkdgkkchollqnnqjjwjokisqcfwqxvmerjgbdsqqfchtommkgetqdrrwiyaondfnylqsynxhqkedlcqglozcpmvwkhklflinwfevkxhntntfgvpqfyoiucrlnthlxdpdfmsocsjleihahghbvywgjrksofylvkdodicntislvxwyfaucqybnqscytuteccxwdwylswiiqkpptvaezhxvkurfvofagxdcjhmpleyltjqlqxsgyolvgyxwoxvafqglenpsdabouapxgxarignhevoyinqxegohecgmdepjcrjjfvnlfvpoaanvybmcldlisvltbrjwpiwfvqssvzmjecduffgbazhgtenlkxlrarscapedmanpocclifvugncrnyqmhgjqdurcnsmpvojvxhlqtpwulevbnahqmihedgibvpvrwupwkbomdwdrldcywtbkivgyakssuujfmphssluldpusavrdhbbapbbdbizgelbzrfofwbiblsimzuqbqxnjxvpjfesvpozwcksgpytrkserpfehziyqamztqqimyalsldqebicytjcatvhlvxvxernjfnynifbdtfyvjdrnemjnougsqvoffjtslpnznvaemsmenydwpmekdwrzdqkcdetxapxiwedsyfaltiavppscbkpymlofvzhacjnronkapjgooocsnkhpjwxukyeqflqbnnztbmojczqzhlpxwctuckmeyhyyxbaigxkyekyfgrvjxrajfggpcgkgqvwkgwwydewkznnzsrbvrikefkcskahltbyvuppenmcnnwkanvqkmkjpkaipnqyjuzyjfsgrkzzcicdmudoryjhlnecgiyrqzomgtcdwvwyigtljenyyvdwdryclwjsq"
    s1 = "luxrwvzjexvfugmjytymnvirllgaztthzevojaceikfhapsbizntbzooagnehmyakjtkkpdqzrycyzqmiiqddwxusuawreyjeeknrhsohkdgkkchollqnnqjjwjokisqcfwqxvmerjgbdsqqfchtommkgetqdrrwiyaondfnylqsynxhqkedlcqglozcpmvwkhklflinwfevkxhntntfgvpqfyoiucrlnthlxdpdfmsocsjleihahghbvywgjrksofylvkdodicntislvxwyfaucqybnqscytuteccxwdwylswiiqkpptvaezhxvkurfvofagxdcjhmpleyltjqlqxsgyolvgyxwoxvafqglenpsdabouapxgxarignhevoyinqxegohecgmdepjcrjjfvnlfvpoaanvybmcldlisvltbrjwpiwfvqssvzmjecduffgbazhgtenlkxlrarscapedmanpocclifvugncrnyqmhgjqdurcnsmpvojvxhlqtpwulevbnahqmihedgibvpvrwupwkbomdwdrldcywtbkivgyakssuujfmphssluldpusavrhbbapbbdbizgelbzrfofwbiblsimzuqbqxnjxvpjfesvpozwcksgpytrkserpfehziyqamztqqimyalsldqebicytjcatvhlvxvxernjfnynifbdtfyvjdrnemjnougsqvoffjtslpnznvaemsmenydwpmekdwrzdqkcdetxapxiwedsyfaltiavppscbkpymlofvzhacjnronkapjgooocsnkhpjwxukyeqflqbnnztbmojczqzhlpxwctuckmeyhyyxbaigxkyekyfgrvjxrajfggpcgkgqvwkgwwydewkznnzsrbvrikefkcskahltbyvuppenmcnnwkanvqkmkjpkaipnqyjuzyjfsgrkzzcicdmudoryjhlnecgiyrqzomgtcdwvwyigtljenyyvdwdryclwjsq"
    solver = Solution()
    assert solver.solve(s0, s1) == True