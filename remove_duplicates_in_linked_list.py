"""
binarysearch.com :: Remove Duplicates in Linked List
"""
from operator import itemgetter
from itertools import groupby


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def list_to_ll(arr):
    if not arr:
        return None
    head = LLNode(arr[0])
    prev = head
    for v in arr[1:]:
        node = LLNode(v)
        prev.next = node
        prev = node
    return head


def ll_to_list(head):
    arr =[]
    node = head
    while node:
        arr.append(node.val)
        node = node.next
    return arr


class Solution:
    def solve(self, node):
        if node == None:
            return None
        # Convert to list of tuples (value, index).
        arr = sorted((a, i) for i, a in enumerate(ll_to_list(node)))
        # Sort.  This will group values together with lowest index first.
        arr.sort()
        arr0 = [arr[0]]
        # Compress arr into arr0 by filtering duplicates.
        for i in range(1, len(arr)):
            if arr[i][0] != arr[i-1][0]:
                arr0.append(arr[i])
        # Sort again, this time by the index.
        arr0.sort(key=itemgetter(1))
        return list_to_ll([a for a, _ in arr0])


def test_1():
    ll = list_to_ll([1, 2, 1, 3])
    result = Solution().solve(ll)
    assert ll_to_list(result) == [1, 2, 3]

def test_2():
    ll = list_to_ll([1, 1, 2, 2])
    result = Solution().solve(ll)
    assert ll_to_list(result) == [1, 2]

def test_3():
    ll = list_to_ll([])
    result = Solution().solve(ll)
    assert ll_to_list(result) == []
