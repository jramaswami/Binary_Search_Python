"""
binarysearch.com :: Embolden
jramaswami
"""

class Solution:

    def solve(self, text, patterns):
        bold = [0 for _ in text]
        for pattern in set(patterns):
            index = text.find(pattern)
            while index >= 0:
                for i in range(index, index + len(pattern)):
                    bold[i] = 1
                index = text.find(pattern, index + 1)

        soln = []
        for i, c in enumerate(text):
            if bold[i] and i == 0:
                soln.append('<b>')
            elif bold[i] and not bold[i-1]:
                soln.append('<b>')

            soln.append(c)

            if bold[i] and i == len(text) - 1:
                soln.append('</b>')
            elif bold[i] and not bold[i+1]:
                soln.append('</b>')

        return "".join(soln)


def test_1():
    text = "abcdefg"
    patterns = ["bc", "ef"]
    expected = "a<b>bc</b>d<b>ef</b>g"
    assert Solution().solve(text, patterns) == expected


def test_2():
    text = "abcdefg"
    patterns = ["bc", "de"]
    expected = "a<b>bcde</b>fg"
    assert Solution().solve(text, patterns) == expected


def test_3():
    """WA"""
    text = "cbbabcacbbccbacbaccbbcabcabbbccbcbbcaaabcacbaabaabaccacaaccbbbaaaabcbccaacbcacabbcbacbbcbbccccbababc"
    patterns = ["bba", "bbb", "baa", "baa", "aba", "bab", "abb", "abb", "bbb", "aab"]
    expected = "c<b>bbab</b>cacbbccbacbaccbbcabc<b>abbb</b>ccbcbbca<b>aab</b>cac<b>baabaaba</b>ccacaacc<b>bbbaaaab</b>cbccaacbcac<b>abb</b>cbacbbcbbcccc<b>babab</b>c"
    assert Solution().solve(text, patterns) == expected
