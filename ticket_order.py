"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections
import random


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
        treap.subtree_size = 1
        treap.subtree_sum = treap.data
        for child in treap.children:
            treap.subtree_sum += treap_subtree_sum(child)
            treap.subtree_size += treap_subtree_size(child)


def treap_split(treap, x):
    if treap is None:
        return [None, None]
    if treap.data > x:
        left_result = treap_split(treap.children[0], x)
        treap.children[0] = left_result[1]
        treap_recalculate(treap)
        return [left_result[0], treap]
    else:
        right_result = treap_split(treap.children[1], x)
        treap.children[1] = right_result[0]
        treap_recalculate(treap)
        return [treap, right_result[1]]


def treap_merge(left_treap, right_treap):
    if left_treap is None:
        return right_treap
    if right_treap is None:
        return left_treap
    if left_treap.priority < right_treap.priority:
        left_treap.children[1] = treap_merge(left_treap.children[1], right_treap)
        treap_recalculate(left_treap)
        return left_treap
    else:
        right_treap.children[0] = treap_merge(left_treap, right_treap.children[0])
        treap_recalculate(right_treap)
        return right_treap


class Treap:
    def __init__(self, data, priority):
        self.data = data
        # Could be random.
        self.priority = priority
        self.children = [None, None]
        self.subtree_size = 1
        self.subtree_sum = self.data
        treap_recalculate(self)

    def __repr__(self):
        return f"Treap({self.data=} {self.priority=} {self.subtree_size=} {self.subtree_sum=})"


class Solution:

    def solve(self, tickets):
        # TODO: Need a datastructure that allows you to get the sum of elements
        #       less than k and a count of elements greater than or equal to k.
        #       Some kind of balanced binary tree --> a Treap maybe?
        priority = list(range(len(tickets)))
        random.shuffle(priority)

        fwd_treap = Treap(tickets[0], priority[0])
        soln = list(tickets)
        for i, t in enumerate(tickets[1:], start=1):
            # For each person in front of me in the line, I will have to wait
            # for the minimum of how many tickets I buy or how many they will
            # buy.
            # Split in left: people who are buying less tickets than me;
            # and right: people who are buying the same or more tickets
            # than me.
            left, right = treap_split(fwd_treap, t)
            # print(t, left, right)
            # Minimum of how many they will buy.
            soln[i] += treap_subtree_sum(left)
            # Minimum of how many I will buy.
            soln[i] += treap_subtree_size(right) * t
            # Now add me to treap.
            fwd_treap = treap_merge(Treap(t, priority[i]), treap_merge(left, right))

        bkw_treap = Treap(tickets[-1], priority[-1])
        for i in range(len(tickets)-2, -1, -1):
            t = tickets[i]
            # For each person in front of me in the line, I will have to wait
            # for the minimum of how many tickets I buy less the ticket I
            # bought before them, and how many they will buy.
            left, right = treap_split(bkw_treap, t-1)
            # print(t, left, right)
            # Minimum of how many they will buy.
            soln[i] += treap_subtree_sum(left)
            # Minimum of how many I will buy.
            soln[i] += treap_subtree_size(right) * (t-1)
            # Put treap back together
            bkw_treap = treap_merge(Treap(t, priority[i]), treap_merge(left, right))

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


# def test_3():
#     for _ in range(10):
#         tickets = [random.randint(1, 100) for _ in range(10000)]
#         expected = brute_force(tickets)
#     assert Solution().solve(tickets) == expected


# def test_4():
#     for _ in range(100):
#         N = random.randint(0, 1000)
#         tickets = [random.randint(1, 100) for _ in range(N)]
#         expected = brute_force(tickets)
#     assert Solution().solve(tickets) == expected


# def test_5():
#     tickets = []
#     expected = brute_force(tickets)
#     assert Solution().solve(tickets) == expected
