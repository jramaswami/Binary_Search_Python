"""
binarysearch.com :: Binary Circuit
jramaswami
"""


import collections


class Solution:

    def solve(self, words):
        # Corner case:
        if len(words) == 0:
            return False

        # Create a directed graph from the words If we want 4
        # to make a eulerian cycle we must treat the words as
        # edges making the nodes the first and last letters of
        # each word.
        adj = collections.defaultdict(list)
        rev_adj = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)
        out_degree = collections.defaultdict(int)
        letter_nodes = set()
        for word in words:
            # Make an edge from word[0] to word[-1].
            adj[word[0]].append(word[-1])
            # Increment in/out degrees.
            out_degree[word[0]] += 1
            in_degree[word[-1]] += 1
            # Add the letter to our set of nodes.
            letter_nodes.add(word[0])
            letter_nodes.add(word[-1])
            # Reverse graph for Kosaraju's algorithm
            rev_adj[word[-1]].append(word[0])

        # Make sure that the graph is strongly connected using
        # Kosaraju's algorithm.
        def dfs(node, graph, visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, graph, visited)

        fwd_visited = set()
        dfs(word[0][0], adj, fwd_visited)
        if fwd_visited != letter_nodes:
            return False
        rev_visited = set()
        dfs(word[0][0], rev_adj, rev_visited)
        if rev_visited != letter_nodes:
            return False

        # Make sure in degree == out degree for all nodes.
        return all(in_degree[node] == out_degree[node] for node in letter_nodes)


def test_1():
    words = ["chair", "height", "racket", "touch", "tunic"]
    assert Solution().solve(words) == True


def test_2():
    words = []
    assert Solution().solve(words) == False


def test_3():
    words = ["chail", "height", "racket", "touch", "tunic"]
    assert Solution().solve(words) == False