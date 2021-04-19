"""
binarysearch.com :: Bounce
jramaswami
"""
from collections import deque


class Solution:
    def solve(self, nums, k):
        if k == len(nums) - 1:
            return True
        queue = deque([k])
        visited = [False for _ in nums]
        visited[k] = True
        while queue:
            i = queue.popleft()
            # Hop left
            left = i - nums[i]
            if left >= 0 and not visited[left]:
                visited[left] = True
                queue.append(left)
            # Hop right
            right = i + nums[i]
            if right == len(nums) - 1:
                return True
            elif right < len(nums) and not visited[right]:
                visited[right] = True
                queue.append(right)
        return False


def test_1():
    nums = [0, 0, 1, 2, 0, 3]
    k = 2
    expected = True
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [0, 2, 0]
    k = 1
    expected = False
    assert Solution().solve(nums, k) == expected
