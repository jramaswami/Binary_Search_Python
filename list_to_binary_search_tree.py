"""
binarysearch.com :: List to Binary Search Tree
jramaswami
"""


class Solution:
    def solve(self, nums):

        def solve0(left, right):
            if left > right:
                return None
            mid = left + ((right - left  + 1) // 2)
            root = Tree(nums[mid])
            root.left = solve0(left, mid - 1)
            root.right = solve0(mid + 1, right)
            return root

        return solve0(0, len(nums) - 1)
