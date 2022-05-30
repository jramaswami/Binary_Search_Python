"""
binarysearch.com :: Mindboggling
jramaswami
"""


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_terminal = False
        self.is_found = False
        self.char = ""


def add(root, word):
    "Add word to Trie."
    curr = root
    for i, c in enumerate(word):
        if c not in curr.children:
            curr.children[c] = TrieNode()
        curr = curr.children[c]
        curr.char = c
        if i == len(word) - 1:
            curr.is_terminal = True


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))

    def solve(self, matrix, words):
        # Add words to Trie
        root = TrieNode()
        for wd in words:
            add(root, wd)

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def dfs(r, c, curr, visited):
            result = 0
            visited[r][c] = True
            if curr.is_terminal and not curr.is_found:
                curr.is_found = True
                result += 1
            for r0, c0 in neighbors(r, c):
                if not visited[r0][c0] and matrix[r0][c0] in curr.children:
                    result += dfs(r0, c0, curr.children[matrix[r0][c0]], visited)
            return result

        soln = 0
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                visited = [[False for _ in row] for row in matrix]
                soln += dfs(r, c, root, visited)
        return soln


def test_1():
    matrix = [
        ["a", "b", "c", "d"],
        ["x", "a", "y", "z"],
        ["t", "z", "r", "r"],
        ["s", "q", "q", "q"]
    ]
    words = ["bar", "car", "cat"]
    expected = 3
    assert Solution().solve(matrix, words) == expected


def test_2():
    "WA"
    matrix = [["a","b","c","d"],["f","a","p","n"],["t","o","r","i"],["s","a","m","q"]]
    words = ["farm","mas","qinpf"]
    expected = 2
    assert Solution().solve(matrix, words) == expected
