"""
binarysearch.com :: Hop Cost Sequel
jramaswami
"""



import collections


class Solution:
    def solve(self, nums):
        locations = collections.defaultdict(list)
        for i, n in enumerate(nums):
            locations[n].append(i)
        visited = [False for _ in nums]
        queue = collections.deque()
        queue.append((0, 0))
        visited[0] = True
        while queue:
            i, h = queue.popleft()
            if i == len(nums) - 1:
                return h
            if i-1 >= 0 and not visited[i-1]:
                queue.append((i-1, h+1))
                visited[i-1] = True
            if not visited[i+1]:
                queue.append((i+1, h+1))
                visited[i+1] = True
            if locations[nums[i]]:
                for j in locations[nums[i]]:
                    queue.append((j, h+1))
                locations[nums[i]] = []
        return -1


def test_1():
    nums = [3, 7, 7, 4, 3, 5, 4]
    expected = 3
    assert Solution().solve(nums) == expected