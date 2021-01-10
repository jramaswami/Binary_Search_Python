"""
binarysearch.com :: Longest Concatenated String
jramaswami
"""
from collections import defaultdict


def dfs(wd, acc, first_letter, visited, words, starts_with):
    result = 0
    if first_letter == words[wd][-1]:
        result = acc

    found = False
    last_letter = words[wd][-1]
    for wd0 in starts_with[last_letter]:
        if not visited[wd0] and wd < wd0:
            visited[wd0] = True
            found = True
            result = max(result, dfs(wd0, acc + len(words[wd0]), first_letter, visited, words, starts_with))
            visited[wd0] = False

    return result


class Solution:
    def solve(self, words):
        starts_with = defaultdict(list)
        for i, wd in enumerate(words):
            starts_with[wd[0]].append(i)

        visited = [False for _ in words]
        result = 0
        for wd, _ in enumerate(words):
            visited[wd] = True
            result = max(result, dfs(wd, len(words[wd]), words[wd][0], visited, words, starts_with))
            visited[wd] = False

        return result


def test_1():
    words = ["hello", "olympic", "crunch"]
    assert Solution().solve(words) == 18

def test_2():
    words = ["bc"]
    assert Solution().solve(words) == 0

def test_3():
    words = ["d"]
    assert Solution().solve(words) == 1

def test_4():
    words = ["cd", "d"]
    assert Solution().solve(words) == 1

def test_5():
    words = ["d", "da"]
    assert Solution().solve(words) == 1

def test_6():
    words = ["ac", "bca", "c", "cbab"]
    assert Solution().solve(words) == 1
