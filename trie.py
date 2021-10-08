"""
binarysearch.com :: Trie
jramaswami
"""


class TrieNode:

    def __init__(self):
        self.value = ""
        self.end_word = False
        self.children = dict()


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_word = True

    def exists(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end_word

    def startswith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


def test_1():
    methods = ["constructor", "add", "exists", "exists", "startswith", "add", "exists"]
    arguments = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expecteds = [None, None, True, False, True, None, True]
    trie = Trie()
    for m, a, e in zip(methods[1:], arguments[1:], expecteds[1:]):
        assert getattr(trie, m)(*a) == e


def test_2():
    methods = ["constructor", "add", "add", "exists", "startswith", "exists"]
    arguments = [[], ["dog"], ["document"], ["dog"], ["doc"], ["doge"]]
    expecteds = [None, None, None, True, True, False]
    trie = Trie()
    for m, a, e in zip(methods[1:], arguments[1:], expecteds[1:]):
        assert getattr(trie, m)(*a) == e
