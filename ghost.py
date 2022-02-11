"""
binarysearch.com :: Ghost
jramaswami
"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word_end = False
        self.index = -1
        self.word = ""

    def add(self, index, word):
        self.index = index
        self.word = word
        if index == len(word) - 1:
            self.word_end = True
            return

        if word[index+1] not in self.children:
            self.children[word[index+1]] = TrieNode()
        self.children[word[index+1]].add(index + 1, word)

    def is_winner(self):
        if self.word_end:
            return False
        # If there is a move from the current state to a losing state
        # it is a winning state, otherwise it is a losing state.
        return not all(node.is_winner() for node in self.children.values())


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        self.root.add(-1, word)

    def is_winner(self):
        # Root is the turn before the actual start of the game.
        return not self.root.is_winner()


class Solution:

    def solve(self, words):
        trie = Trie()
        for word in words:
            trie.add_word(word)
        return trie.is_winner()


def test_1():
    words = ["ghost", "ghostbuster", "gas"]
    expected = False
    assert Solution().solve(words) == expected


def test_2():
    "WA"
    words = ["sa", "fi"]
    expected = True
    assert Solution().solve(words) == expected


def test_3():
    "RTE"
    words = ["gr", "rf"]
    expected = True
    assert Solution().solve(words) == expected


def test_4():
    "WA"
    words = ["aba", "accc"]
    expected = False
    assert Solution().solve(words) == expected
