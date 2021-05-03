"""
binarysearch.com :: Word Concatenation
jramaswami
"""
from collections import defaultdict

def char_index(char):
    """Transform lowercase char to 0-26 index."""
    return ord(char) - ord('a')


class TrieNode(object):
    """Trie node implementation."""
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie(object):
    """Trie implementation."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = char_index(char)
            if index not in node.children:
                node.children[index] = TrieNode()
            node = node.children.get(index)
        node.terminating = True

    def search(self, word):
        node = self.root
        for char in word:
            index = char_index(char)
            if node is None:
                return False
            node = node.children.get(index)
        return node and node.terminating

    def concat_search(self, word, i):
        node = self.root
        for j, char in enumerate(word[i:], start=i):
            if node is None:
                return False
            if node.terminating and self.concat_search(word, j):
                return True
            index = char_index(char)
            node = node.children.get(index)
        return node and node.terminating


class Solution:
    def solve(self, words):
        trie = Trie()
        soln = 0
        for word in sorted(words, key=len):
            if trie.concat_search(word, 0):
                soln += 1
            trie.insert(word)
        return soln


def test_1():
    words = ["news", "paper", "newspaper", "binary", "search", "binarysearch"]
    assert Solution().solve(words) == 2