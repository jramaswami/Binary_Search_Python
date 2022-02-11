"""
binarysearch.com :: Ghost
jramaswami
"""


class TrieNode:
    def __init__(self, char, index):
        self.children = dict()
        self.word_end = False
        self.word = ""
        self.char = char
        self.index = index

    def add(self, index, word):
        if index == len(word) - 1:
            self.word_end = True
            self.word = word
            return

        if word[index+1] not in self.children:
            self.children[word[index+1]] = TrieNode(word[index + 1], index + 1)
        self.children[word[index+1]].add(index + 1, word)

    def is_winner(self):
        if self.word_end:
            if self.index % 2 == 0:
                # print(self.word, 'is loser at', self.index)
                return False
            else:
                # print(self.word, 'is winner at', self.index)
                return True

        if self.index % 2 == 1:
            # If it is my turn and there are any winners then return a win:
            winner = any(node.is_winner() for node in self.children.values())
            # if winner:
            #     print(self.char, '@', self.index, 'is a winner with a child as winners')
            # else:
            #     print(self.char, '@', self.index, 'is a loser with all childrend as losers')
            return winner
        else:
            # If it is my opponent's turn and there are any losers I lose.
            winner = all(node.is_winner() for node in self.children.values())
            # if winner:
            #     print(self.char, '@', self.index, 'is a winner all children as winners')
            # else:
            #     print(self.char, '@', self.index, 'is a loser with a child as loser')
            return winner


class Trie:

    def __init__(self):
        self.root = TrieNode("", -1)

    def add_word(self, word):
        self.root.add(-1, word)

    def is_winner(self):
        # Root is the turn before the actual start of the game.
        return any(node.is_winner() for node in self.root.children.values())


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
