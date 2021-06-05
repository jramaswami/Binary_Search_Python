"""
binarysearch.com :: Justify Text
jramaswami
"""


class Solution:
    def solve(self, words, k):
        lines = []
        curr_line = []
        curr_length = 0
        for word in words:
            if curr_length + len(curr_line) + len(word) > k:
                lines.append((curr_line, curr_length))
                curr_line = [word]
                curr_length = len(word)
            else:
                curr_line.append(word)
                curr_length += len(word)
        if curr_line:
            lines.append((curr_line, curr_length))
        
        soln = []
        for words, length in lines:
            if len(words) == 1:
                soln.append(words[0] +  " " * (k - length))
            else:
                spaces, extra_spaces = divmod(k - length, len(words) - 1)
                new_line = [words[0]]
                for word in words[1:]:
                    if extra_spaces:
                        new_line.append(" " * (spaces + 1))
                        extra_spaces -= 1
                    else:
                        new_line.append(" " * spaces)
                    new_line.append(word)
                soln.append("".join(new_line))

        return soln
            


def test_1():
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    k = 16
    expected = ["the  quick brown", "fox  jumps  over", "the   lazy   dog"]
    assert Solution().solve(words, k) == expected


def test_2():
    words = ["There", "should", "be", "at", "least", "one", "space", "between", "each", "word"]
    k = 16
    expected = ["There  should be", "at   least   one", "space    between", "each        word"]
    assert Solution().solve(words, k) == expected


def test_3():
    """RTE"""
    words = ["abc", "de", "fg", "bfq", "fdgre"]
    k = 5
    expected = ["abc  ", "de fg", "bfq  ", "fdgre"]
    assert Solution().solve(words, k) == expected
