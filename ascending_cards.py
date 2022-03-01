"""
binarysearch.com :: Ascending Cards
jramaswami
"""


import collections


class Solution:
    def solve(self, cards):
        cards.sort()
        deck = collections.deque(range(len(cards)))
        order = []
        while deck:
            order.append(deck.popleft())
            deck.rotate(-1)
        soln = list(cards)
        for i, c in zip(order, cards):
            soln[i] = c
        return soln


#
# TESTING
#


import random


def check(deck):
    deck0 = collections.deque(deck)
    order = []
    while deck0:
        order.append(deck0.popleft())
        deck0.rotate(-1)
    return sorted(deck) == order


def test_1():
    cards = [1, 2, 3, 4, 5]
    expected = [1, 5, 2, 4, 3]
    assert Solution().solve(cards) == expected


def test_2():
    cards = list(range(1, 31))
    assert check(Solution().solve(cards))


def test_3():
    N = 100000
    cards = [random.randint(-1000, 1000) for _ in range(N)]
    assert check(Solution().solve(cards))


def test_random():
    for _ in range(100):
        N = random.randint(0, 100000)
        cards = [random.randint(-1000, 1000) for _ in range(N)]
        assert check(Solution().solve(cards))

