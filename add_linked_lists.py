"""
binarysearch.com :: Add Linked Lists
jramaswami
"""


class Solution:
    def solve(self, left, right):

        def get_val(node):
            """Return value of node or zero if node is None."""
            if node is None:
                return 0
            return node.val

        def traverse(left0, right0, carry, acc):
            """Traverse linked list, building a new linked list with the sum."""
            # Stop when carry is zero and both right and left are empty.
            if carry == 0 and left0 is None and right0 is None:
                return

            curr = carry
            curr += get_val(left0)
            curr += get_val(right0)
            carry, curr = divmod(curr, 10)
            node = LLNode(curr)
            acc.next = node
            return traverse(None if left0 is None else left0.next,
                            None if right0 is None else right0.next,
                            carry, node
            )

        dummy = LLNode(-1)
        traverse(left, right, 0, dummy)
        return dummy.next



#
# Testing
#
from bscom_linked_lists import *

def test_1():
    left = list_to_ll([6, 4])
    right = list_to_ll([4, 7])
    expected = [0, 2, 1]
    assert ll_to_list(Solution().solve(left, right)) == expected
