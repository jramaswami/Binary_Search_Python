"""
binarysearch.com :: Sentence Reversal
jramaswami
"""


class Solution:
    def solve(self, sentence):
        sentence = sentence[::-1]
        i = 0
        for j, c in enumerate(sentence):
            if c == " ":
                sentence[i:j] = reversed(sentence[i:j])
                i = j + 1
        sentence[i:] = reversed(sentence[i:])
        return sentence



def test_1():
    sentence = ["h", "i", " ", "w", "o", "r", "l", "d"]
    assert Solution().solve(sentence) == ["w", "o", "r", "l", "d", " ", "h", "i"]


def test_2():
    sentence = list("A programmer walks into a bar")
    expected = list("bar a into walks programmer A")
    assert Solution().solve(sentence) == expected