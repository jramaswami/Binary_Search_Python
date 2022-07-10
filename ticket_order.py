"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections


class Solution:

    def solve(self, tickets):
        fwd_freqs = collections.defaultdict(int)
        soln = list(tickets)
        for i, t in enumerate(tickets):
            # For each person in front of me in the line, I will have to wait
            # for the minimum of how many tickets I buy or how many they will
            # buy.
            for t1, fr in fwd_freqs.items():
                soln[i] += (fr * min(t1, t))
            fwd_freqs[t] += 1

        bkw_freqs = collections.defaultdict(int)
        for i in range(len(tickets)-1, -1, -1):
            t = tickets[i]
            # For each person in front of me in the line, I will have to wait
            # for the minimum of how many tickets I buy less the ticket I
            # bought before them, and how many they will buy.
            for t1, fr in bkw_freqs.items():
                soln[i] += (fr * min(t1, t-1))
            bkw_freqs[t] += 1

        return soln


#
# Testing
#


import random


def brute_force(tickets):
        tickets0 = collections.deque(enumerate(tickets))
        soln = [0 for _ in tickets]
        time = 1
        while tickets0:
            i, x = tickets0.popleft()
            if x - 1 == 0:
                soln[i] = time
            else:
                tickets0.append((i, x - 1))
            time += 1
        return soln


def test_1():
    tickets = [2, 1, 2]
    expected = [4, 2, 5]
    assert Solution().solve(tickets) == expected


def test_2():
    for _ in range(100):
        tickets = [random.randint(1, 100) for _ in range(1000)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_3():
    for _ in range(10):
        tickets = [random.randint(1, 100) for _ in range(10000)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_4():
    for _ in range(100):
        N = random.randint(0, 1000)
        tickets = [random.randint(1, 100) for _ in range(N)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_5():
    tickets = []
    expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected
