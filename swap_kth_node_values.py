"""
binarysearch.com :: Swap Kth Node Values
jramaswami
"""
class Solution:
    def solve(self, node, k):
        # Find k-th from start
        kth_from_start = node
        for _ in range(k):
            # Assume there are at least k elements.
            kth_from_start = kth_from_start.next

        # Find k-th from end
        kth_from_end = node
        fast = kth_from_start
        while fast:
            fast = fast.next
            # Stop when fast is off the end.
            if fast:
                kth_from_end = kth_from_end.next

        # Swap values
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val

        return node


#
# Testing
#
from bscom_linked_lists import *

def test_1():
    node = [1, 2, 3, 4, 5, 6]
    k = 1
    expected = [1, 5, 3, 4, 2, 6]
    result = Solution().solve(list_to_ll(node), k)
    assert ll_to_list(result) == expected

def test_2():
    node = [0, 6, 8, 2, 9]
    k = 2
    expected = [0, 6, 8, 2, 9]
    result = Solution().solve(list_to_ll(node), k)
    assert ll_to_list(result) == expected
