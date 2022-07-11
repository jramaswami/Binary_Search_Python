"""
binarysearch.com :: Ticket Order
jramaswami
"""


import random

"""
TODO: Try sqrt decomp.
Let X = max(tickets) - min(tickets).
Have sqrt(X) buckets.
Each bucket keeps track of sum and size.
Update is simply adding to bucket O(N).
"""

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.subtree_sum = value
        self.subtree_size = 1

    def __repr__(self):
        return f"Node({self.value=} {self.priority=} {self.subtree_sum=} {self.subtree_size=})"


def treap_subtree_size(node):
    return node.subtree_size if node else 0


def treap_subtree_sum(node):
    return node.subtree_sum if node else 0


def treap_recalculate(node):
    "Recompute the subtree statistics."
    if node:
        node.subtree_size = (1 + treap_subtree_size(node.left) + treap_subtree_size(node.right))
        node.subtree_sum = (1 + treap_subtree_sum(node.left) + treap_subtree_sum(node.right))


def treap_split(root, x):
    """
    Split the tree into left and right.
    Left contains all nodes such that node.value < x.
    Right contains all nodes such that x <= node.value.
    """
    if root is None:
        return None, None
    elif root.value is None:
        return None, None
    else:
        if x < root.value:
            # Right tree's root will be the current node. Now we split
            # current node's left subtree.
            left, root.left = treap_split(root.left, x)
            treap_recalculate(left)
            treap_recalculate(root)
            return left, root
        else:
            root.right, right = treap_split(root.right, x)
            treap_recalculate(right)
            treap_recalculate(root)
            return root, right


def treap_merge(left, right):
    "Merge two trees into a single tree."
    if left is None:
        return right
    elif right is None:
        return left
    elif left.priority < right.priority:
        # Left will be root.
        left.right = treap_merge(left.right, right)
        treap_recalculate(left.right)
        treap_recalculate(left)
        return left
    else:
        right.left = treap_merge(left, right.left)
        treap_recalculate(right.left)
        treap_recalculate(right)
        return right


def treap_insert(root, node):
    left, right = treap_split(root, node.value)
    return treap_merge(treap_merge(left, node), right)



class Solution:
    def solve(self, tickets):
        priority = list(range(len(tickets)))
        random.shuffle(priority)
        soln = list(tickets)
        fwd_treap = None
        for i, t in enumerate(tickets):
            lt, gte = treap_split(fwd_treap, t - 0.1)
            print(f"fwd {t=} {lt=} {gte=}")
            # For the people in front that are buying less tickets than I am,
            # I will wait for the time it takes them to buy their tickets.
            soln[i] += treap_subtree_sum(lt)
            # For the people in front that are buying the same for more tickets
            # than I am, I will wait my number of tickets for each of them.
            soln[i] += (t * treap_subtree_size(gte))
            # Put treap back together
            fwd_treap = treap_merge(lt, gte)
            # Add current ticket.
            fwd_treap = treap_insert(fwd_treap, Node(t, priority[i]))

        bkw_treap = None
        for i in range(len(tickets)-1, -1, -1):
            # For people behind me, imagine I am in front.  I buy one ticket
            # and then move to the back.  At that point we can apply the same
            # logic as above.  So by the ticket and then compute against all
            # those behind me.
            t = max(0, tickets[i] - 1)
            lt, gte = treap_split(bkw_treap, t - 0.1)
            print(f"bkw {t+1=} {t=} {lt=} {gte=}")
            # For the people in back that are buying less tickets than I am,
            # I will wait for the time it takes them to buy their tickets.
            soln[i] += treap_subtree_sum(lt)
            # For the people in back that are buying the same for more tickets
            # than I am, I will wait my number of tickets for each of them.
            soln[i] += (t * treap_subtree_size(gte))
            # Put treap back together
            bkw_treap = treap_merge(lt, gte)
            # Add current ticket.
            bkw_treap = treap_insert(bkw_treap, Node(t, priority[i]))

        return soln

#
# Testing
#


import collections


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
