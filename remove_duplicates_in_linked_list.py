"""
binarysearch.com :: Remove Duplicates in Linked List
"""
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
        curr_node = node
        while curr_node != None:
            value = curr_node.val
            node0 = curr_node
            while node0.next != None:
                if node0.next.val == value:
                    node0.next = node0.next.next
                else:
                    node0 = node0.next
            curr_node = curr_node.next
        return node


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
