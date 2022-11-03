"""
binarysearch.com :: Weekly Contest 42 :: Fix Flight Itinerary
jramaswami
"""
from collections import defaultdict
from math import inf


class Solution:
    def solve(self, itinerary, edges):
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        cost = dict()
        x = itinerary[0]
        for u in adj:
            delta = sum(1 if a != b else 0 for a, b in zip(x, u))
            cost[u] = delta

        new_cost = defaultdict(lambda: inf)
        for x in itinerary[1:]:
            for u in adj:
                for v in adj[u]:
                    delta = sum(1 if a != b else 0 for a, b in zip(x, v))
                    new_cost[v] = min(new_cost[v], cost[u] + delta)
            cost, new_cost = new_cost, defaultdict(lambda: inf)

        return min(cost.values())

def test_1():
    itinerary = ["YYZ", "SFO", "JFK"]
    edges = [
        ["YYZ", "SEA"],
        ["SEA", "JAM"],
        ["SEA", "JFL"]
    ]
    assert Solution().solve(itinerary, edges) == 3

def test_2():
    itinerary = ["YYZ", "SFO", "JFK"]
    edges = [
        ["YYZ", "SFO"],
        ["SFO", "JFK"]
    ]
    assert Solution().solve(itinerary, edges) == 0
