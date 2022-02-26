"""
binarysearch.com :: DDoS Protection
jramaswami
"""


import collections


Request = collections.namedtuple('Request', ['timestamp', 'userid'])


class Solution:

    def solve(self, requests, user_max, global_max):
        requests0 = [Request(t, u) for u, t in requests]
        requests0.sort()

        urqs = collections.defaultdict(int)
        grq = collections.deque()

        processed_requests = 0
        for request in requests0:
            # Remove expired requests.
            while grq and grq[0].timestamp <= request.timestamp - 60:
                uid = grq[0].userid
                urqs[uid] -= 1
                grq.popleft()

            if urqs[request.userid] < user_max and len(grq) < global_max:
                grq.append(request)
                urqs[request.userid] += 1
                processed_requests += 1

        return processed_requests


def test_1():
    requests = [ [0, 1], [0, 2] ]
    u = 1
    g = 5
    expected = 1
    assert Solution().solve(requests, u, g) == expected


def test_2():
    requests = [ [0, 1], [0, 61] ]
    u = 1
    g = 5
    expected = 2
    assert Solution().solve(requests, u, g) == expected
