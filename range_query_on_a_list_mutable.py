"""
binarysearch.com :: Range Query on a List - Mutable
jramaswami
"""


class MutableRangeSum:
    def __init__(self, nums):
        self.N = len(nums)
        self.tree = [0 for _ in range(2 * self.N)]
        # Copy A into bottom of tree
        for i, n in enumerate(nums):
            self.tree[i + self.N] = n
        for i in range(self.N - 1, 0, -1):
            lc = i * 2
            rc = lc + 1
            self.tree[i] = self.tree[lc] + self.tree[rc]

    def total(self, left, right):
        result = 0
        left += self.N
        right += self.N
        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]
            left = left // 2
            right = right // 2
        return result

    def update(self, i, x):
        i += self.N
        self.tree[i] = x
        i = i // 2
        while i > 1:
            lc = i * 2
            rc = lc + 1
            self.tree[i] = self.tree[lc] + self.tree[rc]
            i = i // 2
