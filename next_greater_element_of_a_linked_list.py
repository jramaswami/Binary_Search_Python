"""
binarysearch.com :: Next Greater Element of a Linked List
jramaswami
"""


class Solution:

    def solve(self, root):

        def traverse(node):
            if node is None:
                return []

            # Stack is monotonically increasing and contains
            stack = traverse(node.next)
            # Make stack contain only values greater than the
            # value of the current node.
            while stack and stack[-1] <= node.val:
                stack.pop()

            curr_val = node.val
            if stack:
                # If there is a value in the stack there is a node
                # to the right of the current node that is greater.
                node.val = stack[-1]
            else:
                # If the stack is empty there is no node greater
                # than the current node.  Set it to 0.
                node.val = 0

            # Add the current node's previous value to the stack.
            # This value is less than any node currently on the stack.
            stack.append(curr_val)

            return stack

        traverse(root)
        return root