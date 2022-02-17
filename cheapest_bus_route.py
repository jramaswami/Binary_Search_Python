"""
binarysearch.com :: Cheapest Bus Route
jramaswami
"""


import collections
import math
import heapq


class Solution:

    def solve(self, connections):
        routes = collections.defaultdict(lambda: collections.defaultdict(list))
        stops = collections.defaultdict(set)

        last_stop = 0
        for start, stop, bus in connections:
            routes[bus][start].append(stop)
            stops[start].add(bus)
            stops[stop].add(bus)
            last_stop = max(start, stop, last_stop)

        queue = [(0, 0, -1, -1)]
        total_cost = [[math.inf for _ in range(last_stop+1)] for bus in routes]
        while queue:
            curr_cost, curr_stop, curr_bus, init_stop = heapq.heappop(queue)
            if curr_bus >= 0:
                total_cost[curr_bus][curr_stop] = min(total_cost[curr_bus][curr_stop], curr_cost)

            # I can stay on this bus for 0 cost.
            for next_stop in routes[curr_bus][curr_stop]:
                if next_stop != init_stop and total_cost[curr_bus][next_stop] > curr_cost:
                    queue.append((curr_cost, next_stop, curr_bus, init_stop))

            # I can switch buses at cost of 1.
            for next_bus in stops[curr_stop]:
                if curr_bus != next_bus and init_stop != curr_stop:
                    if total_cost[next_bus][curr_stop] > curr_cost + 1:
                        heapq.heappush(queue, (curr_cost + 1, curr_stop, next_bus, curr_stop))

        min_cost = min(total_cost[bus][last_stop] for bus in routes)
        return -1 if min_cost == math.inf else min_cost



def test_1():
    connections = [
        [0, 1, 0],
        [1, 2, 0],
        [0, 3, 1],
        [2, 4, 1],
        [3, 0, 1]
    ]
    expected = 2
    assert Solution().solve(connections) == expected


def test_2():
    connections = [
        [0, 1, 0],
        [1, 2, 1],
        [2, 3, 0]
    ]
    expected = 3
    assert Solution().solve(connections) == expected


def test_3():
    "WA"
    connections = [[0,1,0],[0,2,0]]
    expected = 1
    assert Solution().solve(connections) == expected
