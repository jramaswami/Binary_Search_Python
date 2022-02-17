"""
binarysearch.com :: Cheapest Bus Route
jramaswami
"""


import collections
import heapq


class Solution:

    def solve(self, connections):
        max_bus = max(t[2] for t in connections)
        last_stop = max(max(t[0], t[1]) for t in connections)

        # bus_changes[curr_bus] = next buses
        bus_changes = [set() for _ in range(last_stop+1)]

        # adj[curr_bus][curr_stop] = next stops
        adj = [[[] for _ in range(last_stop+1)] for _ in range(max_bus+1)]

        for curr_stop, next_stop, curr_bus in connections:
            bus_changes[curr_stop].add(curr_bus)
            bus_changes[next_stop].add(curr_bus)
            adj[curr_bus][curr_stop].append(next_stop)

        # visited[bus][stop]
        visited = [[False for _ in range(last_stop+1)] for _ in range(max_bus+1)]

        def ride_bus(curr_bus, init_stop):
            if not visited[curr_bus][init_stop]:
                visited[curr_bus][init_stop] = True
                tqueue = collections.deque()
                tqueue.append(init_stop)
                while tqueue:
                    curr_stop = tqueue.popleft()
                    yield curr_stop, curr_bus
                    for next_stop in adj[curr_bus][curr_stop]:
                        if not visited[curr_bus][next_stop]:
                            visited[curr_bus][next_stop] = True
                            tqueue.append(next_stop)

        queue = collections.deque([(0, -1)])
        curr_cost = 0
        new_queue = collections.deque()
        while queue:

            while queue:
                curr_stop, curr_bus = queue.popleft()

                if curr_stop == last_stop:
                    return curr_cost

                for next_bus in bus_changes[curr_stop]:
                    # Get on next bus at this stop and visit every next stop
                    new_queue.extend(ride_bus(next_bus, curr_stop))

            curr_cost += 1
            queue, new_queue = new_queue, collections.deque()

        return -1


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
