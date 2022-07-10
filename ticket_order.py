"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections


class Solution:

    def solve(self, tickets):
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
