"""
binarysearch.com :: Flight Itinerary
jramaswami
"""


import collections


class Solution:

    def solve(self, edges):
        if edges == []:
            return []

        def dfs(node, graph, visited, acc):
            "Topological sort using dfs."
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, graph, visited, acc)
            acc.appendleft(node)

        # Build graph and find root node (no indegree)
        indegree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for left, right in edges:
            graph[left].append(right)
            indegree[right] += 1
        root = [node for node in graph if indegree[node] == 0][0]

        # Topological sort to get order of visits.
        topo = collections.deque()
        visited = set()
        dfs(root, graph, visited, topo)
        return list(topo)


def test_1():
    flights = [
        ["WRE", "RPM"],
        ["AGN", "WRE"],
        ["NTL", "AGN"]
    ]
    expected = ["NTL", "AGN", "WRE", "RPM"]
    assert Solution().solve(flights) == expected
