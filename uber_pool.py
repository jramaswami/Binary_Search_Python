"""
binarysearch.com :: Uber Pool
jramaswami
"""


import collections


Event = collections.namedtuple('Event', ['x', 'delta'])


class Solution:
    def solve(self, trips, capacity):
        events = []
        for start_x, end_x, num_passengers in trips:
            events.append(Event(start_x, num_passengers))
            events.append(Event(end_x, -num_passengers))
        events.sort()
        curr_passengers = 0
        for event in events:
            curr_passengers += event.delta
            if curr_passengers > capacity:
                return False
        return True


def test_1():
    trips = [
        [1, 30, 2],
        [3, 5, 3],
        [5, 9, 3]
    ]
    capacity = 6
    expected = True
    assert Solution().solve(trips, capacity) == expected


def test_2():
    trips = [
        [1, 30, 2],
        [3, 6, 3],
        [5, 9, 3]
    ]
    capacity = 6
    expected = False
    assert Solution().solve(trips, capacity) == expected
