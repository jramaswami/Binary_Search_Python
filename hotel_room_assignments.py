"""
binarysearch.com :: Hotel Room Assignments
jramaswami
"""


import collections
import heapq


Event = collections.namedtuple('Event', ['time', 'type', 'index'])


CHECKOUT = 0
CHECKIN = 1


class Solution:

    def solve(self, intervals):
        # Convert intervals into events.
        events = []
        for index, (timein, timeout) in enumerate(intervals):
            events.append(Event(timein, CHECKIN, index))
            events.append(Event(timeout, CHECKOUT, index))
        events.sort()

        room_no = [-1 for _ in intervals]
        next_room = 0
        available_rooms = []
        for event in events:
            if event.type == CHECKIN:
                if available_rooms:
                    room_no[event.index] = available_rooms[0]
                    heapq.heappop(available_rooms)
                else:
                    room_no[event.index] = next_room
                    next_room += 1
            else:
                heapq.heappush(available_rooms, room_no[event.index])
        return room_no


def test_1():
    intervals = [ [1, 9], [2, 4], [4, 6], [5, 9] ]
    expected = [0, 1, 1, 2]
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [ [1, 9], [2, 6], [6, 7], [3, 10] ]
    expected = [0, 1, 1, 2]
    assert Solution().solve(intervals) == expected
