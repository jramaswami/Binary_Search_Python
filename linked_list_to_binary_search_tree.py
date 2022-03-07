"""
binarysearch.com :: Linked List to Binary Search Tree
jramaswami
"""


class Solution:

    def solve(self, head):

        A = []
        curr = head
        while curr:
            A.append(curr)
            curr = curr.next

        def build(left, right):
            if left > right:
                return None

            if left == right:
                return Tree(A[right].val, None, None)

            mid = left + ((right - left + 1) // 2)

            return Tree(A[mid].val, build(left, mid-1), build(mid+1, right))

        return build(0, len(A)-1)
