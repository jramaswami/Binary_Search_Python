"""
binarysearch.com :: Next Greater Element of a Linked List
jramaswami
"""


class Solution:

    def solve(self, root):
        # Monotonically decreasing stack containing nodes to the left
        # of current node (if any).
        stack = []
        curr_node = root
        while curr_node:
            # For any nodes less than current node, the current node
            # is the next node to the right with a greater value.
            # Remove them from stack and change their value to the current
            # node's value.
            while stack and stack[-1].val < curr_node.val:
                stack[-1].val = curr_node.val
                stack.pop()
            # All nodes in the stack have a value greater than or equal
            # to the current node.  Adding the current node to the stack
            # maintains the monotonically decreasing invariant.
            stack.append(curr_node)
            # Move to the next node.
            curr_node = curr_node.next

        # Any nodes remaining on the stack did not have a node with a
        # greater value to their right.  Change the value of those nodes
        # to zero.
        while stack:
            stack[-1].val = 0
            stack.pop()

        return root