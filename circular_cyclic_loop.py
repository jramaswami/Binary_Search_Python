"""
binarysearch.com :: Circular Cyclic Loop
jramaswami
"""


import enum


class Color(enum.Enum):
    WHITE = enum.auto()
    GRAY = enum.auto()
    BLACK = enum.auto()


class Solution:

    def solve(self, nums):

        color = [Color.WHITE for _ in nums]
        parent = [i for i, _ in enumerate(nums)]

        def dfs(node):
            "DFS to detect cycle."
            color[node] = Color.GRAY
            neighbor = (node + nums[node]) % len(nums)
            result = False
            if node != neighbor and nums[neighbor] * nums[node] > 0:
                # Only follow if same sign or cycle will be more than one node.
                if color[neighbor] == Color.WHITE:
                    parent[neighbor] = node
                    result = result or dfs(neighbor)
                elif color[neighbor] == Color.GRAY:
                    result = True
            color[node] = Color.BLACK
            return result

        # Use DFS from each unvisited node to detect a cycle.
        for node, _ in enumerate(nums):
            if color[node] == Color.WHITE:
                if dfs(node):
                    return True
        return False


def test_1():
    nums = [1, 1, 1, 2, 4]
    assert Solution().solve(nums) == True


def test_2():
    nums = [-1, -1, -1]
    assert Solution().solve(nums) == True


def test_3():
    nums = [1, -1]
    assert Solution().solve(nums) == False


def test_4():
    "WA"
    nums = [1]
    assert Solution().solve(nums) == False
