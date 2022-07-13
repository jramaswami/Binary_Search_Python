"""
binarysearch.com :: Ticket Order
jramaswami
"""


import collections


class Node:
    def __init__(self, value):
        self.value = value
        self.freq = 1
        self.subtree_size = 1
        self.subtree_sum = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value=} {self.freq=} {self.subtree_size=} {self.subtree_sum=})"


class BST:

    def __init__(self):
        self.root = None

    def put(self, value):
        self.root = self._put(self.root, value)

    def _put(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._put(node.left, value)
        elif value == node.value:
            node.freq += 1
        else:
            node.right = self._put(node.right, value)

        # Recalculate on the way back up.
        node.subtree_size = (
            node.freq +
            self._subtree_size(node.left) +
            self._subtree_size(node.right)
        )
        node.subtree_sum = (
            node.freq * node.value +
            self._subtree_sum(node.left) +
            self._subtree_sum(node.right)
        )
        return node

    def _subtree_size(self, node):
        if node is None:
            return 0
        return node.subtree_size

    def _subtree_sum(self, node):
        if node is None:
            return 0
        return node.subtree_sum

    def sum_lt(self, x):
        return self._sum_lt(self.root, x)

    def _sum_lt(self, node, x):
        if node is None:
            return 0
        if x == node.value:
            # Everything to the left is less than x and must be counted.
            # Everything to the right is greater than x and must be ignored.
            return self._subtree_sum(node.left)
        elif node.value < x:
            # Everything to my left is less than x since I am less than x and
            # must be counted.
            # I am less than x and must be counted.
            # There could be some to my right that should be added.
            return (
                self._sum_lt(node.left, x) +
                self._sum_lt(node.right, x) +
                (node.freq * node.value)
            )
        elif x < node.value:
            # I am more than the node value.  Everything to my right will
            # also be more than the node value and should be ignored.
            # It is possible that values to my left are less than x.
            return self._sum_lt(node.left, x)

    def count_gte(self, x):
        return self._count_gte(self.root, x)

    def _count_gte(self, node, x):
        # print(f"_count_gte({node=} {x=})")
        if node is None:
            return 0
        if x == node.value:
            # Everthing to the left is less than x and should be ignored.
            # Everything to the right + the current node should be counted.
            return node.freq + self._subtree_size(node.right)
        elif x < node.value:
            # Everything to the left is less than node.value. X is less than
            # that so this node and possibly nodes to the right and left
            # will be greate than x.
            return (
                node.freq +
                self._count_gte(node.left, x) +
                self._count_gte(node.right, x)
            )
        elif x > node.value:
            # Everything to the left is less than x and should be ignored.
            return self._count_gte(node.right, x)


class Solution:
    def solve(self, tickets):
        fwd_bst = BST()
        soln = list(tickets)
        for i, t in enumerate(tickets):
            lt_sum = fwd_bst.sum_lt(t)
            gte_count = fwd_bst.count_gte(t)
            soln[i] += lt_sum + (gte_count * t)
            fwd_bst.put(t)

        bkw_bst = BST()
        for i in range(len(tickets)-1, -1, -1):
            t = tickets[i] - 1
            lt_sum = bkw_bst.sum_lt(t)
            gte_count = bkw_bst.count_gte(t)
            soln[i] += lt_sum + (gte_count * t)
            bkw_bst.put(t+1)
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
        N = random.randint(0, 100)
        tickets = [random.randint(1, 1000) for _ in range(N)]
        expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected


def test_5():
    tickets = []
    expected = brute_force(tickets)
    assert Solution().solve(tickets) == expected



#
# Testing for BST
#

def test_bst():

    def bf_sum_lt(A, x):
        return sum(a for a in A if a < x)

    def bf_count_gte(A, x):
        return sum(1 for a in A if a >= x)

    A = [random.randint(10, 100) for _ in range(1000)]
    bst = BST()
    for i, n in enumerate(A):
        lt = random.randint(1, n)
        gt = random.randint(n+1, 1000)
        assert bf_sum_lt(A[:i], lt) == bst.sum_lt(lt)
        assert bf_sum_lt(A[:i], gt) == bst.sum_lt(gt)
        assert bf_sum_lt(A[:i], n) == bst.sum_lt(n)

        assert bf_count_gte(A[:i], lt) == bst.count_gte(lt)
        assert bf_count_gte(A[:i], gt) == bst.count_gte(gt)
        assert bf_count_gte(A[:i], gt) == bst.count_gte(gt)
        bst.put(n)
