"""
binarysearch.com :: Reverse Words Sequel
jramaswami
"""


from collections import namedtuple


Word = namedtuple('Word', ['start', 'end'])


class Solution:
    def solve(self, sentence, delimiters):
        # No constraints given.
        # How many delimiters?
        # Are delimiters single characters?

        def word_to_string(word):
            return sentence[word.start:word.end+1]

        # Separate the words and the delimeters. For the words, just
        # keep track of the indices.
        just_words = []
        curr = None
        for i, c in enumerate(sentence):
            if c in delimiters:
                if curr is not None:
                    just_words.append(curr)
                curr = None
            else:
                if curr is None:
                    curr = Word(i, i)
                else:
                    curr = Word(curr.start, i)

        # Don't forget the last word.
        if curr is not None:
            just_words.append(curr)

        # Now do the same thing but when you would have appended a word to
        # just_words, instead append the last item still in just words to
        # the new sentence.
        new_sentence = []
        curr = None
        for i, c in enumerate(sentence):
            if c in delimiters:
                if curr is not None:
                    new_sentence.append(word_to_string(just_words.pop()))
                new_sentence.append(c)
                curr = None
            else:
                if curr is None:
                    curr = Word(i, i)
                else:
                    curr = Word(curr.start, i)

        # Don't forget the last word.
        if curr is not None:
            new_sentence.append(word_to_string(just_words.pop()))

        return "".join(new_sentence)


def test_1():
    sentence = "hello/world:here"
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == "here/world:hello"


def test_2():
    sentence = "hello/world:here/"
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == "here/world:hello/"


def test_3():
    sentence = "hello//world:here"
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == "here//world:hello"


def test_4():
    sentence = "//:"
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == "//:"


def test_5():
    sentence = ""
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == ""


def test_6():
    sentence = "alksfdjalkjsdhflak"
    delimiters = ["/", ":"]
    assert Solution().solve(sentence, delimiters) == sentence