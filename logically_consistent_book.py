"""
binarysearch.com :: Logically Consistent Book
jramaswami
"""


import collections


class Solution:

    def solve(self, lists):
        # TODO: Implied edges ...
        graph = collections.defaultdict(list)
        start_pages = set()
        end_pages = set()
        for i, (u, v, w) in enumerate(lists):
            u, v = min(u, v), max(u, v)
            graph[u].append((v, w))
            start_pages.add(u)
            end_pages.add(v)

        # DFS Forward Only.
        # At any ending point, all paths from the same starting point
        # must have the same parity.
        def dfs(u, curr_parity, ending_parity):
            for v, w in graph[u]:
                # You can reach the end of page v from the start of page u.
                next_parity = (curr_parity + w) % 2
                if v in ending_parity:
                    # The parities must match.
                    if next_parity != ending_parity[v]:
                        return False
                else:
                    ending_parity[v] = next_parity
                    # Having reached the end of page v, we can turn the
                    # page to the start of page v + 1.
                    if v + 1 in start_pages:
                        dfs(v+1, next_parity, ending_parity)
            return True

        for u in start_pages:
            ending_parity = dict()
            if not dfs(u, 0, ending_parity):
                return False
        return True



def test_1():
    lists = [ [1, 5, 1], [6, 10, 0], [1, 10, 0] ]
    expected = False
    assert Solution().solve(lists) == expected


def test_2():
    lists = [ [0, 2, 0], [2, 4, 0], [0, 4, 0] ]
    expected = True
    assert Solution().solve(lists) == expected


def test_3():
    lists = [ [0, 2, 1], [3, 4, 1], [0, 4, 0] ]
    expected = True
    assert Solution().solve(lists) == expected


def test_4():
    "WA"
    lists = [[1, 1, 1]]
    expected = True
    assert Solution().solve(lists) == expected


def test_5():
    "WA"
    lists = [[0, 0, 1], [0, 1, 0], [1, 2, 0], [2, 2, 0]]
    expected = False
    assert Solution().solve(lists) == expected


def test_6():
    "WA"
    lists = [[0, 1, 0], [0, 2, 0], [1, 1, 1], [1, 2, 0]]
    expected = False
    assert Solution().solve(lists) == expected
