"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections


def treap_subtree_sum(treap):
    if treap is None:
        return 0
    return treap.subtree_sum

def treap_subtree_size(treap):
    if treap is None:
        return 0
    return treap.subtree_size

def treap_recalculate(treap):
    if treap is not None:
        treap._recalculate()

def split_treap(treap, x):
    if treap is None:
        return [None, None]
    if treap.children[0] and treap.data >= x:
        left_result = split_treap(treap.children[0], x)
        treap.children[0] = left_result[1]
        treap._recalculate()
        return [left_result[0], treap]
    else:
        right_result = split_treap(treap_children[1], x)
        treap.children[1] = right_result
        treap._recalculate()
        return [treap, right_result]

def merge_treap(left_treap, right_treap):
    if left_treap is None:
        return right_treap
    if right_treap is None:
        return left_treap
    if left_treap.priority < right_treap.priority:
        left_treap.children[1] = merge_treap(left_treap.children[1], right_treap)
        treap_recalculate(left_treap)
        return left_treap
    else:
        right_treap.children[0] = merge_treap(left_treap, right_treap.children[0])
        treap_recalculate(right_treap)
        return right_treap


class Treap:
    def __init__(self, data, priority):
        self.data = data
        # Could be random.
        self.priority = priority
        self.children = [None, None]
        self._recalculate()

    def _recalculate(self):
        self.subtree_size = 1
        self.subtree_sum = self.data
        for child in self.children:
            if child is not None:
                self.subtree_size += child.subtree_size
                self.subtree_sum += child.subtree_sum

class Solution:

    def solve(self, tickets):
        # TODO: Need a datastructure that allows you to get the sum of elements
        #       less than k and a count of elements greater than or equal to k.
        #       Some kind of balanced binary tree --> a Treap maybe?
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
