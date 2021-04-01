"""
binarysearch.com :: Palindrome Linked List
jramaswami


There is a LeetCode version of this problem.  I solved that one in O(1)
space by manipulating the links of the linked list.  This is a far easier
way to solve this problem!
"""
class Solution:
    def solve(self, node):
        L = []
        curr = node
        while curr:
            L.append(curr.val)
            curr = curr.next
        return L == L[::-1]

