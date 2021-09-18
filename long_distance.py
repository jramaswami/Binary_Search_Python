"""
binarysearch.com :: Long Distance
jramaswami
"""

import bisect


class SegmentTree:

    def __init__(self, nums):
        self.tree = [[] for _ in range(2 * len(nums))]
        self.nums = nums
        self.build()

    def merge(self, merge_node_index):
        left_child_index = merge_node_index * 2
        right_child_index = left_child_index + 1
        left_node = self.tree[left_child_index]
        right_node = self.tree[right_child_index]
        merge_node = self.tree[merge_node_index]
        i = 0
        j = 0
        while i < len(left_node) and j < len(right_node):
            if left_node[i] < right_node[j]:
                merge_node.append(left_node[i])
                i += 1
            else:
                merge_node.append(right_node[j])
                j += 1
        while i < len(left_node):
            merge_node.append(left_node[i])
            i += 1
        while j < len(right_node):
            merge_node.append(right_node[j])
            j += 1

    def build(self):
        # Fill bottom of tree.
        for i, n in enumerate(self.nums):
            self.tree[i + len(self.nums)] = [n]

        # Fill upper levels of tree.
        for i in range(len(self.nums)-1, 0, -1):
            self.merge(i)

    def count_less_than(self, node, target):
        # Find the index for the first element less than target.
        i = bisect.bisect_left(self.tree[node], target)
        return i

    def query(self, left, right, target):
        left += len(self.nums)
        right += len(self.nums)
        result = 0
        while left <= right:
            if left % 2 == 1:
                result += self.count_less_than(left, target)
                left += 1
            if right % 2 == 0:
                result += self.count_less_than(right, target)
                right -= 1
            left //= 2
            right //= 2
        return result


class Solution:

    def solve(self, nums):
        st = SegmentTree(nums)
        soln = [st.query(i+1, len(nums)-1, n) for i, n in enumerate(nums)]
        return soln



def test_1():
    nums = [3, 4, 9, 6, 1]
    expected = [1, 1, 2, 1, 0]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().solve(nums) == expected


def test_3():
    nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    expected = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert Solution().solve(nums) == expected


def test_5():
    nums = list(reversed(range(100000)))
    expected = list(reversed(range(100000)))
    assert Solution().solve(nums) == expected


def test_6():
    """WA"""
    nums = [0, 0]
    expected = [0, 0]
    assert Solution().solve(nums) == expected
