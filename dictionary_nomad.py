"""
binarysearch.com :: Dictionary Nomad
jramaswami
"""


import collections
import string


class Solution:

    def solve(self, dictionary, start, end):
        visited = {wd: False for wd in dictionary}

        # Boundary case.
        if start == end:
            return 1

        # Boundary case.
        if start not in visited or end not in visited:
            return -1

        def adjacent_words(wd):
            neighbors = []
            for ltr in string.ascii_letters:
                for i, _ in enumerate(wd):
                    # Replace wd[i] with ltr
                    wd0 = wd[:i] + ltr + wd[i+1:]
                    # Only include words that are in the dictionary and unvisited.
                    if wd0 in visited:
                        yield wd0

        queue = collections.deque()
        queue.append((start, 1))
        while queue:
            wd, d = queue.popleft()
            for wd0 in adjacent_words(wd):
                if not visited[wd0]:
                    if wd0 == end:
                        return d + 1
                    queue.append((wd0, d+1))
                    visited[wd0] = True
        return -1


def test_1():
    dictionary = ["day", "say", "soy"]
    start = "soy"
    end = "day"
    expected = 3
    assert Solution().solve(dictionary, start, end) == expected


def test_2():
    dictionary = ["day", "soy"]
    start = "soy"
    end = "day"
    expected = -1
    assert Solution().solve(dictionary, start, end) == expected
